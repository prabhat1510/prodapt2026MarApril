const CustomerDetailsComponent = (props) => {
    if (!props.selectedCustomer.id) {
        return (
            <div className="card mt-4">
                <div className="card-body">
                    <h1 className="card-title text-muted">Customer Details</h1>
                    <p className="card-text text-muted">Please select a customer from the list to see details.</p>
                </div>
            </div>
        );
    }

    return (
        <div className="card mt-4">
            <div className="card-body">
                <h1 className="card-title">Customer Details</h1>
                <p className="card-text"><strong>Id:</strong> {props.selectedCustomer.id}</p>
                <p className="card-text"><strong>Name:</strong> {props.selectedCustomer.name}</p>
                <p className="card-text"><strong>Email:</strong> {props.selectedCustomer.email}</p>
                <p className="card-text"><strong>Phone:</strong> {props.selectedCustomer.phone}</p>
            </div>
        </div>
    );
};

export default CustomerDetailsComponent;