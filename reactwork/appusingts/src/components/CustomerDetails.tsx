import type { Customer } from "../types"

const CustomerDetails = (props: Customer) => {
    return (
        <div>
            <h1>Customer Details</h1>
            <p>Name: {props.name}</p>
            <p>Email: {props.email}</p>
            <p>Phone: {props.phone}</p>
            <p>Address: {props.address}</p>
        </div>
    )
}

export default CustomerDetails