// ES6 Features:

// Let and Const
let age = 25;
const pi = 3.14;

// Arrow Functions
const add = (a, b) => a + b;

// Template Literals
const name = "Alice";
console.log(`Hello, ${name}!`);

// Classes
class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        console.log(`${this.name} makes a sound.`);
    }
}

const cat = new Animal("Cat");
cat.speak(); // Output: Cat makes a sound.

// Modules
// Create two files, module1.js and module2.js.
// module1.js
export const message = "Hello from Module 1!";

// module2.js
import { message } from './module1.js';
console.log(message);

// Working of JavaScript:

// Interpretation: JavaScript is automatically interpreted by web browsers. You don't need to compile it.

// Single-Threaded: JavaScript executes one task at a time. Asynchronous operations ensure non-blocking behavior.

// Event-Driven:
document.getElementById("myButton").addEventListener("click", function() {
    console.log("Button clicked!");
});

// DOM Manipulation:
document.getElementById("myDiv").innerHTML = "Hello, World!";

// Scope and Closures:
function outer() {
    let x = 10;

    function inner() {
        console.log(x); // Inner function can access the 'x' variable from the outer scope.
    }

    return inner;
}

const closureFunc = outer();
closureFunc(); // Output: 10

// Advanced JavaScript Topics:

// Object-Oriented Programming (OOP):
class Car {
    constructor(make, model) {
        this.make = make;
        this.model = model;
    }

    drive() {
        console.log(`Driving the ${this.make} ${this.model}`);
    }
}

const myCar = new Car("Toyota", "Camry");
myCar.drive();

// Functional Programming:
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(number => number * 2);
console.log(doubled); // Output: [2, 4, 6, 8, 10]

// Design Patterns:

// Singleton Pattern
class Singleton {
    constructor() {
        if (!Singleton.instance) {
            Singleton.instance = this;
        }
        return Singleton.instance;
    }
}

const instance1 = new Singleton();
const instance2 = new Singleton();
console.log(instance1 === instance2); // Output: true (Both instances are the same)

// Promises and Async/Await Patterns:
function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Data fetched!");
        }, 2000);
    });
}

async function getData() {
    try {
        const data = await fetchData();
        console.log(data);
    } catch (error) {
        console.error(error);
    }
}

getData();
