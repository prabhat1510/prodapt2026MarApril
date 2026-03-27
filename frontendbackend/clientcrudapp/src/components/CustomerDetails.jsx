const CustomerDetails = ({ customer }) => {
    // Check if customer is selected or has valid data
    if (!customer || !customer.customer_id) {
        return (
            <div className="container mt-4">
                <div className="alert alert-info">
                    Please select a customer from the list to view details.
                </div>
            </div>
        );
    }

    return (
        <div className="container mt-4">
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
                <div className="card-footer bg-light text-end">
                    <button className="btn btn-outline-secondary btn-sm" onClick={() => window.location.reload()}>Back to List</button>
                </div>
            </div>
        </div>
    );
}

export default CustomerDetails;