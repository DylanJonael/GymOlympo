export default function MembershipList({ membresias, loading }) {
  return (
    <section className="panel">
      <div className="panel-heading">
        <h2>Membresias</h2>
        <p>Catalogo actual de planes disponibles para vender.</p>
      </div>
      <div className="cards-grid">
        {loading ? <p>Cargando membresias...</p> : null}
        {!loading && membresias.length === 0 ? <p>No hay membresias registradas.</p> : null}
        {membresias.map((membresia) => (
          <article key={membresia.ID_Membresia} className="membership-card">
            <h3>{membresia.Tipo}</h3>
            <p className="price">${Number(membresia.Precio).toFixed(2)}</p>
            <p>{membresia.Duracion_Dias} dias</p>
          </article>
        ))}
      </div>
    </section>
  );
}
