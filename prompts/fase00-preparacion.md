# FASE 00 – Preparación del Proyecto

## Rol
Actúa como un desarrollador senior full-stack, disciplinado y orientado a arquitectura limpia.

## Contexto General
Se va a desarrollar un sistema **local** de gestión de membresías para un gimnasio.

Stack definido:
- Backend: FastAPI + Python
- Frontend: React 18 + Vite
- Base de datos: SQL Server (SSMS)

⚠️ IMPORTANTE:
- La conexión a la base de datos YA EXISTE.
- NO debes crear ni modificar la conexión.
- NO debes implementar lógica de negocio.
- NO debes adelantar fases futuras.

## Objetivo de esta Fase
Dejar preparada la **estructura base del proyecto**, sin implementar funcionalidades.
Esta fase solo crea carpetas y archivos base.

Nada más.
Nada menos.

## Alcance Permitido
✅ Crear carpetas  
✅ Crear archivos vacíos o con comentarios mínimos  
NO Crear lógica  
NO Escribir endpoints  
NO Definir modelos  
NO Agregar dependencias  
NO Hacer configuraciones complejas  

## Estructura Backend Esperada

Crear la siguiente estructura:

backend/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   ├── services/
│   └── utils/
│
└── requirements.txt

### Reglas Backend
- `main.py` puede contener solo comentarios o un placeholder mínimo
- `database.py` debe quedar intacto (archivo vacío o sin cambios)
- Las carpetas pueden contener archivos `.gitkeep` si es necesario

## Estructura Frontend Esperada

Crear la siguiente estructura:

frontend/
├── src/
│   ├── api/
│   ├── components/
│   ├── pages/
│   ├── hooks/
│   ├── services/
│   ├── App.jsx
│   └── main.jsx

### Reglas Frontend
- `App.jsx` y `main.jsx` pueden estar vacíos o con comentarios mínimos
- NO inicializar Vite
- NO agregar dependencias
- NO escribir lógica React

## Condiciones Estrictas
- No improvisar
- No adelantar trabajo de otras fases
- No suponer funcionalidades futuras
- Mantener el proyecto limpio y ordenado

## Criterio de Finalización
La fase se considera completada cuando:
- La estructura coincide exactamente con lo definido arriba
- No existe lógica implementada
- El proyecto queda listo para comenzar la Fase 01

## Instrucción Final
Limítate estrictamente a esta fase.
Cualquier cosa fuera de este alcance debe ser ignorada.