var fruits1 = ["apple", "banana", "orange", "mango", "grapes"];
console.log(fruits1);
console.log(typeof fruits1);

//Creating an fruits2 array using new keyword and passing values as arguments to the constructor of Array class
var fruits2 = new Array("apple", "banana", "orange", "mango", "grapes");
console.log(fruits2);
console.log(typeof fruits2);

//Creating an fruits3 array using new keyword and passing size of the array as argument to the constructor of Array class
var fruits3 = new Array(5);
fruits3[0] = "apple";
fruits3[1] = "banana";
fruits3[2] = "orange";
fruits3[3] = "mango";
fruits3[4] = "grapes";
console.log(fruits3);
console.log(typeof fruits3);

for (var i = 0; i < fruits1.length; i++) {
    console.log(fruits1[i]);
}
console.log("****************************")
for (fruit in fruits1) { //Here fruit variable referes to index of fruits in fruits1
    console.log(fruits1[fruit]);
}
console.log("****************************")
for (fruit of fruits1) { //Here fruit variable referes to value of fruits in fruits1
    console.log(fruit);
}


