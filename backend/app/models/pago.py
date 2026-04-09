from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Pago(Base):
    __tablename__ = 'Pagos'

    ID_Pago = Column(Integer, primary_key=True, autoincrement=True)
    ID_Cliente = Column(Integer, ForeignKey('Clientes.ID_Cliente'))
    ID_Membresia = Column(Integer, ForeignKey('Membresias.ID_Membresia'))
    Fecha_Pago = Column(DateTime, default=None)

    cliente = relationship('Cliente', back_populates='pagos')
    membresia = relationship('Membresia', back_populates='pagos')