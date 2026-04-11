import { useEffect, useState } from "react";

import { createMembresia, fetchMembresias } from "../services/membresias";

export function useMembresias() {
  const [membresias, setMembresias] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadMembresias = async () => {
    try {
      setLoading(true);
      setError("");
      const data = await fetchMembresias();
      setMembresias(data);
    } catch (err) {
      setError(err.response?.data?.detail || "No se pudieron cargar las membresias.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadMembresias();
  }, []);

  const saveMembresia = async (payload) => {
    const created = await createMembresia(payload);
    await loadMembresias();
    return created;
  };

  return {
    membresias,
    loading,
    error,
    loadMembresias,
    saveMembresia,
  };
}
