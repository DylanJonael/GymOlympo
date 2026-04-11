import { useState } from "react";

const initialState = {
  ID_Cliente: "",
  ID_Membresia: "",
  Fecha_Pago: "",
};

export default function PaymentForm({
  clientes,
  membresias,
  onSubmit,
  submitting,
}) {
  const [form, setForm] = useState(initialState);

  const clienteOptions = clientes.map((cliente) => ({
    value: cliente.ID_Cliente,
    label: `${cliente.Nombre} (${cliente.estado_membresia})`,
  }));

  const membresiaOptions = membresias.map((membresia) => ({
    value: membresia.ID_Membresia,
    label: `${membresia.Tipo} - ${membresia.Duracion_Dias} dias`,
  }));

  const handleChange = (event) => {
    const { name, value } = event.target;
    setForm((current) => ({ ...current, [name]: value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    await onSubmit({
      ID_Cliente: Number(form.ID_Cliente),
      ID_Membresia: Number(form.ID_Membresia),
      Fecha_Pago: form.Fecha_Pago || null,
    });
    setForm(initialState);
  };

  return (
    <form className="panel form-grid" onSubmit={handleSubmit}>
      <div className="panel-heading">
        <h2>Registrar pago</h2>
        <p>El sistema recalculara el estado de membresia al instante.</p>
      </div>
      <label>
        Cliente
        <select
          name="ID_Cliente"
          value={form.ID_Cliente}
          onChange={handleChange}
          required
        >
          <option value="">Selecciona un cliente</option>
          {clienteOptions.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
      </label>
      <label>
        Membresia
        <select
          name="ID_Membresia"
          value={form.ID_Membresia}
          onChange={handleChange}
          required
        >
          <option value="">Selecciona una membresia</option>
          {membresiaOptions.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
      </label>
      <label>
        Fecha de pago
        <input
          name="Fecha_Pago"
          type="datetime-local"
          value={form.Fecha_Pago}
          onChange={handleChange}
        />
      </label>
      <button type="submit" className="accent-button" disabled={submitting}>
        {submitting ? "Guardando..." : "Registrar pago"}
      </button>
    </form>
  );
}
