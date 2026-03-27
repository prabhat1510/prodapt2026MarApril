import React from 'react';

const CustomerDetails = ({ selectedCustomer }) => {
    // Check if a customer is selected and has an id
    if (!selectedCustomer || !selectedCustomer.id) {
        return (
            <div className="card shadow-sm border-0 mt-4 rounded-3 h-100">
                <div className="card-body text-center d-flex flex-column justify-content-center py-5">
                    <div className="mb-3">
                        <i className="bi bi-person-badge text-muted" style={{ fontSize: '3rem' }}></i>
                    </div>
                    <h3 className="card-title text-muted fw-light">No Selection</h3>
                    <p className="card-text text-muted">Please select a customer from the list to view their detailed profile.</p>
                </div>
            </div>
        );
    }

    return (
        <div className="card shadow border-0 mt-4 rounded-3 overflow-hidden animate-fade-in">
            <div className="card-header bg-primary text-white py-3">
                <h4 className="card-title mb-0">Customer Profile</h4>
            </div>
            <div className="card-body p-4">
                <div className="row mb-3">
                    <div className="col-12 text-center mb-4">
                        <div className="rounded-circle bg-light d-inline-flex align-items-center justify-content-center border" style={{ width: '80px', height: '80px' }}>
                            <span className="h1 text-primary mb-0">{selectedCustomer.firstname.charAt(0)}{selectedCustomer.lastname.charAt(0)}</span>
                        </div>
                    </div>
                </div>

                <div className="list-group list-group-flush border rounded">
                    <div className="list-group-item d-flex justify-content-between p-3">
                        <span className="text-secondary fw-bold">Customer ID</span>
                        <span className="badge bg-light text-dark border">#{selectedCustomer.id}</span>
                    </div>
                    <div className="list-group-item d-flex justify-content-between p-3">
                        <span className="text-secondary fw-bold">First Name</span>
                        <span className="text-dark">{selectedCustomer.firstname}</span>
                    </div>
                    <div className="list-group-item d-flex justify-content-between p-3">
                        <span className="text-secondary fw-bold">Last Name</span>
                        <span className="text-dark">{selectedCustomer.lastname}</span>
                    </div>
                    <div className="list-group-item d-flex flex-column p-3">
                        <span className="text-secondary fw-bold mb-1">Email Address</span>
                        <span className="text-primary text-break">{selectedCustomer.email}</span>
                    </div>
                </div>

                <div className="mt-4 text-center">
                    <button className="btn btn-outline-secondary btn-sm" onClick={() => window.print()}>
                        <i className="bi bi-printer me-2"></i> Print Profile
                    </button>
                </div>
            </div>
        </div>
    );
};

export default CustomerDetails;
