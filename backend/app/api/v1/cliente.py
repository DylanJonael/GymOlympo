from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.app.database import get_db
from backend.app.schemas.cliente import (
    ClienteConEstadoResponse,
    ClienteCreate,
    ClienteResponse,
    ClienteUpdate,
    EstadoMembresiaResponse,
)
from backend.app.services import cliente_service

router = APIRouter()


@router.get("", response_model=list[ClienteConEstadoResponse])
def list_clientes(db: Session = Depends(get_db)):
    return cliente_service.list_clientes_with_status(db)


@router.post("", response_model=ClienteResponse, status_code=status.HTTP_201_CREATED)
def create_cliente(payload: ClienteCreate, db: Session = Depends(get_db)):
    return cliente_service.create_cliente(db, payload)


@router.get("/{cliente_id}", response_model=ClienteResponse)
def get_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return cliente_service.get_cliente_or_404(db, cliente_id)


@router.put("/{cliente_id}", response_model=ClienteResponse)
def update_cliente(cliente_id: int, payload: ClienteUpdate, db: Session = Depends(get_db)):
    return cliente_service.update_cliente(db, cliente_id, payload)


@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente_service.delete_cliente(db, cliente_id)


@router.get("/{cliente_id}/estado-membresia", response_model=EstadoMembresiaResponse)
def get_estado_membresia(cliente_id: int, db: Session = Depends(get_db)):
    return cliente_service.get_membership_status(db, cliente_id)
