//user service make api call to backend
import axios from 'axios';


const API_URL = 'http://localhost:8000/user';

// Helper to get auth header
const getAuthHeader = () => {
    const token = localStorage.getItem("access_token");
    return token ? { Authorization: `Bearer ${token}` } : {};
};

export const registerUser = async (user) => {
    const response = await axios.post(`${API_URL}/register`, user);
    return response.data;
}

export const loginUser = async (user) => {
    const response = await axios.post(`${API_URL}/login`, user);
    console.log(response.data);
    return response.data;
}

export const logoutUser = async (user) => {
    const response = await axios.post(`${API_URL}/logout`, {}, { headers: getAuthHeader() });
    return response.data;
}

export const refreshUser = async () => {
    const response = await axios.post(`${API_URL}/refresh`, {}, { headers: getAuthHeader() });
    return response.data;
}

export const updateUserDetails = async (user) => {
    const response = await axios.put(`${API_URL}/update/${user.id}`, user, { headers: getAuthHeader() });
    return response.data;
}

export const getUserProfile = async () => {
    const response = await axios.get(`${API_URL}/details`, { headers: getAuthHeader() });
    return response.data;
}
