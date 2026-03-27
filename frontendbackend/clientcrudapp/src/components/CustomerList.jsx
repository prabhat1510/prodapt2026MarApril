import { useState, useEffect } from "react";
import { getCustomers, deleteCustomer } from "../services/services";

const CustomerList = ({ customerSelected, onEditCustomer, refreshKey }) => {
    const [customers, setCustomers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const fetchCustomers = async () => {
        try {
            setLoading(true);
            const data = await getCustomers();
            setCustomers(data);
        } catch (err) {
            setError(err);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchCustomers();
    }, [refreshKey]);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }

    const handleCustomerClick = (customer) => {
        console.log("Show customer:", customer);
        customerSelected(customer);
    };

    const handleEdit = (customer) => {
        console.log("Edit customer:", customer);
        if (onEditCustomer) onEditCustomer(customer);
        // Scroll to top so the form is visible
        window.scrollTo({ top: 0, behavior: "smooth" });
    };

    const handleDelete = async (id) => {
        if (!window.confirm(`Are you sure you want to delete customer #${id}?`)) return;
        try {
            await deleteCustomer(id);
            console.log("Deleted customer:", id);
            await fetchCustomers(); // Refresh the list
        } catch (err) {
            console.error("Error deleting customer:", err);
            alert("Failed to delete customer. Please try again.");
        }
    };

    return (
        <div className="container">
            <h1>Customer List</h1>
            <table className="table table-hover table-bordered table-sm">
                <thead className="thead-light">
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Phone</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {customers.map((customer) => (
                        <tr
                            onClick={() => handleCustomerClick && handleCustomerClick(customer)}
                            key={customer.customer_id}
                        >
                            <td>{customer.customer_id}</td>
                            <td>{customer.name}</td>
                            <td>{customer.email}</td>
                            <td>{customer.phone}</td>
                            <td className="d-flex gap-2">
                                <button
                                    className="btn btn-primary btn-sm"
                                    onClick={(e) => { e.stopPropagation(); handleCustomerClick && handleCustomerClick(customer); }}
                                >Show</button>
                                <button
                                    className="btn btn-warning btn-sm"
                                    onClick={(e) => { e.stopPropagation(); handleEdit(customer); }}
                                >Edit</button>
                                <button
                                    className="btn btn-danger btn-sm"
                                    onClick={(e) => { e.stopPropagation(); handleDelete(customer.customer_id); }}
                                >Delete</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default CustomerList;