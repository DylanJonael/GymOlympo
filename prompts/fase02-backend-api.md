# Fase 02 – Backend API (FastAPI)

## Objetivo

Construir el backend del sistema de gestión de membresías del gimnasio usando **FastAPI**, exponiendo una API REST clara, segura y alineada estrictamente con los modelos definidos en la **Fase 01**.

Esta fase se enfoca en:

* Configuración base del backend
* Implementación de CRUDs
* Reglas mínimas de negocio

Nada de magia negra todavía. Primero, cimientos sólidos.

---

## Stack Backend

* **Python 3.11+**
* **FastAPI** – framework principal
* **Uvicorn** – servidor ASGI
* **SQLAlchemy 2.0** – ORM
* **Pydantic v2** – validación de datos


---

## Estructura de Carpetas

```
backend/
├── app/
│   ├── main.py
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   ├── models/
│   │   ├── cliente.py
│   │   ├── membresia.py
│   │   └── pago.py
│   ├── schemas/
│   │   ├── cliente.py
│   │   ├── membresia.py
│   │   └── pago.py
│   ├── repositories/
│   │   ├── cliente_repo.py
│   │   ├── membresia_repo.py
│   │   └── pago_repo.py
│   ├── services/
│   │   ├── cliente_service.py
│   │   ├── membresia_service.py
│   │   └── pago_service.py
│   └── api/
│       ├── router.py
│       └── v1/
│           ├── cliente.py
│           ├── membresia.py
│           └── pago.py
└── requirements.txt
```

Separación clara: rutas → servicios → repositorios → modelos. Sin spaghetti.

---

## Configuración de Base de Datos

### database.py

Responsabilidades:

* Crear el engine
* Manejar sesiones
* Centralizar la conexión

Conceptos clave:

* Pool de conexiones
* Session por request
* Cierre automático

---

## Modelos ORM

Se utilizan **exactamente los campos definidos en la Fase 01**.

Reglas:

* Sin campos calculados
* Sin lógica de negocio
* Solo definición de tablas y relaciones

---

## Schemas (Pydantic)

Por cada entidad:

* `Create`
* `Update`
* `Response`

Ejemplo conceptual:

* ClienteCreate
* ClienteUpdate
* ClienteResponse

Beneficio: control total de lo que entra y sale de la API.

---

## Repositorios

Responsabilidad única:

* Acceso a datos

Incluyen:

* create
* get_by_id
* get_all
* update
* delete

Sin validaciones de negocio. Eso va en servicios.

---

## Servicios

Aquí vive el cerebro del sistema.

Ejemplos de reglas:

* No permitir dos clientes con la misma cédula
* Validar existencia de cliente y membresía antes de registrar un pago
* Preparar datos antes de persistir

Los servicios orquestan repositorios y aplican lógica.

---

## Rutas (API)

Prefijo base:

```
/api/v1
```

Endpoints principales:

### Clientes

* POST /clientes
* GET /clientes
* GET /clientes/{id}
* PUT /clientes/{id}
* DELETE /clientes/{id}

### Membresías

* POST /membresias
* GET /membresias
* PUT /membresias/{id}

### Pagos

* POST /pagos
* GET /pagos
* GET /pagos/cliente/{id_cliente}

---

## Manejo de Errores

* 404 → recurso no encontrado
* 400 → validaciones de negocio
* 500 → errores inesperados

FastAPI + HTTPException. Simple y efectivo.

---

## Estado al Finalizar la Fase

Al terminar esta fase tendrás:

* API REST funcional
* CRUD completo
* Arquitectura limpia y escalable

Backend listo para que el frontend se conecte sin llorar.

---

## Siguiente Fase

**Fase 03 – Frontend (React)**

Aquí pasamos de números y endpoints… a algo que el admin realmente pueda usar.
