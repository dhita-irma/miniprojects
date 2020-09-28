// Understanding Call, Bind and Apply Methods in JavaScript


// Create person object
const person = {
    firstname:'John',
    lastname: 'Doe',
    printName: function() {
        console.log(this.firstname + ' ' + this.lastname)
    }
}

// Print person's name 
person.printName();