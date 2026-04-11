from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.database import Base


class Cliente(Base):
    __tablename__ = "Clientes"

    ID_Cliente: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    Nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    WhatsApp: Mapped[str | None] = mapped_column(String(20), nullable=True)
    Fecha_Registro: Mapped[datetime] = mapped_column(DateTime, server_default=func.getdate())
    Cedula: Mapped[str | None] = mapped_column(String(15), unique=True, nullable=True)

    pagos = relationship("Pago", back_populates="cliente")
