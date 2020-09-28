class User{
    constructor(firstname, lastname, credit){
        this.firstname = firstname
        this.lastname = lastname
        this.credit = credit
    }

    // Create class methods
    getFullName(){
        return `${this.firstname} ${this.lastname} is my full name`
    }

    editName(newname){
        const myname = newname.split(' ')
        this.firstname = myname[0]
        this.lastname = myname[1]
    }
}

const john = new User("John", "Anderson", 34);

console.log(john);
console.log(john.getFullName()); 

john.editName("Johny Anderson");
console.log(john.getFullName());

// const justin = new User();
// console.log(justin);