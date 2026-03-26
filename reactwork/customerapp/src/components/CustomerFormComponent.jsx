import { useState } from "react";


const CustomerFormComponent = ({ onAddCustomer, customers }) => {

    const [customer, setCustomer] = useState({
        name: "",
        email: "",
        phone: "",
    });

    const handleChange = (e) => {
        setCustomer({ ...customer, [e.target.name]: e.target.value });
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        
        // Ensure customers list exists to find length
        const nextId = (customers && customers.length > 0) 
            ? Math.max(...customers.map(c => c.id)) + 1 
            : 1;

        const newCustomer = {
            id: nextId,
            ...customer
        }

        // Send to parent state manager
        if (onAddCustomer) {
            onAddCustomer(newCustomer);
        }

        // Reset form
        setCustomer({
            name: "",
            email: "",
            phone: "",
        });
    }

    return (
        <div className="container">
            <h1>Add Customer</h1>

            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label className="form-label">Name</label>
                    <input
                        type="text"
                        name="name"   // IMPORTANT
                        className="form-control"
                        value={customer.name}
                        onChange={handleChange}
                    />
                </div>

                <div className="mb-3">
                    <label className="form-label">Email</label>
                    <input
                        type="email"
                        name="email"   // IMPORTANT
                        className="form-control"
                        value={customer.email}
                        onChange={handleChange}
                    />
                </div>

                <div className="mb-3">
                    <label className="form-label">Phone</label>
                    <input
                        type="text"
                        name="phone"   // IMPORTANT
                        className="form-control"
                        value={customer.phone}
                        onChange={handleChange}
                    />
                </div>

                <button type="submit" className="btn btn-primary">
                    Submit
                </button>
            </form>

        </div>
    );
};

export default CustomerFormComponent;