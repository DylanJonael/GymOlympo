import pyodbc

server = "DESKTOP-IALE84M\\SQLEXPRESS"
database = "GimnasioDB"

print("Controladores ODBC instalados:")
for driver in pyodbc.drivers():
    print(f" - {driver}")

candidate_drivers = [
    "ODBC Driver 18 for SQL Server",
    "ODBC Driver 17 for SQL Server",
    "SQL Server Native Client 11.0",
    "SQL Server",
]

connected = False
last_error = None

for driver in candidate_drivers:
    try:
        conn_str = (
            f"Driver={{{driver}}};"
            f"Server={server};"
            f"Database={database};"
            "Trusted_Connection=yes;"
        )
        print(f"Probando conexión con driver: {driver}")
        conexion = pyodbc.connect(conn_str, timeout=5)
        print("¡Conexión exitosa con el gimnasio!")
        connected = True
        break
    except Exception as e:
        print(f"No se pudo conectar con el driver {driver}: {e}")
        last_error = e

if not connected:
    print("\nNo se pudo conectar con ningún driver probado.")
    print("Revisa estas opciones:")
    print(" - Que SQL Server esté en ejecución.")
    print(" - Que el nombre del servidor/instancia sea correcto.")
    print(" - Que la base de datos 'GimnasioDB' exista.")
    print(" - Que el usuario tenga permisos o uses una conexión de Windows válida.")
    if last_error:
        print(f"Último error detectado: {last_error}")
else:
    cursor = conexion.cursor()
    cursor.execute("SELECT ID_Cliente, Nombre, Cedula FROM Clientes")
    for fila in cursor:
        print(f"ID: {fila.ID_Cliente} | Nombre: {fila.Nombre} | Cédula: {fila.Cedula}")