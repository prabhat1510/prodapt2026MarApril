import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { getCustomer } from "../services/services";

const CustomerDetails = () => {
    const { id } = useParams();
    const navigate = useNavigate();

    const [customer, setCustomer] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchCustomer = async () => {
            try {
                const data = await getCustomer(id);
                setCustomer(data);
            } catch (err) {
                setError("Failed to load customer details.");
                console.error(err);
            } finally {
                setLoading(false);
            }
        };
        fetchCustomer();
    }, [id]);

    if (loading) {
        return (
            <div className="text-center py-5">
                <div className="spinner-border text-primary" role="status" />
            </div>
        );
    }

    if (error) return <div className="alert alert-danger">{error}</div>;
    if (!customer) return <div className="alert alert-info">Customer not found.</div>;

    return (
        <div className="row justify-content-center">
            <div className="col-lg-8">
                <div className="card shadow-sm border-0">
                    <div className="card-header bg-primary text-white d-flex align-items-center justify-content-between">
                        <h3 className="mb-0">Customer Profile</h3>
                        <span className="badge bg-light text-primary">ID: {customer.customer_id}</span>
                    </div>
                    <div className="card-body">
                        <div className="row g-3">
                            <div className="col-md-6 border-end">
                                <h5 className="text-muted small text-uppercase fw-bold mb-3">Basic Information</h5>
                                <div className="mb-3">
                                    <label className="form-label text-secondary mb-1">Full Name</label>
                                    <p className="h5">{customer.name}</p>
                                </div>
                                <div className="mb-3">
                                    <label className="form-label text-secondary mb-1">Customer ID</label>
                                    <p className="fw-medium">{customer.customer_id}</p>
                                </div>
                            </div>
                            <div className="col-md-6">
                                <h5 className="text-muted small text-uppercase fw-bold mb-3">Contact Details</h5>
                                <div className="mb-3">
                                    <label className="form-label text-secondary mb-1">Email Address</label>
                                    <p className="h5 text-break">{customer.email}</p>
                                </div>
                                <div className="mb-3">
                                    <label className="form-label text-secondary mb-1">Phone Number</label>
                                    <p className="h5">{customer.phone}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="card-footer bg-light d-flex gap-2 justify-content-end">
                        <button
                            className="btn btn-warning btn-sm"
                            onClick={() => navigate(`/customers/${customer.customer_id}/edit`)}
                        >Edit</button>
                        <button
                            className="btn btn-outline-secondary btn-sm"
                            onClick={() => navigate("/customers")}
                        >← Back to List</button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default CustomerDetails;