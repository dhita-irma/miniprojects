// Call() method with arguments 


// Create function
function greet(greeting) {
    console.log(`${greeting}, I am ${this.name} and I am ${this.age} years old`);
}


// Create object
const john = {
    name: 'John',
    age: 24,
}

const jane = {
    name: 'Jane',
    age: 22
}


// Use call() method
greet.call(john, 'Hi');
greet.call(jane, 'Hola');
