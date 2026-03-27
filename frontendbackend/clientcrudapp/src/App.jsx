import { BrowserRouter, Routes, Route, Navigate, Link } from "react-router-dom";
import CustomerList from "./components/CustomerList";
import CustomerDetails from "./components/CustomerDetails";
import CustomerForm from "./components/CustomerForm";

const App = () => {
    return (
        <BrowserRouter>
            {/* Navbar */}
            <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
                <div className="container">
                    <Link className="navbar-brand fw-bold" to="/customers">Prodapt CRM</Link>
                    <div className="d-flex gap-3">
                        <Link className="btn btn-outline-light btn-sm" to="/customers">Customers</Link>
                        <Link className="btn btn-light btn-sm text-primary fw-semibold" to="/customers/new">+ Add Customer</Link>
                    </div>
                </div>
            </nav>

            {/* Page body */}
            <div className="bg-light min-vh-100 py-4">
                <div className="container">
                    <Routes>
                        <Route path="/" element={<Navigate to="/customers" replace />} />
                        <Route path="/customers" element={<CustomerList />} />
                        <Route path="/customers/new" element={<CustomerForm />} />
                        <Route path="/customers/:id/edit" element={<CustomerForm />} />
                        <Route path="/customers/:id" element={<CustomerDetails />} />
                    </Routes>
                </div>
            </div>
        </BrowserRouter>
    );
};

export default App;