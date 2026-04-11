from sqlalchemy.orm import Session
from backend.app.models.membresia import Membresia

def get_all_membresias(db: Session):
    return db.query(Membresia).order_by(Membresia.Tipo.asc()).all()


def get_membresia_by_id(db: Session, membresia_id: int):
    return db.query(Membresia).filter(Membresia.ID_Membresia == membresia_id).first()

def create_membresia(db: Session, membresia: Membresia):
    db.add(membresia)
    db.commit()
    db.refresh(membresia)
    return membresia


def update_membresia(db: Session, membresia: Membresia, data: dict):
    for key, value in data.items():
        setattr(membresia, key, value)
    db.commit()
    db.refresh(membresia)
    return membresia


def delete_membresia(db: Session, membresia: Membresia):
    db.delete(membresia)
    db.commit()
