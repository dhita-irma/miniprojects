// Bind() with no argument

// Create objects
const john = {
    name: 'John',
    age: 24,
};

const jane = {
    name: 'Jane',
    age: 22,
};


// Create function
function greeting() {
    console.log(`Hi, I am ${this.name} and I am ${this.age} years old`);
}

// Bind
const greetingJohn = greeting.bind(john);
greetingJohn();

const greetingJane = greeting.bind(jane);
greetingJane();
