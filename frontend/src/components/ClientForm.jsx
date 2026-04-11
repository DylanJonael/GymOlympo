import { useState } from "react";

const initialState = {
  Nombre: "",
  WhatsApp: "",
  Cedula: "",
};

export default function ClientForm({ onSubmit, submitting }) {
  const [form, setForm] = useState(initialState);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setForm((current) => ({ ...current, [name]: value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    await onSubmit({
      ...form,
      WhatsApp: form.WhatsApp || null,
      Cedula: form.Cedula || null,
    });
    setForm(initialState);
  };

  return (
    <form className="panel form-grid" onSubmit={handleSubmit}>
      <div className="panel-heading">
        <h2>Nuevo cliente</h2>
        <p>Registra clientes rapido y sin depender de papel.</p>
      </div>
      <label>
        Nombre
        <input
          name="Nombre"
          value={form.Nombre}
          onChange={handleChange}
          placeholder="Nombre completo"
          required
        />
      </label>
      <label>
        WhatsApp
        <input
          name="WhatsApp"
          value={form.WhatsApp}
          onChange={handleChange}
          placeholder="0999999999"
        />
      </label>
      <label>
        Cedula
        <input
          name="Cedula"
          value={form.Cedula}
          onChange={handleChange}
          placeholder="Cedula del cliente"
        />
      </label>
      <button type="submit" className="primary-button" disabled={submitting}>
        {submitting ? "Guardando..." : "Crear cliente"}
      </button>
    </form>
  );
}
