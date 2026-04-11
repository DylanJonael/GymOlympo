from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ClienteBase(BaseModel):
    Nombre: str = Field(min_length=1, max_length=100)
    WhatsApp: str | None = Field(default=None, max_length=20)
    Cedula: str | None = Field(default=None, max_length=15)


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(BaseModel):
    Nombre: str | None = Field(default=None, min_length=1, max_length=100)
    WhatsApp: str | None = Field(default=None, max_length=20)
    Cedula: str | None = Field(default=None, max_length=15)


class ClienteResponse(ClienteBase):
    ID_Cliente: int
    Fecha_Registro: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class EstadoMembresiaResponse(BaseModel):
    cliente_id: int
    estado: str
    fecha_ultimo_pago: datetime | None = None
    fecha_vencimiento: datetime | None = None
    membresia: str | None = None
    dias_restantes: int | None = None


class ClienteConEstadoResponse(ClienteResponse):
    estado_membresia: str
    fecha_vencimiento: datetime | None = None
    dias_restantes: int | None = None
