import { createCustomer, updateCustomer } from "../services/services";
import { useState, useEffect } from "react";

const CustomerForm = ({ customer, onSuccess }) => {
    const isEditMode = !!customer;

    const [formData, setFormData] = useState({
        name: "",
        email: "",
        phone: ""
    });

    // Populate form when editing customer changes
    useEffect(() => {
        if (customer) {
            setFormData({
                name: customer.name || "",
                email: customer.email || "",
                phone: customer.phone || ""
            });
        } else {
            setFormData({ name: "", email: "", phone: "" });
        }
    }, [customer]);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            if (isEditMode) {
                await updateCustomer(customer.customer_id, formData);
                console.log("Customer updated:", formData);
            } else {
                await createCustomer(formData);
                console.log("Customer created:", formData);
            }
            setFormData({ name: "", email: "", phone: "" });
            if (onSuccess) onSuccess();
        } catch (error) {
            console.error("Error submitting form:", error);
        }
    };

    const handleCancel = () => {
        setFormData({ name: "", email: "", phone: "" });
        if (onSuccess) onSuccess();
    };

    return (
        <div>
            <h2>{isEditMode ? "Edit Customer" : "Add Customer"}</h2>
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="name" className="form-label">Name</label>
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
                    <label htmlFor="email" className="form-label">Email</label>
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
                    <label htmlFor="phone" className="form-label">Phone</label>
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
                    {isEditMode && (
                        <button type="button" className="btn btn-secondary" onClick={handleCancel}>
                            Cancel
                        </button>
                    )}
                </div>
            </form>
        </div>
    );
};

export default CustomerForm;