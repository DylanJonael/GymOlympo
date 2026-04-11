from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.app.database import get_db
from backend.app.schemas.membresia import MembresiaCreate, MembresiaResponse, MembresiaUpdate
from backend.app.services import membresia_service

router = APIRouter()


@router.get("", response_model=list[MembresiaResponse])
def list_membresias(db: Session = Depends(get_db)):
    return membresia_service.list_membresias(db)


@router.post("", response_model=MembresiaResponse, status_code=status.HTTP_201_CREATED)
def create_membresia(payload: MembresiaCreate, db: Session = Depends(get_db)):
    return membresia_service.create_membresia(db, payload)


@router.get("/{membresia_id}", response_model=MembresiaResponse)
def get_membresia(membresia_id: int, db: Session = Depends(get_db)):
    return membresia_service.get_membresia_or_404(db, membresia_id)


@router.put("/{membresia_id}", response_model=MembresiaResponse)
def update_membresia(
    membresia_id: int,
    payload: MembresiaUpdate,
    db: Session = Depends(get_db),
):
    return membresia_service.update_membresia(db, membresia_id, payload)


@router.delete("/{membresia_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_membresia(membresia_id: int, db: Session = Depends(get_db)):
    membresia_service.delete_membresia(db, membresia_id)
