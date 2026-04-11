from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class MembresiaBase(BaseModel):
    Tipo: str = Field(min_length=1, max_length=50)
    Precio: Decimal = Field(gt=0)
    Duracion_Dias: int = Field(gt=0)


class MembresiaCreate(MembresiaBase):
    pass


class MembresiaUpdate(BaseModel):
    Tipo: str | None = Field(default=None, min_length=1, max_length=50)
    Precio: Decimal | None = Field(default=None, gt=0)
    Duracion_Dias: int | None = Field(default=None, gt=0)


class MembresiaResponse(MembresiaBase):
    ID_Membresia: int

    model_config = ConfigDict(from_attributes=True)
