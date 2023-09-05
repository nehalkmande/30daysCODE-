//js Basics

// Variable
let name = "Nehal";

// Function
function greet(name) {
   console.log("Hello, " + name + "!");
}

// Conditional Statement
let age = 18;
if (age >= 18) {
   console.log("You are an adult.");
} else {
   console.log("You are not yet an adult.");
}

// Loop
for (let i = 0; i < 3; i++) {
   console.log("Iteration " + i);
}

// Array
let colors = ["red", "green", "blue"];
console.log(colors[0]); // Accesses the first element, "red."

// Object
let person = { name: "Arav", age: 25 };
console.log(person.name); // Accesses the 'name' property, which is "Arav."

// Event Handling (This requires an HTML element with the ID "myButton" to be present)
// You can remove this part if you're not working in a web environment
document.getElementById("myButton").addEventListener("click", function() {
   alert("Button clicked!");
});

// Variables with different data types
let num = 30; // Integer
let userName = "John"; // String
let isStudent = true; // Boolean
let initial = 'A'; // JavaScript doesn't have a separate 'char' type
let noValue = null; // Null

// Type conversions
let numString = "42"; // String
let numConverted = parseInt(numString); // Convert to Integer
console.log(numConverted); // Output: 42

let boolString = "true"; // String
let boolConverted = Boolean(boolString); // Convert to Boolean
console.log(boolConverted); // Output: true

// Operators
let a = 5;
let b = 2;

// Arithmetic operators
let sum = a + b; // Addition
let difference = a - b; // Subtraction
let product = a * b; // Multiplication
let quotient = a / b; // Division
let remainder = a % b; // Modulus

// Comparison operators
let isEqual = a === b; // Equal to
let isNotEqual = a !== b; // Not equal to
let isGreaterThan = a > b; // Greater than
let isLessThan = a < b; // Less than
let isGreaterOrEqual = a >= b; // Greater than or equal to
let isLessOrEqual = a <= b; // Less than or equal to

// Logical operators
let andResult = true && false; // Logical AND
let orResult = true || false; // Logical OR
let notResult = !true; // Logical NOT

// String concatenation
let greeting = "Hello";
let anotherName = "Alice"; // Changed the variable name here
let welcomeMessage = greeting + " " + anotherName; // Concatenate strings

console.log("Sum:", sum);
console.log("isEqual:", isEqual);
console.log("andResult:", andResult);
console.log("welcomeMessage:", welcomeMessage);
