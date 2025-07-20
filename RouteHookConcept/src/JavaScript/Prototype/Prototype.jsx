import React from 'react'



/*

✅ What is Inheritance?
✔ lll  Inheritance means one object can access the properties or methods of another object.
✔ lll  In JavaScript, all inheritance works via prototypes, not classical class-based inheritance like Java or C++.




✅ What is a Prototype?
✔ lll Every object in JavaScript has a hidden property called [[Prototype]], accessible via __proto__.
✔ lll The prototype itself is also an object, which can have its own prototype — forming a prototype chain.
✔ lll The chain ends at null.



✅ Prototype Inheritance in JavaScript - Complete Interview Notes
✔ lll  Prototype Inheritance is the foundation of inheritance in JavaScript.
✔ lll  Prototype Inheritance allows one object to access properties or methods of another object through the prototype chain.








✅ Examples of Prototype Chain

let arr = ["Deepanshu", "Singh"];
let obj = {
    name: "Deepanshu",
    city: "Gorakhpur",
    getIntro: function () {
        console.log(this.name + " from " + this.city);
    }
};
function fun() {}

✔ Prototype Access
arr.__proto__ === Array.prototype       // true  
arr.__proto__.__proto__ === Object.prototype   // true  
arr.__proto__.__proto__.__proto__ === null    // true  

obj.__proto__ === Object.prototype     // true  
obj.__proto__.__proto__ === null       // true  

fun.__proto__ === Function.prototype   // true  
fun.__proto__.__proto__ === Object.prototype  // true  
fun.__proto__.__proto__.__proto__ === null   // true  

✔ lll Everything in JavaScript (arrays, objects, functions) eventually links to Object.prototype.
✔ This forms the Prototype Chain, ending at null.





✅ Practical Example of Prototype Inheritance

let object1 = {
    name: "Deepanshu",
    city: "Gorakhpur",
    getInfo: function () {
        console.log(this.name + " from " + this.city);
    }
};

let object2 = {
    name: "Himanshu"
};

// Prototype Inheritance (Demo purpose - not recommended with __proto__)
object2.__proto__ = object1;

object2.getInfo();  // Output: Himanshu from Gorakhpur

✔ object2 inherits getInfo() and city from object1 via prototype chain.
✔ If a property exists in both objects, JavaScript uses the nearest one — own property shadows prototype.








✅ Function Prototype Example

Function.prototype.mybind = function () {
    console.log("Custom bind method - Rohan Singh");
};

function fun1() {}
function fun2() {}

fun1.mybind();  // Output: Custom bind method - Rohan Singh  
fun2.mybind();  // Output: Custom bind method - Rohan Singh  

✔ You can extend all functions by adding to Function.prototype.
✔ This is how built-in methods like bind, call, apply work.








✅ Final Interview-Ready Statements
✔ JavaScript uses Prototype Inheritance, where objects inherit from other objects through prototype chains.
✔ The chain continues until null, known as the Prototype Chain.
✔ Functions, arrays, objects — all link to Object.prototype eventually.
✔ Extending prototypes allows adding shared methods, but modifying built-in prototypes is not recommended in production code.






*/






const Prototype = () => {
  return (
    <div><h1>Prototype</h1></div>
  )
}

export default Prototype