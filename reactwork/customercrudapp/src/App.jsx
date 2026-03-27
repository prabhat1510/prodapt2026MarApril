import { useState } from "react";
import { Routes, Route, Link, useNavigate } from "react-router-dom";
import Home from "./components/Home";
import CustomerList from "./components/CustomerList";
import About from "./components/About";
import CustomerForm from "./components/CustomerForm";
import CustomerDetails from "./components/CustomerDetails";
import initialCustomers from "./assets/customers.json";

function App() {
    const navigate = useNavigate();
    const [customers, setCustomers] = useState(initialCustomers);
    const [selectedCustomer, setSelectedCustomer] = useState({});

    const handleAddCustomer = (newCust) => {
        setCustomers([...customers, newCust]);
    };

    const handleEditCustomerSubmit = (updatedCust) => {
        setCustomers(customers.map(c => c.id === updatedCust.id ? updatedCust : c));
    };

    const handleDeleteCustomer = (id) => {
        setCustomers(customers.filter(c => c.id !== id));
        if (selectedCustomer.id === id) {
            setSelectedCustomer({});
        }
    };

    const handleCustomerClick = (cust) => {
        setSelectedCustomer(cust);
    };

    const onEdit = (cust) => {
        navigate(`/edit/${cust.id}`);
    };

    return (
        <div className="bg-light min-vh-100 pb-5">
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark shadow-sm mb-4">
                <div className="container">
                    <Link to="/" className="navbar-brand fw-bold">
                        <i className="bi bi-people-fill me-2"></i>TopGuns Bank
                    </Link>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarNav">
                        <ul className="navbar-nav ms-auto">
                            <li className="nav-item">
                                <Link to="/" className="nav-link">Home</Link>
                            </li>
                            <li className="nav-item">
                                <Link to="/customers" className="nav-link btn btn-outline-success btn-sm ms-lg-3 px-3 py-1 mt-2 mt-lg-0 text-white border-success">
                                    Customers
                                </Link>
                            </li>
                            <li className="nav-item ms-lg-3">
                                <Link to="/about" className="nav-link">About</Link>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>

            <div className="container">
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route
                        path="/customers"
                        element={
                            <div className="row">
                                <div className="col-lg-8">
                                    <CustomerList
                                        customers={customers}
                                        onCustomerClick={handleCustomerClick}
                                        selectedCustomerId={selectedCustomer.id}
                                        onDelete={handleDeleteCustomer}
                                        onEdit={onEdit}
                                    />
                                </div>
                                <div className="col-lg-4">
                                    <CustomerDetails selectedCustomer={selectedCustomer} />
                                </div>
                            </div>
                        }
                    />
                    <Route path="/about" element={<About />} />
                    <Route
                        path="/create"
                        element={<CustomerForm onAddCustomer={handleAddCustomer} customers={customers} />}
                    />
                    <Route
                        path="/edit/:id"
                        element={<CustomerForm onUpdateCustomer={handleEditCustomerSubmit} customers={customers} />}
                    />
                </Routes>
            </div>
        </div>
    )
}

export default App;

