import { useState } from "react";
import CustomerList from "./components/CustomerList";
import CustomerDetails from "./components/CustomerDetails";
import CustomerForm from "./components/CustomerForm";

const App = () => {
    const [selectedCustomer, setSelectedCustomer] = useState(null);
    const [editingCustomer, setEditingCustomer] = useState(null);
    const [refreshKey, setRefreshKey] = useState(0);

    const handleFormSuccess = () => {
        setEditingCustomer(null);
        setRefreshKey((prev) => prev + 1); // triggers CustomerList to re-fetch
    };

    return (
        <div className="bg-light min-vh-100 py-5">
            <div className="container">
                <header className="mb-5 text-center">
                    <h1 className="display-4 fw-bold text-primary">Prodapt CRM</h1>
                    <p className="lead text-secondary">Manage and view customer records efficiently</p>
                </header>
                <div className="row justify-content-center">
                    <div className="col-lg-10 mb-5">
                        <CustomerForm
                            customer={editingCustomer}
                            onSuccess={handleFormSuccess}
                        />
                    </div>
                </div>

                <div className="row justify-content-center">
                    <div className="col-lg-10 mb-5">
                        <CustomerList
                            customerSelected={setSelectedCustomer}
                            onEditCustomer={setEditingCustomer}
                            refreshKey={refreshKey}
                        />
                    </div>
                </div>

                <div className="row justify-content-center">
                    <div className="col-lg-8">
                        {selectedCustomer && (
                            <CustomerDetails customer={selectedCustomer} />
                        )}

                        {!selectedCustomer && (
                            <div className="text-center text-muted border rounded p-5 bg-white shadow-sm">
                                <i className="bi bi-person-badge display-1 d-block mb-3"></i>
                                <p>Click the "Show" button in the list above to view customer details.</p>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default App;