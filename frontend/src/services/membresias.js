import apiClient from "../api/client";

export async function fetchMembresias() {
  const { data } = await apiClient.get("/membresias");
  return data;
}

export async function createMembresia(payload) {
  const { data } = await apiClient.post("/membresias", payload);
  return data;
}
