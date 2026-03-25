import { useState } from "react";
import CustomerListComponent from "./CustomerListComponent";

const CustomerFormComponent = () => {

    const [customer, setCustomer] = useState({
        name: "",
        email: "",
        contact: "",
        accountType: ""
    });

    const [customers, setCustomers] = useState([]); // array

    const handleChange = (e) => {
        console.log("e.target.name-->", e.target.name);
        console.log("e.target.value-->", e.target.value);
        setCustomer({ ...customer, [e.target.name]: e.target.value });
    }

    const handleSubmit = (e) => {
        e.preventDefault();

        //Add new customer to list
        setCustomers([...customers, customer]);

        console.log(customer);

        // reset form
        setCustomer({
            name: "",
            email: "",
            contact: "",
            accountType: ""
        });
    }

    return (
        <div className="container">
            <h1>Customer Form</h1>

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
                    <label className="form-label">Contact</label>
                    <input
                        type="text"
                        name="contact"   // IMPORTANT
                        className="form-control"
                        value={customer.contact}
                        onChange={handleChange}
                    />
                </div>

                <div className="mb-3">
                    <label className="form-label">Account Type</label>
                    <select
                        name="accountType"   // IMPORTANT
                        className="form-select"
                        value={customer.accountType}
                        onChange={handleChange}
                    >
                        <option value="">Select</option>
                        <option value="savings">Savings</option>
                        <option value="current">Current</option>
                    </select>
                </div>

                <button type="submit" className="btn btn-primary">
                    Submit
                </button>
            </form>

            {/* pass array */}
            <CustomerListComponent customers={customers} />
        </div>
    );
};

export default CustomerFormComponent;