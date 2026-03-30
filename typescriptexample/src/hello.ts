const message = "Hello World";
console.log(message);

let helloWorld: string = "Hello World";
console.log(helloWorld);

function printMessage(message: string) {
    console.log(message);
}
printMessage(helloWorld);
//printMessage(123); // This will give error -- Argument of type 'number' is not assignable to parameter of type 'string'.
//printMessage((123).toString());
const customer = {
    name: "John",
    age: 30,
    email: "john@gmail.com",
    phone: "1234567890"
}

console.log(customer.age)