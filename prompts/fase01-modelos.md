Perfecto. Entramos en **backend serio** ahora.
Abajo tienes el **contenido FINAL, preciso y sin ambigüedades** del archivo:

📄 **`prompts/fase01-modelos.md`**

Este `.md` está diseñado para:

* Usarse **como archivo de contexto** en GitHub Copilot Chat
* Mapear **exactamente tus tablas reales de SQL Server**
* Evitar que Copilot invente columnas, tipos o relaciones
* Omitir **explícitamente** los campos derivados (`Estado`, `Fecha_Vencimiento`)

Cópialo **tal cual**, sin editar.

---

# 📄 `fase01-modelos.md`

````md
# FASE 01 – Modelos SQLAlchemy (Mapeo de Tablas Existentes)

## Rol
Actúa como un **backend developer senior especializado en FastAPI + SQLAlchemy**, con experiencia en **SQL Server** y sistemas en producción.

## Contexto General
El proyecto es un sistema **local** de gestión de membresías para un gimnasio.

Stack:
- Backend: FastAPI + Python
- ORM: SQLAlchemy
- Base de datos: SQL Server (SSMS)

⚠️ IMPORTANTE:
- Las tablas **YA EXISTEN** en la base de datos.
- **NO debes modificar la base de datos**.
- **NO debes crear migraciones**.
- **NO debes redefinir ni tocar la conexión** (`database.py` ya existe).
- Tu tarea es **mapear**, no diseñar.

## Objetivo de esta Fase
Crear los **modelos SQLAlchemy** que representen **1:1** las tablas existentes en SQL Server.

Los modelos deben:
- Reflejar columnas reales
- Respetar tipos de datos
- Definir correctamente claves primarias y foráneas
- Definir relaciones entre entidades

## Tablas Existentes en SQL Server

### Tabla: Clientes
```sql
CREATE TABLE Clientes (
    ID_Cliente INT PRIMARY KEY IDENTITY(1,1),
    Nombre VARCHAR(100) NOT NULL,
    WhatsApp VARCHAR(20),
    Fecha_Registro DATETIME DEFAULT GETDATE(),
    Cedula VARCHAR(15) UNIQUE
);
````

### Tabla: Membresias

```sql
CREATE TABLE Membresias (
    ID_Membresia INT PRIMARY KEY IDENTITY(1,1),
    Tipo VARCHAR(50) NOT NULL,
    Precio DECIMAL(10, 2) NOT NULL,
    Duracion_Dias INT NOT NULL
);
```

### Tabla: Pagos

```sql
CREATE TABLE Pagos (
    ID_Pago INT PRIMARY KEY IDENTITY(1,1),
    ID_Cliente INT,
    ID_Membresia INT,
    Fecha_Pago DATETIME DEFAULT GETDATE(),
    Fecha_Vencimiento AS (DATEADD(day, 30, Fecha_Pago)),
    Estado AS (
        CASE 
            WHEN GETDATE() > DATEADD(day, 30, Fecha_Pago) 
            THEN 'Vencido' 
            ELSE 'Activo' 
        END
    ),
    CONSTRAINT FK_Cliente FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente),
    CONSTRAINT FK_Membresia FOREIGN KEY (ID_Membresia) REFERENCES Membresias(ID_Membresia)
);
```

## Reglas de Mapeo OBLIGATORIAS

### 1️⃣ Campos que SÍ deben mapearse

* Todas las columnas **persistidas físicamente**:

  * IDs
  * Fechas base
  * Campos de texto
  * Campos numéricos
  * Foreign Keys

### 2️⃣ Campos que NO deben mapearse

❌ **NO incluir en los modelos SQLAlchemy**:

* `Fecha_Vencimiento`
* `Estado`

Motivo:

* Son campos **derivados / computados**
* La lógica de vencimiento y estado se manejará en la capa de servicios
* No deben ser fuente de verdad en el backend

### 3️⃣ Convenciones Técnicas

* Usar nombres de clases en singular:

  * `Cliente`
  * `Membresia`
  * `Pago`
* Usar `__tablename__` exactamente como en SQL Server
* Mapear columnas con nombres exactos (`ID_Cliente`, etc.)
* Usar tipos compatibles con SQL Server (`Integer`, `String`, `DateTime`, `Numeric`)
* Definir relaciones con `relationship`

## Estructura de Archivos Esperada

Ubicación:

```
backend/app/models/
```

Archivos a crear:

* `cliente.py`
* `membresia.py`
* `pago.py`

Cada archivo debe contener **solo su modelo correspondiente**.

## Alcance Permitido

✅ Definir clases SQLAlchemy
✅ Definir columnas
✅ Definir relaciones
NO Crear lógica de negocio
NO Crear queries complejas
NO Acceder a servicios
NO Implementar endpoints

## Condiciones Estrictas

* No inventar columnas
* No renombrar campos
* No “optimizar” el esquema
* No usar los campos derivados
* No adelantar fases futuras

## Criterio de Finalización

La fase se considera completada cuando:

* Los tres modelos existen
* Los modelos reflejan fielmente las tablas reales
* No hay lógica fuera del mapeo ORM
* El código es claro, limpio y mantenible

## Instrucción Final

Limítate estrictamente a esta fase.
No implementes nada fuera del mapeo de modelos.

```
