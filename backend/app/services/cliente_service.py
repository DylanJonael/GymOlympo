from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.app.models.cliente import Cliente
from backend.app.repositories import cliente_repo, pago_repo
from backend.app.schemas.cliente import ClienteCreate, ClienteUpdate
from backend.app.services.estado_membresia_service import build_membership_status_payload


def list_clientes(db: Session):
    return cliente_repo.get_all_clientes(db)


def list_clientes_with_status(db: Session):
    clientes = cliente_repo.get_all_clientes(db)
    response = []
    for cliente in clientes:
        status_payload = build_membership_status_payload(
            pago_repo.get_last_pago_by_cliente(db, cliente.ID_Cliente)
        )
        response.append(
            {
                "ID_Cliente": cliente.ID_Cliente,
                "Nombre": cliente.Nombre,
                "WhatsApp": cliente.WhatsApp,
                "Cedula": cliente.Cedula,
                "Fecha_Registro": cliente.Fecha_Registro,
                "estado_membresia": status_payload["estado"],
                "fecha_vencimiento": status_payload["fecha_vencimiento"],
                "dias_restantes": status_payload["dias_restantes"],
            }
        )
    return response


def get_cliente_or_404(db: Session, cliente_id: int):
    cliente = cliente_repo.get_cliente_by_id(db, cliente_id)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")
    return cliente


def create_cliente(db: Session, payload: ClienteCreate):
    if payload.Cedula and cliente_repo.get_cliente_by_cedula(db, payload.Cedula):
        raise HTTPException(status_code=400, detail="La cedula ya esta registrada.")
    cliente = Cliente(**payload.model_dump())
    try:
        return cliente_repo.create_cliente(db, cliente)
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=400, detail="No se pudo crear el cliente.") from exc


def update_cliente(db: Session, cliente_id: int, payload: ClienteUpdate):
    cliente = get_cliente_or_404(db, cliente_id)
    data = payload.model_dump(exclude_unset=True)
    new_cedula = data.get("Cedula")
    if new_cedula:
        existing = cliente_repo.get_cliente_by_cedula(db, new_cedula)
        if existing and existing.ID_Cliente != cliente_id:
            raise HTTPException(status_code=400, detail="La cedula ya esta registrada.")
    try:
        return cliente_repo.update_cliente(db, cliente, data)
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=400, detail="No se pudo actualizar el cliente.") from exc


def delete_cliente(db: Session, cliente_id: int):
    cliente = get_cliente_or_404(db, cliente_id)
    try:
        cliente_repo.delete_cliente(db, cliente)
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="No se puede eliminar el cliente porque tiene pagos asociados.",
        ) from exc


def get_membership_status(db: Session, cliente_id: int):
    get_cliente_or_404(db, cliente_id)
    status_payload = build_membership_status_payload(
        pago_repo.get_last_pago_by_cliente(db, cliente_id)
    )
    return {"cliente_id": cliente_id, **status_payload}
