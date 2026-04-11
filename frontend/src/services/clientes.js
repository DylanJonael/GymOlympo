import apiClient from "../api/client";

export async function fetchClientes() {
  const { data } = await apiClient.get("/clientes");
  return data;
}

export async function createCliente(payload) {
  const { data } = await apiClient.post("/clientes", payload);
  return data;
}

export async function updateCliente(id, payload) {
  const { data } = await apiClient.put(`/clientes/${id}`, payload);
  return data;
}

export async function fetchEstadoMembresia(id) {
  const { data } = await apiClient.get(`/clientes/${id}/estado-membresia`);
  return data;
}
