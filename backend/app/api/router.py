from fastapi import APIRouter
from backend.app.api.v1 import cliente, membresia, pago

api_router = APIRouter()

api_router.include_router(cliente.router, prefix="/clientes", tags=["Clientes"])
api_router.include_router(membresia.router, prefix="/membresias", tags=["Membresias"])
api_router.include_router(pago.router, prefix="/pagos", tags=["Pagos"])