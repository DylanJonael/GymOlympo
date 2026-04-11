function formatDate(value) {
  if (!value) {
    return "Sin fecha";
  }
  return new Date(value).toLocaleDateString("es-EC");
}

function getStatusClass(status) {
  switch (status) {
    case "ACTIVA":
      return "status status-active";
    case "PROXIMA_A_VENCER":
      return "status status-warning";
    case "VENCIDA":
      return "status status-expired";
    default:
      return "status status-empty";
  }
}

export default function ClientsTable({ clientes, loading }) {
  return (
    <section className="panel">
      <div className="panel-heading">
        <h2>Clientes</h2>
        <p>Vista rapida del estado actual de cada cliente.</p>
      </div>
      <div className="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Cliente</th>
              <th>Cedula</th>
              <th>WhatsApp</th>
              <th>Estado</th>
              <th>Vence</th>
              <th>Dias restantes</th>
            </tr>
          </thead>
          <tbody>
            {loading ? (
              <tr>
                <td colSpan="6">Cargando clientes...</td>
              </tr>
            ) : clientes.length === 0 ? (
              <tr>
                <td colSpan="6">Aun no hay clientes registrados.</td>
              </tr>
            ) : (
              clientes.map((cliente) => (
                <tr key={cliente.ID_Cliente}>
                  <td>{cliente.Nombre}</td>
                  <td>{cliente.Cedula || "Sin cedula"}</td>
                  <td>{cliente.WhatsApp || "Sin WhatsApp"}</td>
                  <td>
                    <span className={getStatusClass(cliente.estado_membresia)}>
                      {cliente.estado_membresia}
                    </span>
                  </td>
                  <td>{formatDate(cliente.fecha_vencimiento)}</td>
                  <td>
                    {typeof cliente.dias_restantes === "number"
                      ? cliente.dias_restantes
                      : "-"}
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </section>
  );
}
