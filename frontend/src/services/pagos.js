import apiClient from "../api/client";

export async function fetchPagos() {
  const { data } = await apiClient.get("/pagos");
  return data;
}

export async function fetchPagosByCliente(clienteId) {
  const { data } = await apiClient.get(`/pagos/cliente/${clienteId}`);
  return data;
}

export async function createPago(payload) {
  const { data } = await apiClient.post("/pagos", payload);
  return data;
}
