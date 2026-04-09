from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Membresia(Base):
    __tablename__ = 'Membresias'

    ID_Membresia = Column(Integer, primary_key=True, autoincrement=True)
    Tipo = Column(String(50), nullable=False)
    Precio = Column(Numeric(10, 2), nullable=False)
    Duracion_Dias = Column(Integer, nullable=False)