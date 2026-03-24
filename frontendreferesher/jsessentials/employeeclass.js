class Employee {
    constructor(id, name, salary) {
        this.id = id;
        this.name = name;
        this.salary = salary;
    }

    getId() {
        return this.id;
    }

    getName() {
        return this.name;
    }

    getSalary() {
        return this.salary;
    }

    display() {
        console.log(this.id + " " + this.name + " " + this.salary);
    }
}

const emp1 = new Employee(1, "John", 1000);
const emp2 = new Employee(2, "Jane", 2000);
const emp3 = new Employee(3, "Bob", 3000);

console.log(emp1);
console.log(emp2);
console.log(emp3);

let employees = [emp1, emp2, emp3];
console.log(employees);
const emp4 = new Employee(4, "John", 1000);
console.log(emp4);
employees.push(emp4);
console.log(employees);