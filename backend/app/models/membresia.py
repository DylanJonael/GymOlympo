from decimal import Decimal

from sqlalchemy import Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.database import Base


class Membresia(Base):
    __tablename__ = "Membresias"

    ID_Membresia: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    Tipo: Mapped[str] = mapped_column(String(50), nullable=False)
    Precio: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    Duracion_Dias: Mapped[int] = mapped_column(Integer, nullable=False)

    pagos = relationship("Pago", back_populates="membresia")
