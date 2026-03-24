/**
fetch("https://jsonplaceholder.typicode.com/users")
    .then(response => response.json())
    .then(data => console.log(data));
*/
/**
let data = fetch("https://jsonplaceholder.typicode.com/users");
console.log(data);
*/

async function getData() {
    let response = await fetch("https://jsonplaceholder.typicode.com/users");
    let data = await response.json();
    console.log(data);
}
getData();

//fetch api with post method
fetch("https://jsonplaceholder.typicode.com/posts", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        title: "foo",
        body: "bar",
        userId: 1
    })
})
    .then(response => response.json())
    .then(data => console.log(data));


//fetch api with then and catch block
fetch("https://jsonplaceholder.typicode.com/users")
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error));

//fetch api with async and await with error handling
async function getData() {
    try {
        let response = await fetch("https://jsonplaceholder.typicode.com/users");
        let data = await response.json();
        console.log(data);
    } catch (error) {
        console.log(error);
    }
}
getData();
