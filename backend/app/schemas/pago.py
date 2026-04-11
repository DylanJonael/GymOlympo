from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PagoBase(BaseModel):
    ID_Cliente: int
    ID_Membresia: int


class PagoCreate(PagoBase):
    Fecha_Pago: datetime | None = None


class PagoUpdate(BaseModel):
    ID_Cliente: int | None = None
    ID_Membresia: int | None = None
    Fecha_Pago: datetime | None = None


class PagoResponse(PagoBase):
    ID_Pago: int
    Fecha_Pago: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
