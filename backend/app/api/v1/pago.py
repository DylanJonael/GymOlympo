from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.app.database import get_db
from backend.app.schemas.pago import PagoCreate, PagoResponse, PagoUpdate
from backend.app.services import pago_service

router = APIRouter()


@router.get("", response_model=list[PagoResponse])
def list_pagos(db: Session = Depends(get_db)):
    return pago_service.list_pagos(db)


@router.post("", response_model=PagoResponse, status_code=status.HTTP_201_CREATED)
def create_pago(payload: PagoCreate, db: Session = Depends(get_db)):
    return pago_service.create_pago(db, payload)


@router.get("/{pago_id}", response_model=PagoResponse)
def get_pago(pago_id: int, db: Session = Depends(get_db)):
    return pago_service.get_pago_or_404(db, pago_id)


@router.put("/{pago_id}", response_model=PagoResponse)
def update_pago(pago_id: int, payload: PagoUpdate, db: Session = Depends(get_db)):
    return pago_service.update_pago(db, pago_id, payload)


@router.delete("/{pago_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pago(pago_id: int, db: Session = Depends(get_db)):
    pago_service.delete_pago(db, pago_id)


@router.get("/cliente/{cliente_id}", response_model=list[PagoResponse])
def list_pagos_by_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return pago_service.list_pagos_by_cliente(db, cliente_id)
