let languages = ["C", "C++", "Java", "Python", "JavaScript"];
languages.push("TypeScript"); //adds to end of the array
languages.pop(); //removes from end of the array
languages.shift(); //removes from start of the array
languages.unshift("HTML"); //adds to start of the array
languages.splice(2, 0, "CSS"); //adds CSS at index 2
languages.splice(2, 1); //removes 1 element from index 2
console.log("****************************")
languages.forEach(function (language) {
    console.log(language);
});
console.log("****************************")
languages.forEach((language) => {
    console.log(language);
});
console.log("****************************")
languages.forEach((language, index) => {
    console.log(language, index);
});
console.log("****************************")
languages.forEach((language, index, array) => {
    console.log(language, index, array);
});


let arrayOfNumbers = [1, 2, 3, 4, 5];
console.log("****************************")
let newArray = []
arrayOfNumbers.forEach(function (number) {
    let square = number * number
    newArray.push(square)
});
console.log(newArray)
console.log("****************************")
let oddEvenNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
let oddNumbers = []
let evenNumbers = []
oddEvenNumbers.forEach(function (number) {
    if (number % 2 == 0) {
        evenNumbers.push(number)
    } else {
        oddNumbers.push(number)
    }
});
console.log(oddNumbers)
console.log(evenNumbers)
