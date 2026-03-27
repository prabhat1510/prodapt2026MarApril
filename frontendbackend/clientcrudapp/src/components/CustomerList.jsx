import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { getCustomers, deleteCustomer } from "../services/services";

const CustomerList = () => {
    const [customers, setCustomers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const navigate = useNavigate();

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
    }, []);

    if (loading) {
        return (
            <div className="text-center py-5">
                <div className="spinner-border text-primary" role="status" />
            </div>
        );
    }

    if (error) {
        return <div className="alert alert-danger">Error: {error.message}</div>;
    }

    const handleShow   = (id) => navigate(`/customers/${id}`);
    const handleEdit   = (id) => navigate(`/customers/${id}/edit`);
    const handleDelete = async (id) => {
        if (!window.confirm(`Delete customer #${id}?`)) return;
        try {
            await deleteCustomer(id);
            await fetchCustomers();
        } catch (err) {
            console.error("Error deleting customer:", err);
            alert("Failed to delete customer. Please try again.");
        }
    };

    return (
        <div>
            <div className="d-flex justify-content-between align-items-center mb-4">
                <h2 className="fw-bold text-primary mb-0">Customer List</h2>
                <span className="badge bg-primary fs-6">{customers.length} customers</span>
            </div>

            {customers.length === 0 ? (
                <div className="alert alert-info">
                    No customers found. <a href="/customers/new">Add one!</a>
                </div>
            ) : (
                <div className="table-responsive shadow-sm rounded">
                    <table className="table table-hover table-bordered table-sm mb-0 bg-white">
                        <thead className="table-primary">
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
                                <tr key={customer.customer_id}>
                                    <td>{customer.customer_id}</td>
                                    <td>{customer.name}</td>
                                    <td>{customer.email}</td>
                                    <td>{customer.phone}</td>
                                    <td>
                                        <div className="d-flex gap-2">
                                            <button
                                                className="btn btn-primary btn-sm"
                                                onClick={() => handleShow(customer.customer_id)}
                                            >Show</button>
                                            <button
                                                className="btn btn-warning btn-sm"
                                                onClick={() => handleEdit(customer.customer_id)}
                                            >Edit</button>
                                            <button
                                                className="btn btn-danger btn-sm"
                                                onClick={() => handleDelete(customer.customer_id)}
                                            >Delete</button>
                                        </div>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
};

export default CustomerList;