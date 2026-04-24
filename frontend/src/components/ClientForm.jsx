import { useState } from "react";

const initialState = {
  Nombre: "",
  WhatsApp: "",
  Cedula: "",
};

export default function ClientForm({ onSubmit, submitting }) {
  const [form, setForm] = useState(initialState);
  const [errors, setErrors] = useState({});

  const handleChange = (event) => {
    const { name, value } = event.target;
    let nextValue = value;

    if (name === "WhatsApp" || name === "Cedula") {
      nextValue = value.replace(/\D/g, "").slice(0, 10);
    }

    if (name === "Nombre") {
      nextValue = value.slice(0, 50);
    }

    setForm((current) => ({ ...current, [name]: nextValue }));
    setErrors((current) => ({ ...current, [name]: "" }));
  };

  const validateForm = () => {
    const nextErrors = {};

    if (!form.Nombre.trim()) {
      nextErrors.Nombre = "El nombre es obligatorio.";
    } else if (form.Nombre.length > 50) {
      nextErrors.Nombre = "El nombre no puede superar los 50 caracteres.";
    }

    if (form.WhatsApp && !/^\d{1,10}$/.test(form.WhatsApp)) {
      nextErrors.WhatsApp = "WhatsApp debe tener solo numeros y maximo 10 digitos.";
    }

    if (form.Cedula && !/^\d{1,10}$/.test(form.Cedula)) {
      nextErrors.Cedula = "La cedula debe tener solo numeros y maximo 10 digitos.";
    }

    setErrors(nextErrors);
    return Object.keys(nextErrors).length === 0;
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!validateForm()) {
      return;
    }
    await onSubmit({
      ...form,
      WhatsApp: form.WhatsApp || null,
      Cedula: form.Cedula || null,
    });
    setForm(initialState);
    setErrors({});
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
          maxLength={50}
          required
        />
        {errors.Nombre ? <span className="field-error">{errors.Nombre}</span> : null}
      </label>
      <label>
        WhatsApp
        <input
          name="WhatsApp"
          value={form.WhatsApp}
          onChange={handleChange}
          placeholder="0999999999"
          maxLength={10}
          inputMode="numeric"
          pattern="[0-9]*"
        />
        {errors.WhatsApp ? <span className="field-error">{errors.WhatsApp}</span> : null}
      </label>
      <label>
        Cedula
        <input
          name="Cedula"
          value={form.Cedula}
          onChange={handleChange}
          placeholder="Cedula del cliente"
          maxLength={10}
          inputMode="numeric"
          pattern="[0-9]*"
        />
        {errors.Cedula ? <span className="field-error">{errors.Cedula}</span> : null}
      </label>
      <button type="submit" className="primary-button" disabled={submitting}>
        {submitting ? "Guardando..." : "Crear cliente"}
      </button>
    </form>
  );
}
