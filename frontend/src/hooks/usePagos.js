import { useEffect, useState } from "react";

import { createPago, fetchPagos } from "../services/pagos";

export function usePagos() {
  const [pagos, setPagos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadPagos = async () => {
    try {
      setLoading(true);
      setError("");
      const data = await fetchPagos();
      setPagos(data);
    } catch (err) {
      setError(err.response?.data?.detail || "No se pudieron cargar los pagos.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadPagos();
  }, []);

  const savePago = async (payload) => {
    const created = await createPago(payload);
    await loadPagos();
    return created;
  };

  return {
    pagos,
    loading,
    error,
    loadPagos,
    savePago,
  };
}
