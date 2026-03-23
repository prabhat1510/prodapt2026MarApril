//const prompt = require("prompt-sync")();
import PromptSync from "prompt-sync";
const prompt = PromptSync();
var sizeOfArray = parseInt(prompt("Enter the size of the array"));
var arr = new Array(sizeOfArray);
for (var i = 0; i < sizeOfArray; i++) {
    arr[i] = parseInt(prompt("Enter the " + (i + 1) + "th element"));
}
console.log(arr);
console.log("****************************")
for (var i = 0; i < sizeOfArray; i++) {
    console.log(arr[i]);
}