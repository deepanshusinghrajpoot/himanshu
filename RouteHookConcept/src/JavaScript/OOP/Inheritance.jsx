import React from 'react'


/*







 What is Inheritance?
-------------------------

✔ lll  Inheritance means one object can access the properties or methods of another object.
✔ lll  In JavaScript, all inheritance works via prototypes, not classical class-based inheritance like Java or C++.




 What is a Prototype?
------------------------

✔ lll Every object in JavaScript has a hidden property called [[Prototype]], accessible via __proto__.
✔ lll The prototype itself is also an object, which can have its own prototype — forming a prototype chain.
✔ lll The chain ends at null.



Prototype Inheritance in JavaScript - Complete Interview Notes
--------------------------------------------------------------

✔ lll  Prototype Inheritance is the foundation of inheritance in JavaScript.
✔ lll  Prototype Inheritance allows one object to access properties or methods of another object through the prototype chain.





Method overridding
-------------------

When base class and derived class contain same function but different implementation.

Then base class function said to method overridding



Super Keyword
--------------

The super keyword is used to call the constructor of its parent class to access the parent's
class properties and methods.


super(args) :- here this args is pass to constructor of base



*/








const Inheritance = () => {


 class Person{

    constructor(name){
        this.species = "homo sapiens";
        this.name = name;
    }

    eat(){
        console.log("eat!");
    }

 }


 class Engineer extends Person{
    
    constructor(name){
        super(name);
    }

    work(){
        super.eat();
        console.log("Solve problem, build something");
    }

 }



 let engObj = new Engineer("Child obj1");

  
  engObj.work();





  return (
    <div>Inheritance</div>
  )
}

export default Inheritance