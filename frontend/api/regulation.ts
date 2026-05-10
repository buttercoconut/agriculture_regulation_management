import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000',
  timeout: 10000,
});

export async function getRegulations(params: any) {
  const response = await apiClient.get('/regulations/', { params });
  return response.data;
}

export async function getRegulation(id: string | number) {
  const response = await apiClient.get(`/regulations/${id}`);
  return response.data;
}

export async function sendNotification(data: any) {
  const response = await apiClient.post('/notifications/', data);
  return response.data;
}
