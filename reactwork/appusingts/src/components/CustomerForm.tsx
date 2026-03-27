import { useState } from "react"
import type { Customer } from "../types"

const CustomerForm = () => {
    const [customer, setCustomer] = useState<Customer>({
        name: '',
        email: '',
        phone: '',
        address: '',
    })

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setCustomer({ ...customer, [e.target.name]: e.target.value })
    }

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault()
        console.log('Customer data registered:', customer)
        alert('Customer registered successfully!')

    }

    return (
        <div className="card">
            <h1>Register Customer</h1>
            <p className="subtitle">Please fill out the form below to create a new profile.</p>

            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="name">Full Name</label>
                    <input
                        id="name"
                        name="name"
                        value={customer.name}
                        onChange={handleChange}
                        placeholder="e.g. John Doe"
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="email">Email Address</label>
                    <input
                        id="email"
                        type="email"
                        name="email"
                        value={customer.email}
                        onChange={handleChange}
                        placeholder="john@example.com"
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="phone">Phone Number</label>
                    <input
                        id="phone"
                        name="phone"
                        value={customer.phone}
                        onChange={handleChange}
                        placeholder="+1 (555) 000-0000"
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="address">Address</label>
                    <input
                        id="address"
                        name="address"
                        value={customer.address}
                        onChange={handleChange}
                        placeholder="123 Main St, Springfield"
                    />
                </div>
                <button type="submit">Complete Registration</button>
            </form>
        </div>
    )
}

export default CustomerForm