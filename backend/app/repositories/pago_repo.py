from sqlalchemy.orm import Session
from backend.app.models.pago import Pago

def get_all_pagos(db: Session):
    return db.query(Pago).order_by(Pago.Fecha_Pago.desc(), Pago.ID_Pago.desc()).all()


def get_pago_by_id(db: Session, pago_id: int):
    return db.query(Pago).filter(Pago.ID_Pago == pago_id).first()


def get_pagos_by_cliente(db: Session, cliente_id: int):
    return (
        db.query(Pago)
        .filter(Pago.ID_Cliente == cliente_id)
        .order_by(Pago.Fecha_Pago.desc(), Pago.ID_Pago.desc())
        .all()
    )


def get_last_pago_by_cliente(db: Session, cliente_id: int):
    return (
        db.query(Pago)
        .filter(Pago.ID_Cliente == cliente_id)
        .order_by(Pago.Fecha_Pago.desc(), Pago.ID_Pago.desc())
        .first()
    )

def create_pago(db: Session, pago: Pago):
    db.add(pago)
    db.commit()
    db.refresh(pago)
    return pago


def update_pago(db: Session, pago: Pago, data: dict):
    for key, value in data.items():
        setattr(pago, key, value)
    db.commit()
    db.refresh(pago)
    return pago


def delete_pago(db: Session, pago: Pago):
    db.delete(pago)
    db.commit()
