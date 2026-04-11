function formatDateTime(value) {
  if (!value) {
    return "Sin fecha";
  }
  return new Date(value).toLocaleString("es-EC");
}

export default function PaymentHistory({ pagos, loading }) {
  return (
    <section className="panel">
      <div className="panel-heading">
        <h2>Pagos recientes</h2>
        <p>Historial visible para darle trazabilidad al cobro.</p>
      </div>
      <div className="table-wrap">
        <table>
          <thead>
            <tr>
              <th>ID Pago</th>
              <th>ID Cliente</th>
              <th>ID Membresia</th>
              <th>Fecha pago</th>
            </tr>
          </thead>
          <tbody>
            {loading ? (
              <tr>
                <td colSpan="4">Cargando pagos...</td>
              </tr>
            ) : pagos.length === 0 ? (
              <tr>
                <td colSpan="4">Aun no hay pagos registrados.</td>
              </tr>
            ) : (
              pagos.map((pago) => (
                <tr key={pago.ID_Pago}>
                  <td>{pago.ID_Pago}</td>
                  <td>{pago.ID_Cliente}</td>
                  <td>{pago.ID_Membresia}</td>
                  <td>{formatDateTime(pago.Fecha_Pago)}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </section>
  );
}
