import axios from 'axios';

// Use proxy in development, full URL in production
const API_BASE_URL = import.meta.env.PROD 
  ? 'http://localhost:8000/api' 
  : '/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

// Request interceptor for debugging
api.interceptors.request.use(
  (config) => {
    console.log('API Request:', config.method?.toUpperCase(), config.url);
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    console.error('API Error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

export const agentAPI = {
  getAll: () => api.get('/agents/'),
  getById: (id) => api.get(`/agents/${id}/`),
  create: (data) => api.post('/agents/', data),
  update: (id, data) => api.put(`/agents/${id}/`, data),
  delete: (id) => api.delete(`/agents/${id}/`),
};

export const departmentAPI = {
  getAll: () => api.get('/departments/'),
  getById: (id) => api.get(`/departments/${id}/`),
  create: (data) => api.post('/departments/', data),
  update: (id, data) => api.put(`/departments/${id}/`, data),
  delete: (id) => api.delete(`/departments/${id}/`),
};

export const departmentAgentAPI = {
  getAll: () => api.get('/department-agents/'),
  getById: (id) => api.get(`/department-agents/${id}/`),
  create: (data) => api.post('/department-agents/', data),
  update: (id, data) => api.put(`/department-agents/${id}/`, data),
  delete: (id) => api.delete(`/department-agents/${id}/`),
};

export default api;