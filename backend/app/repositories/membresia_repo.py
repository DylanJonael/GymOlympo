from sqlalchemy.orm import Session
from backend.app.models.membresia import Membresia

def get_all_membresias(db: Session):
    return db.query(Membresia).all()

def create_membresia(db: Session, membresia: Membresia):
    db.add(membresia)
    db.commit()
    db.refresh(membresia)
    return membresia