from pydantic import BaseModel
from datetime import datetime

class PagoBase(BaseModel):
    ID_Cliente: int
    ID_Membresia: int
    Fecha_Pago: datetime

class PagoCreate(PagoBase):
    pass

class PagoResponse(PagoBase):
    ID_Pago: int

    class Config:
        orm_mode = True