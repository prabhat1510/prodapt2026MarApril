import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { createCustomer, updateCustomer, getCustomer } from "../services/services";

const CustomerForm = () => {
    const { id } = useParams();           // defined only on /customers/:id/edit
    const isEditMode = !!id;
    const navigate = useNavigate();

    const [formData, setFormData] = useState({ name: "", email: "", phone: "" });
    const [loading, setLoading] = useState(isEditMode);
    const [error, setError] = useState(null);

    // In edit mode, fetch the existing customer to pre-fill the form
    useEffect(() => {
        if (!isEditMode) return;
        const fetchCustomer = async () => {
            try {
                const data = await getCustomer(id);
                setFormData({
                    name: data.name || "",
                    email: data.email || "",
                    phone: data.phone || ""
                });
            } catch (err) {
                setError("Failed to load customer data.");
                console.error(err);
            } finally {
                setLoading(false);
            }
        };
        fetchCustomer();
    }, [id, isEditMode]);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            if (isEditMode) {
                await updateCustomer(id, formData);
            } else {
                await createCustomer(formData);
            }
            navigate("/customers");   // go back to list on success
        } catch (err) {
            console.error("Error submitting form:", err);
            setError("Failed to save customer. Please try again.");
        }
    };

    if (loading) {
        return (
            <div className="text-center py-5">
                <div className="spinner-border text-primary" role="status" />
            </div>
        );
    }

    return (
        <div className="row justify-content-center">
            <div className="col-lg-6">
                <div className="card shadow-sm border-0">
                    <div className="card-header bg-primary text-white">
                        <h4 className="mb-0">{isEditMode ? "Edit Customer" : "Add New Customer"}</h4>
                    </div>
                    <div className="card-body p-4">
                        {error && <div className="alert alert-danger">{error}</div>}
                        <form onSubmit={handleSubmit}>
                            <div className="mb-3">
                                <label htmlFor="name" className="form-label fw-semibold">Name</label>
                                <input
                                    type="text"
                                    className="form-control"
                                    id="name"
                                    name="name"
                                    value={formData.name}
                                    onChange={handleChange}
                                    required
                                />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="email" className="form-label fw-semibold">Email</label>
                                <input
                                    type="email"
                                    className="form-control"
                                    id="email"
                                    name="email"
                                    value={formData.email}
                                    onChange={handleChange}
                                    required
                                />
                            </div>
                            <div className="mb-3">
                                <label htmlFor="phone" className="form-label fw-semibold">Phone</label>
                                <input
                                    type="text"
                                    className="form-control"
                                    id="phone"
                                    name="phone"
                                    value={formData.phone}
                                    onChange={handleChange}
                                    required
                                />
                            </div>
                            <div className="d-flex gap-2">
                                <button type="submit" className="btn btn-primary">
                                    {isEditMode ? "Update Customer" : "Add Customer"}
                                </button>
                                <button
                                    type="button"
                                    className="btn btn-secondary"
                                    onClick={() => navigate("/customers")}
                                >Cancel</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default CustomerForm;