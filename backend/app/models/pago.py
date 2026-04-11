from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.database import Base


class Pago(Base):
    __tablename__ = "Pagos"

    ID_Pago: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ID_Cliente: Mapped[int | None] = mapped_column(ForeignKey("Clientes.ID_Cliente"))
    ID_Membresia: Mapped[int | None] = mapped_column(ForeignKey("Membresias.ID_Membresia"))
    Fecha_Pago: Mapped[datetime] = mapped_column(DateTime, server_default=func.getdate())

    cliente = relationship("Cliente", back_populates="pagos")
    membresia = relationship("Membresia", back_populates="pagos")
