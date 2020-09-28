// Bind() with argument


// Create function
function greeting(lang) {
    console.log(`${lang}: I am ${this.name}`)
}

// Create object
const john = {
    name: 'John'
}


const greetingJohn = greeting.bind(john, 'en');
greetingJohn();