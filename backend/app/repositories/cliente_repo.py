from sqlalchemy.orm import Session
from backend.app.models.cliente import Cliente

def get_all_clientes(db: Session):
    return db.query(Cliente).order_by(Cliente.Nombre.asc()).all()

def get_cliente_by_id(db: Session, cliente_id: int):
    return db.query(Cliente).filter(Cliente.ID_Cliente == cliente_id).first()

def get_cliente_by_cedula(db: Session, cedula: str):
    return db.query(Cliente).filter(Cliente.Cedula == cedula).first()


def create_cliente(db: Session, cliente: Cliente):
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente


def update_cliente(db: Session, cliente: Cliente, data: dict):
    for key, value in data.items():
        setattr(cliente, key, value)
    db.commit()
    db.refresh(cliente)
    return cliente


def delete_cliente(db: Session, cliente: Cliente):
    db.delete(cliente)
    db.commit()
