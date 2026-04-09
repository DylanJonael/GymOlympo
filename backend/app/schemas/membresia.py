from pydantic import BaseModel

class MembresiaBase(BaseModel):
    Tipo: str
    Precio: float
    Duracion_Dias: int

class MembresiaCreate(MembresiaBase):
    pass

class MembresiaResponse(MembresiaBase):
    ID_Membresia: int

    class Config:
        orm_mode = True