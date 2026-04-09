from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'Clientes'

    ID_Cliente = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(100), nullable=False)
    WhatsApp = Column(String(20))
    Fecha_Registro = Column(DateTime, default=None)
    Cedula = Column(String(15), unique=True)