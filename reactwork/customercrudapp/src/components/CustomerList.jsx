import React from 'react';
import { Link } from 'react-router-dom';

const CustomerList = ({ onCustomerClick, customers, selectedCustomerId, onEdit, onDelete }) => {
    // Safety check to prevent errors during rendering if customers is undefined
    if (!customers || customers.length === 0) {
        return (
            <div className="container mt-4 text-center py-5">
                <div className="spinner-border text-primary mb-3" role="status">
                    <span className="visually-hidden">Loading...</span>
                </div>
                <h3 className="text-muted">Loading customers...</h3>
                <p>If the list remains empty, try adding a new customer.</p>
                <Link to="/create" className="btn btn-primary mt-3">Add First Customer</Link>
            </div>
        );
    }

    return (
        <div className="container mt-4 mb-5">
            <div className="d-flex justify-content-between align-items-center mb-4">
                <h2 className="mb-0 text-dark">Customers List</h2>

            </div>

            <div className="table-responsive shadow-sm rounded-3">
                <table className="table table-hover align-middle mb-0">
                    <thead className="bg-light">
                        <tr className="border-top-0">
                            <th className="px-4 py-3 border-0">ID</th>
                            <th className="py-3 border-0">Name</th>
                            <th className="py-3 border-0">Email Address</th>
                            <th className="px-4 py-3 border-0">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {customers.map((cust) => (
                            <tr
                                onClick={() => onCustomerClick && onCustomerClick(cust)}
                                key={cust.id}
                                style={{ cursor: "pointer" }}
                                className={selectedCustomerId === cust.id ? "table-primary active shadow-sm" : ""}
                            >
                                <td className="px-4 fw-bold text-secondary">#{cust.id}</td>
                                <td>
                                    <div className="d-flex align-items-center">
                                        <div className="rounded-circle bg-secondary bg-opacity-10 p-2 me-3" style={{ width: '40px', height: '40px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                                            <span className="text-secondary small">{cust.firstname.charAt(0)}{cust.lastname.charAt(0)}</span>
                                        </div>
                                        <div>
                                            <div className="fw-bold">{cust.firstname} {cust.lastname}</div>
                                            <small className="text-muted">Registered Customer</small>
                                        </div>
                                    </div>
                                </td>
                                <td className="text-muted">{cust.email}</td>
                                <td className="px-4">
                                    <div className="btn-group btn-group-sm">
                                        <button 
                                            className="btn btn-outline-info rounded-pill me-2 px-3"
                                            onClick={(e) => {
                                                e.stopPropagation();
                                                onCustomerClick && onCustomerClick(cust);
                                            }}
                                        >
                                            Show
                                        </button>
                                        <button 
                                            className="btn btn-outline-warning rounded-pill me-2 px-3"
                                            onClick={(e) => {
                                                e.stopPropagation();
                                                onEdit && onEdit(cust);
                                            }}
                                        >
                                            Edit
                                        </button>
                                        <button 
                                            className="btn btn-outline-danger rounded-pill px-3"
                                            onClick={(e) => {
                                                e.stopPropagation();
                                                if(window.confirm(`Are you sure you want to delete ${cust.firstname}?`)) {
                                                    onDelete && onDelete(cust.id);
                                                }
                                            }}
                                        >
                                            Delete
                                        </button>
                                    </div>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            <div className="mt-3 text-end text-muted small">
                Showing {customers.length} total customers
            </div>
        </div>
    )
}

export default CustomerList;
