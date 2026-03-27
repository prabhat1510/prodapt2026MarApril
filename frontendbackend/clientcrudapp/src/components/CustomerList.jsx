import { useState, useEffect } from "react";
import { getCustomers } from "../services/services";

const CustomerList = () => {
    const [customers, setCustomers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchCustomers = async () => {
            try {
                const data = await getCustomers();
                setCustomers(data);
            } catch (error) {
                setError(error);
            } finally {
                setLoading(false);
            }
        };
        fetchCustomers();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }

    return (
        <div>
            <h1>Customer List</h1>
            <ul>
                {customers.map((customer) => (
                    <li key={customer.customer_id}>{customer.name}</li>
                ))}
            </ul>
        </div>
    );
}

export default CustomerList;