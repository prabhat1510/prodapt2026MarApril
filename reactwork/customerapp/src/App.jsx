import { useState } from "react";
import CustomerFormComponent from "./components/CustomerFormComponent";
import CustomerListComponent from "./components/CustomerListComponent";
import CustomerDetailsComponent from "./components/CustomerDetailsComponent";
import initialCustomersData from './assets/customers.json';

function App() {
    const [selectedCustomer, setSelectedCustomer] = useState({});
    const [customers, setCustomers] = useState(initialCustomersData);

    const addCustomer = (newCustomer) => {
        setCustomers([...customers, newCustomer]);
    };

    return (
        <div className="container">
            <div className="row mt-4">
                <div className="col-md-12">
                    <CustomerListComponent
                        onCustomerClick={setSelectedCustomer}
                        customers={customers}
                    />
                </div>
            </div>
            <div className="row mt-4">
                <div className="col-md-6">
                    <CustomerFormComponent onAddCustomer={addCustomer} customers={customers} />
                </div>
                <div className="col-md-6">
                    <CustomerDetailsComponent selectedCustomer={selectedCustomer} />
                </div>
            </div>
        </div>
    )
}

export default App