import { useEffect, useState } from "react";

import { createCliente, fetchClientes } from "../services/clientes";

export function useClientes() {
  const [clientes, setClientes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadClientes = async () => {
    try {
      setLoading(true);
      setError("");
      const data = await fetchClientes();
      setClientes(data);
    } catch (err) {
      setError(err.response?.data?.detail || "No se pudieron cargar los clientes.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadClientes();
  }, []);

  const saveCliente = async (payload) => {
    const created = await createCliente(payload);
    await loadClientes();
    return created;
  };

  return {
    clientes,
    loading,
    error,
    loadClientes,
    saveCliente,
  };
}
