from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.app.models.pago import Pago
from backend.app.repositories import cliente_repo, membresia_repo, pago_repo
from backend.app.schemas.pago import PagoCreate, PagoUpdate


def list_pagos(db: Session):
    return pago_repo.get_all_pagos(db)


def get_pago_or_404(db: Session, pago_id: int):
    pago = pago_repo.get_pago_by_id(db, pago_id)
    if pago is None:
        raise HTTPException(status_code=404, detail="Pago no encontrado.")
    return pago


def list_pagos_by_cliente(db: Session, cliente_id: int):
    if cliente_repo.get_cliente_by_id(db, cliente_id) is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")
    return pago_repo.get_pagos_by_cliente(db, cliente_id)


def _validate_relations(db: Session, cliente_id: int, membresia_id: int):
    if cliente_repo.get_cliente_by_id(db, cliente_id) is None:
        raise HTTPException(status_code=400, detail="El cliente no existe.")
    if membresia_repo.get_membresia_by_id(db, membresia_id) is None:
        raise HTTPException(status_code=400, detail="La membresia no existe.")


def create_pago(db: Session, payload: PagoCreate):
    _validate_relations(db, payload.ID_Cliente, payload.ID_Membresia)
    pago = Pago(
        ID_Cliente=payload.ID_Cliente,
        ID_Membresia=payload.ID_Membresia,
        Fecha_Pago=payload.Fecha_Pago or datetime.now(),
    )
    try:
        return pago_repo.create_pago(db, pago)
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=400, detail="No se pudo registrar el pago.") from exc


def update_pago(db: Session, pago_id: int, payload: PagoUpdate):
    pago = get_pago_or_404(db, pago_id)
    data = payload.model_dump(exclude_unset=True)
    cliente_id = data.get("ID_Cliente", pago.ID_Cliente)
    membresia_id = data.get("ID_Membresia", pago.ID_Membresia)
    _validate_relations(db, cliente_id, membresia_id)
    try:
        return pago_repo.update_pago(db, pago, data)
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=400, detail="No se pudo actualizar el pago.") from exc


def delete_pago(db: Session, pago_id: int):
    pago = get_pago_or_404(db, pago_id)
    pago_repo.delete_pago(db, pago)
