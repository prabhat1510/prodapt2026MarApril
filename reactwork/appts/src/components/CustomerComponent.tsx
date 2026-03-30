import type { Customer } from "./Customer";

export default function CustomerComponent() {
    let customer: Customer = {
        id: 1,
        name: "John",
        email: "john@gmail.com",
        phone: "1234567890"
    };
    return (
        <div>
            <h1>Customer</h1>
            <p>ID: {customer.id}</p>
            <p>Name: {customer.name}</p>
            <p>Email: {customer.email}</p>
            <p>Phone: {customer.phone}</p>
        </div>
    );
}