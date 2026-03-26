//import customers from '../assets/customers.json'
import { useState } from 'react';

const CustomerListComponent = ({ onCustomerClick, customers }) => {
    // customers is now provided as a prop from App.jsx

    // Safety check to prevent errors during rendering if customers is undefined
    if (!customers) {
        return <div className="container mt-4">Loading customers...</div>;
    }

    return (
        <div className="container mt-4">
            <h1 className="mb-3">Customer List</h1>
            <table className="table table-hover table-bordered table-sm">
                <thead className="thead-light">
                    <tr>
                        <th>Id</th>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Phone</th>
                    </tr>
                </thead>
                <tbody>
                    {customers.map((cust, index) => (
                        <tr
                            onClick={() => onCustomerClick(cust)}  // ✅ FIXED
                            key={index}
                            style={{ cursor: "pointer" }}
                        >
                            <td>{cust.id}</td>
                            <td>{cust.name}</td>
                            <td>{cust.email}</td>
                            <td>{cust.phone}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}

export default CustomerListComponent;