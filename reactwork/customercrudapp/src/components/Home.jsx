import { Link } from "react-router-dom";
import CustomerList from "./CustomerList";
import customers from '../assets/customers.json'

function Home() {
    return (
        <div>
            <Link to="/create">Create new Customer</Link>
            <CustomerList customers={customers} />
        </div>
    )
}

export default Home