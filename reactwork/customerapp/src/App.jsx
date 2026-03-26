import { useState } from "react";
import CustomerFormComponent from "./components/CustomerFormComponent";
import CustomerListComponent from "./components/CustomerListComponent";
import CustomerDetailsComponent from "./components/CustomerDetailsComponent";
import initialCustomersData from './assets/customers.json';
import fs from 'fs';
function App() {
    const [selectedCustomer, setSelectedCustomer] = useState({});
    const [customers, setCustomers] = useState(initialCustomersData);

    const addCustomer = (newCustomer) => {
        setCustomers([...customers, newCustomer]);
        //Write code to save the data to the customers.json file
        const updatedCustomers = [...customers, newCustomer];
        setCustomers(updatedCustomers);
        localStorage.setItem('customers', JSON.stringify(updatedCustomers));
        //Update data in customers.json file
        //const fs = require('fs');
        //fs.writeFileSync('./assets/customers.json', JSON.stringify(updatedCustomers, null, 2));
        //console.log(updatedCustomers);
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