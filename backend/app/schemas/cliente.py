from pydantic import BaseModel

class ClienteBase(BaseModel):
    Nombre: str
    WhatsApp: str | None = None
    Cedula: str

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    ID_Cliente: int

    class Config:
        orm_mode = True# Placeholder for Cliente schemas