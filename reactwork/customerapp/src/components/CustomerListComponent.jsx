const CustomerListComponent = ({ customers }) => {
    //console.log(customers);
    return (
        <div className="container">
            <h1>Customer List</h1>
            <table className="table">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Contact</th>
                        <th>Account Type</th>
                    </tr>
                </thead>
                <tbody>
                    {customers.map((cust, index) => (
                        <tr key={index}>
                            <td>{cust.name}</td>
                            <td>{cust.email}</td>
                            <td>{cust.contact}</td>
                            <td>{cust.accountType}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}

export default CustomerListComponent