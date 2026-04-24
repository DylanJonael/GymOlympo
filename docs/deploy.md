# Despliegue De GymOlympo

## 1. Objetivo Del Documento

Esta guia explica como desplegar **GymOlympo** en dos escenarios:

- **Desarrollo local**: para programar, probar cambios y depurar.
- **Instalacion operativa en la PC del gimnasio**: para dejar el sistema funcionando en un entorno local real.

La documentacion esta pensada para **Windows + PowerShell**, porque el proyecto actual usa:

- FastAPI en backend
- React + Vite en frontend
- SQL Server como base de datos existente
- variables locales en `.env`

## 2. Arquitectura Actual Del Despliegue

La aplicacion esta separada en dos partes:

- **Backend**: API REST con FastAPI, expuesta por defecto en `http://localhost:8000`
- **Frontend**: aplicacion React construida con Vite

Relaciones actuales del sistema:

- El frontend consume la API usando `VITE_API_BASE_URL`
- La base de datos real es **SQL Server**, ya existente
- La app esta pensada para uso **local del gimnasio**
- No es un despliegue cloud ni un SaaS publico en esta etapa

Puntos de entrada actuales:

- Backend: `backend.app.main:app`
- Frontend: `frontend/package.json`
- Variables frontend: `frontend/.env.example`

## 3. Prerrequisitos

Antes de desplegar, verifica lo siguiente:

- Windows con acceso a PowerShell
- Python `3.13` o una version compatible validada por el proyecto
- Node.js y npm instalados
- SQL Server accesible desde la maquina donde correra el sistema
- Un driver ODBC compatible con SQL Server instalado
- Archivo `.env` en la raiz con `IP_SERVIDOR` y `SA_PASSW`

Drivers ODBC compatibles que el backend intenta usar:

- `ODBC Driver 18 for SQL Server`
- `ODBC Driver 17 for SQL Server`
- `SQL Server Native Client 11.0`
- `SQL Server`

## 4. Variables De Entorno Necesarias

### Backend

El backend usa el archivo `.env` en la raiz del proyecto.

Ejemplo actual:

```env
IP_SERVIDOR="192.168.100.120"
SA_PASSW="tu_password_sql_server"
```

Variables usadas:

- `IP_SERVIDOR`: host o IP del SQL Server
- `SA_PASSW`: contrasena del usuario `sa`

Comportamiento si faltan:

- Si falta `IP_SERVIDOR`, el backend falla con: `Falta la variable de entorno IP_SERVIDOR.`
- Si falta `SA_PASSW`, el backend falla con: `Falta la variable de entorno SA_PASSW.`

### Frontend

El frontend debe tener un archivo `.env` dentro de `frontend/`, basado en `frontend/.env.example`.

Contenido esperado:

```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
```

Si el backend corre en otra IP o puerto, este valor debe cambiar.

## 5. Despliegue Para Desarrollo Local

### 5.1 Instalar dependencias del backend

Desde la raiz del proyecto:

```powershell
python -m pip install -r backend\requirements.txt
```

### 5.2 Ejecutar el backend

Desde la raiz del proyecto:

```powershell
uvicorn backend.app.main:app --reload
```

El backend quedara disponible en:

```text
http://localhost:8000
```

Endpoint de verificacion:

```text
http://localhost:8000/health
```

### 5.3 Configurar variables del frontend

Si no existe `frontend\.env`, crealo con este contenido:

```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
```

### 5.4 Instalar dependencias del frontend

```powershell
Set-Location frontend
npm install
```

### 5.5 Ejecutar el frontend

```powershell
npm run dev
```

Con la configuracion actual de Vite, el frontend corre por defecto en:

```text
http://localhost:5173
```

### 5.6 Verificar

- Abrir `http://localhost:5173`
- Abrir `http://localhost:8000/health`
- Confirmar que la UI carga sin error de conexion

## 6. Despliegue Para Cliente Local En Windows

Este flujo esta pensado para una **produccion local** en la PC del gimnasio.

## 6.1 Preparar la carpeta del proyecto

Copiar el proyecto a una ruta estable, por ejemplo:

```powershell
C:\GymOlympo
```

Evita instalarlo en carpetas temporales, Escritorio o descargas.

## 6.2 Configurar el archivo `.env` del backend

En la raiz del proyecto, crear o ajustar:

```env
IP_SERVIDOR="IP_O_NOMBRE_DEL_SQL_SERVER"
SA_PASSW="PASSWORD_REAL"
```

## 6.3 Configurar el archivo `.env` del frontend

Dentro de `frontend\`, crear:

```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
```

Si el backend se va a consumir desde otra maquina de la red local, usar la IP real del equipo que corre el backend, por ejemplo:

```env
VITE_API_BASE_URL=http://192.168.1.50:8000/api/v1
```

## 6.4 Instalar dependencias una sola vez

### Backend

Desde la raiz:

```powershell
python -m pip install -r backend\requirements.txt
```

### Frontend

```powershell
Set-Location frontend
npm install
Set-Location ..
```

## 6.5 Construir el frontend

Desde `frontend\`:

```powershell
Set-Location frontend
npm run build
```

Esto genera la carpeta:

```text
frontend\dist
```

## 6.6 Ejecutar el backend de forma fija

Desde la raiz del proyecto:

```powershell
uvicorn backend.app.main:app --host 0.0.0.0 --port 8000
```

Notas:

- `0.0.0.0` permite conexiones desde otras maquinas de la red local si el firewall lo permite.
- `8000` es el puerto esperado por defecto.

## 6.7 Servir el frontend compilado

### Enfoque temporal recomendado para v1

Usar `vite preview` como solucion simple de instalacion local.

Desde `frontend\`:

```powershell
npm run preview -- --host 0.0.0.0 --port 5173
```

Esto sirve el frontend compilado desde:

```text
http://localhost:5173
```

### Importante sobre CORS

El backend actual permite por defecto estos origenes:

- `http://localhost:5173`
- `http://127.0.0.1:5173`

Por eso, para evitar errores de CORS en esta version, el frontend desplegado debe mantenerse en el **puerto 5173** salvo que tambien se actualice la lista `cors_origins` del backend.

### Mejora futura recomendada

Una mejora posterior seria servir el build del frontend directamente desde FastAPI para simplificar el despliegue y eliminar dependencias de puertos separados.

## 6.8 Puertos usados

- Backend FastAPI: `8000`
- Frontend Vite dev o preview: `5173`

Si el sistema se usara desde otras maquinas de la red local, verifica que Windows Firewall permita trafico de entrada a esos puertos.

Ejemplo de validacion basica:

```powershell
netstat -ano | findstr :8000
netstat -ano | findstr :5173
```

## 7. Verificacion Post-Despliegue

Despues de desplegar, revisar esta lista:

### Backend

- `http://localhost:8000/health` responde:

```json
{"status":"ok"}
```

### Frontend

- La UI carga sin pagina en blanco
- No aparecen errores de red en la consola del navegador

### Flujo funcional

- Se puede listar clientes
- Se puede registrar un cliente
- Se puede registrar una membresia
- Se puede registrar un pago
- El estado de membresia cambia despues del pago

## 8. Problemas Comunes Y Solucion Rapida

### No hay driver ODBC para SQL Server

Sintoma:

- el backend falla al conectarse a SQL Server

Accion:

- instalar `ODBC Driver 17 for SQL Server` o `ODBC Driver 18 for SQL Server`

### Error de conexion a SQL Server

Sintoma:

- la API no responde correctamente al consultar datos

Revisar:

- IP o nombre del servidor en `IP_SERVIDOR`
- password en `SA_PASSW`
- SQL Server encendido
- acceso de red habilitado
- usuario `sa` habilitado y con permisos

### Faltan variables `.env`

Sintoma:

- el backend falla al arrancar con errores sobre `IP_SERVIDOR` o `SA_PASSW`

Accion:

- revisar que el archivo `.env` exista en la raiz del proyecto

### El frontend no conecta con la API

Sintoma:

- la interfaz carga, pero no trae clientes, pagos o membresias

Revisar:

- `frontend\.env`
- valor correcto de `VITE_API_BASE_URL`
- backend corriendo en `8000`
- navegador con acceso a la API

### Error de CORS

Sintoma:

- la API responde en red, pero el navegador bloquea las solicitudes

Revisar:

- si el frontend esta corriendo fuera de `5173`
- si el backend necesita incluir nuevos origenes en `cors_origins`

### Puerto 8000 ocupado

Sintoma:

- `uvicorn` no puede iniciar

Accion:

- usar otro puerto o cerrar el proceso que ocupa `8000`

### Puerto 5173 ocupado

Sintoma:

- Vite no puede levantar el frontend en el puerto esperado

Accion:

- cerrar el proceso que usa `5173`
- o cambiar el puerto y ajustar `cors_origins`

## 9. Recomendaciones De Operacion Y Respaldo

- Mantener una copia del proyecto en una carpeta fija y conocida
- Hacer respaldo frecuente de la base de datos SQL Server
- No editar manualmente archivos del sistema en la PC del cliente sin documentarlo
- Guardar una copia del archivo `.env` en un lugar seguro
- Probar el flujo completo despues de cada cambio relevante
- Documentar cualquier cambio de IP, puerto o servidor

## Notas Finales

Esta guia documenta un **despliegue manual, local y operativo**.

No cubre en esta etapa:

- Docker
- IIS
- Nginx
- despliegue en internet
- automatizacion como servicios de Windows

Esas mejoras pueden agregarse despues, pero para la version actual del proyecto el objetivo es un despliegue simple, reproducible y estable en entorno local.
