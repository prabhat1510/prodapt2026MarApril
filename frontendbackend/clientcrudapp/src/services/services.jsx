import axios from "axios";


const API_URL = "http://localhost:8000";

export const createCustomer = async (customer) => {
    try {
        const response = await axios.post(`${API_URL}/customers`, customer);
        return response.data;
    } catch (error) {
        console.error("Error creating customer:", error);
        throw error;
    }
}

export const getCustomers = async () => {
    try {
        console.log("Inside getCustomers");
        console.log(`${API_URL}/customers`)
        const response = await axios.get(`${API_URL}/customers`);
        console.log(response.data)
        return response.data;
    } catch (error) {
        console.error("Error fetching customers:", error);
        throw error;
    }
}

export const getCustomer = async (id) => {
    try {
        const response = await axios.get(`${API_URL}/customers/${id}`);
        return response.data;
    } catch (error) {
        console.error("Error fetching customer:", error);
        throw error;
    }
}

export const deleteCustomer = async (id) => {
    try {
        const response = await axios.delete(`${API_URL}/customers/${id}`);
        return response.data;
    } catch (error) {
        console.error("Error deleting customer:", error);
        throw error;
    }
}

export const updateCustomer = async (id, customer) => {
    try {
        const response = await axios.put(`${API_URL}/customers/${id}`, customer);
        return response.data;
    } catch (error) {
        console.error("Error updating customer:", error);
        throw error;
    }
}