import React from 'react'

/*

✅ 1. Function Statement vs Function Declaration
✔ Both terms mean the same thing: Defining a function with a name, independently.

Example (Function Statement / Declaration):

function a() {
    console.log("a called");
}
✔ Hoisted fully, so you can call a() before its definition.




✅ 2. Function Expression
✔ When a function is assigned to a variable, it's called a Function Expression.

var b = function () {
    console.log("b called");
};
✔ Only the variable b is hoisted (initialized as undefined).
✔ Calling b() before assignment gives TypeError.

Example:

a();  // Works
b();  // TypeError: b is not a function

function a() {
    console.log("a called");
}

var b = function () {
    console.log("b called");
};






✅ 3. Anonymous Function
✔ A function without a name is called an Anonymous Function.
✔ Standalone anonymous functions are invalid:

function () { }  // SyntaxError
✔ But used in Function Expressions:

var b = function () {
    console.log("Anonymous Function");
};





✅ 4. Named Function Expression

var b = function xyz() {
    console.log(xyz);  // Logs function definition
};

b();      // Works
xyz();    // ReferenceError: xyz is not defined
✔ Function name xyz is only available inside the function body for recursion/debugging.




✅ 5. Parameters vs Arguments
Term	                    Meaning
Parameters	                Local variable names in function definition
Arguments	                Actual values passed during function call

Example:
function p(param) {
    console.log(param);  // parameter used inside
}

p("argument");  // argument passed during call





✅ 6. First Class Functions
✔ JavaScript treats functions as First-Class Citizens:

Meaning:
      Functions can be stored in variables
      Passed as arguments
      Returned from other functions

Example:

var b = function (param) {
    return function xyz() {
        console.log("Returned Function");
    }
};

console.log(b()());  // Logs "Returned Function"






✅ Final Interview-Ready Statements
✔ Function Declarations are hoisted completely, Function Expressions are not.
✔ Anonymous functions have no name, often used in expressions or callbacks.
✔ First Class Functions mean functions can be passed, returned, or stored like any other value.


*/

const BasicOfFunction = () => {
  return (
    <div><h1>BasicOfFunction</h1></div>
  )
}

export default BasicOfFunction