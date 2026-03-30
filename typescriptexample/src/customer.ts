interface Customer {
    firstName: string;
    lastName: string;
    email: string;
    phone: string;
}

const cust: Customer = {
    firstName: "John",
    lastName: "Doe",
    email: "[EMAIL_ADDRESS]",
    phone: "1234567890"
}

function isCustomerValid(cust: Customer) {
    return cust.firstName !== "" && cust.lastName !== "" && cust.email !== "" && cust.phone !== "";
}

console.log(isCustomerValid(cust));