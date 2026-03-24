let student = {
    name: ["Mukesh", "Kumar"],
    age: 21,
    gender: "male",
    interests: ["Carrom", "Bakar"],
    greeting: function () {
        console.log("Hi I am " + this.name[0] + ' .');
    }

}
console.log(typeof student);
console.log(student.name);
console.log(student.gender);
student.greeting()