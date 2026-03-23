//function declaration
function show() {
    console.log("hello");
}
show();//calling function

//function with parameters
function show1(a, b) {
    console.log(a + b);
}
show1(10, 20);//calling function with arguments

//function with return value
function show2(a, b) {
    return a + b;
}
console.log(show2(10, 20));//calling function with arguments and return value

//function expression
var show3 = function () {
    console.log("hello");
}
show3();//calling function

//function expression with parameters
var show4 = function (a, b) {
    console.log(a + b);
}
show4(10, 20);//calling function with arguments

//function expression with return value
var show5 = function (a, b) {
    return a + b;
}
console.log(show5(10, 20));//calling function with arguments and return value

//arrow function
var show6 = () => {
    console.log("hello");
}
show6();//calling function

//arrow function with parameters
var show7 = (a, b) => {
    console.log(a + b);
}
show7(10, 20);//calling function with arguments

//arrow function with return value
var show8 = (a, b) => {
    return a + b;
}
console.log(show8(10, 20));//calling function with arguments and return value

//arrow function with return value
var show9 = (a, b) => a + b;
console.log(show9(10, 20));//calling function with arguments and return value

//arrow function with return value
var show10 = (a, b) => a + b;
console.log(show10(10, 20));//calling function with arguments and return value