import React from 'react'


/*


✅ Function Currying - Interview-Ready Notes

✔ lll Function Currying transforms a function with multiple arguments into a sequence of functions, each taking one argument at a time.
✔ lll Currying improves reusability, modularity, and helps in function customization.







✅lll Two Ways to Implement Currying

1️⃣lll Currying Using bind()
✔ The bind() method creates a copy of a function with preset arguments (partial application).


Example:

let multiply = function (x, y) {
    console.log(x * y);
};

let multiplyByTwo = multiply.bind(this, 2);          // '2' fixed as first argument (x)
multiplyByTwo(3);                                    // Output: 6

let multiplyByThree = multiply.bind(this, 3);
multiplyByThree(4);                                  // Output: 12

let multiplyFixed = multiply.bind(this, 2, 5);
multiplyFixed();                                     // Output: 10 (extra arguments ignored if already filled)






2️⃣ Currying Using Closures
✔ Closure captures variables and returns functions incrementally.

Example:

let multiply = function (x) {
    return function (y) {
        console.log(x * y);
    };
};

let multiplyByTwo = multiply(2);
multiplyByTwo(3);                                  // Output: 6

let multiplyByThree = multiply(3);
multiplyByThree(10);                               // Output: 30






✔ You can keep nesting functions for deep currying:

function sum(a) {
    return function (b) {
        return function (c) {
            console.log(a + b + c);
        };
    };
}

sum(2)(3)(4);  // Output: 9





✅ Benefits of Currying
✔ Reusability of functions
✔ Custom functions with preset arguments
✔ Useful for functional programming patterns
✔ Improves code readability and maintainability






✅ Final Interview Statement
"Function Currying converts a function with multiple parameters into nested functions, each taking one parameter. 
It can be implemented using bind() for partial application or using closures for flexible, reusable functions."





*/



const Currying = () => {


  function x(){
      for(var i=0; i<5; i++){
         function y(x){
            setTimeout(()=>{
              console.log("count:- ", x);
            },i*1000)
         }
         y(i);
      }
  }
  x();



  return (
    <div><h1>Currying</h1></div>
  )
}

export default Currying