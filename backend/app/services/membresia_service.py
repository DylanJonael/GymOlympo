from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.app.models.membresia import Membresia
from backend.app.repositories import membresia_repo
from backend.app.schemas.membresia import MembresiaCreate, MembresiaUpdate


def list_membresias(db: Session):
    return membresia_repo.get_all_membresias(db)


def get_membresia_or_404(db: Session, membresia_id: int):
    membresia = membresia_repo.get_membresia_by_id(db, membresia_id)
    if membresia is None:
        raise HTTPException(status_code=404, detail="Membresia no encontrada.")
    return membresia


def create_membresia(db: Session, payload: MembresiaCreate):
    membresia = Membresia(**payload.model_dump())
    try:
        return membresia_repo.create_membresia(db, membresia)
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=400, detail="No se pudo crear la membresia.") from exc


def update_membresia(db: Session, membresia_id: int, payload: MembresiaUpdate):
    membresia = get_membresia_or_404(db, membresia_id)
    data = payload.model_dump(exclude_unset=True)
    try:
        return membresia_repo.update_membresia(db, membresia, data)
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=400, detail="No se pudo actualizar la membresia.") from exc


def delete_membresia(db: Session, membresia_id: int):
    membresia = get_membresia_or_404(db, membresia_id)
    try:
        membresia_repo.delete_membresia(db, membresia)
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="No se puede eliminar la membresia porque tiene pagos asociados.",
        ) from exc
