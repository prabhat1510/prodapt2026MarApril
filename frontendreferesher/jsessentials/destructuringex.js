class Login {
    constructor(username, password) {
        this.username = username;
        this.password = password;
    }
}

const login = new Login("admin", "password");
console.log(login);

//destructuring
const { username, password } = login;
console.log(username);
console.log(password);

const users = [
    { id: 1, name: "John", salary: 1000 },
    { id: 2, name: "Jane", salary: 2000 },
    { id: 3, name: "Bob", salary: 3000 }
];
console.log(users);

const [user1, user2, user3] = users;
console.log(user1);
console.log(user2);
console.log(user3);