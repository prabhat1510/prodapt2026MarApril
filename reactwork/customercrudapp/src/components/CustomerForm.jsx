import React, { useState, useEffect } from "react";
import { useNavigate, Link, useParams } from "react-router-dom";

const CustomerForm = ({ onAddCustomer, onUpdateCustomer, customers }) => {
    const navigate = useNavigate();
    const { id } = useParams();
    const [customer, setCustomer] = useState({
        firstname: "",
        lastname: "",
        email: ""
    });
    const [errors, setErrors] = useState({});

    useEffect(() => {
        if (id && customers) {
            const existingCustomer = customers.find(c => c.id === parseInt(id));
            if (existingCustomer) {
                setCustomer({
                    firstname: existingCustomer.firstname,
                    lastname: existingCustomer.lastname,
                    email: existingCustomer.email
                });
            }
        }
    }, [id, customers]);

    const handleChange = (e) => {
        setCustomer({ ...customer, [e.target.name]: e.target.value });
        // Clear error when user types
        if (errors[e.target.name]) {
            setErrors({ ...errors, [e.target.name]: "" });
        }
    }

    const validate = () => {
        let newErrors = {};
        if (!customer.firstname.trim()) newErrors.firstname = "First name is required";
        if (!customer.lastname.trim()) newErrors.lastname = "Last name is required";
        if (!customer.email.trim()) {
            newErrors.email = "Email is required";
        } else if (!/\S+@\S+\.\S+/.test(customer.email)) {
            newErrors.email = "Email is invalid";
        }
        return newErrors;
    }

    const handleSubmit = (e) => {
        e.preventDefault();

        const formErrors = validate();
        if (Object.keys(formErrors).length > 0) {
            setErrors(formErrors);
            return;
        }

        if (id) {
            // Edit mode
            onUpdateCustomer({
                id: parseInt(id),
                ...customer
            });
        } else {
            // Create mode
            const nextId = (customers && customers.length > 0)
                ? Math.max(...customers.map(c => c.id)) + 1
                : 1;

            if (onAddCustomer) {
                onAddCustomer({
                    id: nextId,
                    ...customer
                });
            }
        }

        // Redirect to customers list
        navigate("/customers");
    }

    return (
        <div className="container mt-5">
            <div className="row justify-content-center">
                <div className="col-md-6">
                    <div className="card shadow border-0 rounded-3">
                        <div className={`card-header ${id ? 'bg-primary' : 'bg-success'} text-white py-3`}>
                            <h3 className="card-title mb-0">
                                {id ? 'Update Customer' : 'Register New Customer'}
                            </h3>
                        </div>
                        <div className="card-body p-4">
                            <form onSubmit={handleSubmit}>
                                <div className="mb-3">
                                    <label className="form-label fw-bold small text-uppercase">First Name</label>
                                    <input
                                        type="text"
                                        name="firstname"
                                        className={`form-control ${errors.firstname ? 'is-invalid' : ''}`}
                                        placeholder="Enter first name"
                                        value={customer.firstname}
                                        onChange={handleChange}
                                    />
                                    {errors.firstname && <div className="invalid-feedback">{errors.firstname}</div>}
                                </div>

                                <div className="mb-3">
                                    <label className="form-label fw-bold small text-uppercase">Last Name</label>
                                    <input
                                        type="text"
                                        name="lastname"
                                        className={`form-control ${errors.lastname ? 'is-invalid' : ''}`}
                                        placeholder="Enter last name"
                                        value={customer.lastname}
                                        onChange={handleChange}
                                    />
                                    {errors.lastname && <div className="invalid-feedback">{errors.lastname}</div>}
                                </div>

                                <div className="mb-3">
                                    <label className="form-label fw-bold small text-uppercase">Email Address</label>
                                    <input
                                        type="email"
                                        name="email"
                                        className={`form-control ${errors.email ? 'is-invalid' : ''}`}
                                        placeholder="customer@example.com"
                                        value={customer.email}
                                        onChange={handleChange}
                                    />
                                    {errors.email && <div className="invalid-feedback">{errors.email}</div>}
                                </div>

                                <div className="d-grid gap-2 mt-4">
                                    <button type="submit" className={`btn ${id ? 'btn-primary' : 'btn-success'} py-2`}>
                                        <i className={`bi ${id ? 'bi-check-circle-fill' : 'bi-person-check-fill'} me-2`}></i>
                                        {id ? 'Save Changes' : 'Create Account'}
                                    </button>
                                    <Link to="/customers" className="btn btn-outline-secondary py-2 border-0">
                                        Cancel & Return
                                    </Link>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default CustomerForm;

