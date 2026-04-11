import { useState } from "react";

const initialState = {
  Tipo: "",
  Precio: "",
  Duracion_Dias: "",
};

export default function MembershipForm({ onSubmit, submitting }) {
  const [form, setForm] = useState(initialState);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setForm((current) => ({ ...current, [name]: value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    await onSubmit({
      ...form,
      Precio: Number(form.Precio),
      Duracion_Dias: Number(form.Duracion_Dias),
    });
    setForm(initialState);
  };

  return (
    <form className="panel form-grid" onSubmit={handleSubmit}>
      <div className="panel-heading">
        <h2>Nueva membresia</h2>
        <p>Define planes simples y claros para el equipo administrativo.</p>
      </div>
      <label>
        Tipo
        <input
          name="Tipo"
          value={form.Tipo}
          onChange={handleChange}
          placeholder="Mensual"
          required
        />
      </label>
      <label>
        Precio
        <input
          name="Precio"
          type="number"
          min="0.01"
          step="0.01"
          value={form.Precio}
          onChange={handleChange}
          placeholder="25.00"
          required
        />
      </label>
      <label>
        Duracion (dias)
        <input
          name="Duracion_Dias"
          type="number"
          min="1"
          value={form.Duracion_Dias}
          onChange={handleChange}
          placeholder="30"
          required
        />
      </label>
      <button type="submit" className="secondary-button" disabled={submitting}>
        {submitting ? "Guardando..." : "Crear membresia"}
      </button>
    </form>
  );
}
