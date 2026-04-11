# GymOlympo

Sistema local de gestion de membresias para un gimnasio, construido con FastAPI y React.

## Backend

- API REST bajo `/api/v1`
- Entidades principales: clientes, membresias y pagos
- Estado de membresia calculado en backend

Ejecutar:

```bash
uvicorn backend.app.main:app --reload
```

## Frontend

- SPA en React + Vite
- Consumo de API con Axios
- Vistas para clientes, membresias y pagos

Ejecutar:

```bash
cd frontend
npm run dev
```

Variable esperada para el frontend:

```bash
VITE_API_BASE_URL=http://localhost:8000/api/v1
```
