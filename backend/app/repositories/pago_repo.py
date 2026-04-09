from sqlalchemy.orm import Session
from backend.app.models.pago import Pago

def get_all_pagos(db: Session):
    return db.query(Pago).all()

def create_pago(db: Session, pago: Pago):
    db.add(pago)
    db.commit()
    db.refresh(pago)
    return pago