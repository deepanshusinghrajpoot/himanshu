import React from 'react'


/*

✅ Functional Programming (FP)
✔ Functional Programming is a programming paradigm where functions are treated as first-class citizens, meaning:

Functions can be stored in variables
Passed as arguments to other functions
Returned from other functions

✔ Pure Functions, Immutability, and Higher-Order Functions are core to Functional Programming.



lll ✅ What is a Higher-Order Function (HOF)?
✔ A Higher-Order Function is a function that does at least one of the following:

      ✅ Takes another function as an argument
      ✅ Returns another function



✅ Example of Higher-Order Function

function x() {
    console.log("Namaste JavaScript");
}

function y(callback) {
    callback();  // Function passed as argument
}

y(x);  // Output: Namaste JavaScript
✔ Here, y() is a Higher-Order Function, as it accepts x() as an argument.
✔ x() is a callback function, passed to y().

✅ Returning Function from Another Function

function outer() {
    return function inner() {
        console.log("Returned Function");
    };
}

const result = outer();
result();  // Output: Returned Function
✔ Here, outer() is a Higher-Order Function as it returns a function.


✅ Benefits of Higher-Order Functions
✔ Reusability
✔ Modularity
✔ Cleaner, more maintainable code
✔ Enables Functional Programming concepts like:

         Callback functions
         Function composition
         Currying
         Map, Filter, Reduce




*/





const HOF = () => {

  let radius = [1, 2, 3, 4, 5];
 
  function area(r){
    return (Math.PI * r * r);
  }

  function circumTance(r){
    return (2* Math.PI * r)
  }

  function diameter(r){
    return (2 * r);
  }

  Array.prototype.calculate = (logic) => {
      let output = [];
      for(let i=0; i<this.length; i++){
         output.push(logic(this[i]));
      }
      return output;
  }

  console.log(radius.map(area));
  console.log(radius.map(circumTance));
  console.log(radius.map(diameter));



  console.log("area => ", radius.calculate(area));
  console.log("circumTance => ", radius.calculate(circumTance));
  console.log("diameter => ", radius.calculate(diameter));
  


  return (
    <div><h1>Higher Order Function</h1></div>
  )
}

export default HOF