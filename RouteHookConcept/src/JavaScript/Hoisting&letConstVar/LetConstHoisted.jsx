import React from 'react'




/*

✅ Complete Hoisting & TDZ Interview Notes

lll 1. Are let & const Declarations Hoisted?
✔ Yes, let and const are hoisted, but differently from var.
✔ They are hoisted to a separate memory space called Script Scope, not attached to the Global Object like var.
✔ TDZ is the time between hoisting and when the variable is declared — during this time, accessing it gives an error.

✅ (2). What is Temporal Dead Zone (TDZ)?

✅ TDZ is the time between:
➡ Memory allocation (during hoisting)
➡ Actual initialization (when code execution reaches the declaration)

Example:

console.log(a);  // ReferenceError: Cannot access 'a' before initialization  
let a = 10;
➡ Between hoisting and a = 10; — a exists but is uninitialized — that's TDZ.





✅ (3). var vs let & const Hoisting Example:

console.log(b);  // undefined (var is hoisted to global object)
console.log(a);  // ReferenceError (TDZ for 'a')

var b = 100;
let a = 10;
console.log(a);  // 10
✔ var → hoisted to global object → initialized as undefined.
✔ let → hoisted to Script scope → cannot access before initialization.


✅ (4).lll SyntaxError vs ReferenceError vs TypeError
Error Type	              When it Occurs	                                      Example
SyntaxError	              Invalid code structure at compile time	              let x = 10; let x = 20; (redeclaration)
ReferenceError	          Accessing variables in TDZ or undeclared variables	  console.log(a); let a = 5;
TypeError	                Performing invalid operations on data types	          const x = 10; x = 20;


✅ 5.lll Additional Restrictions of let and const

✅ let
    ✅ Cannot redeclare in the same scope
    let a = 10;
    let a = 20;  // SyntaxError

but
    ✅ Can update value
    let a = 10;
    a = 50;  // Allowed'



✅ const
    ✅ More strict than let
    ✅ Cannot redeclare and cannot update
    ✅ Must be initialized at the time of declaration

    const x;  // SyntaxError: Missing initializer  
    const y = 10;
    y = 20;   // TypeError: Assignment to constant variable




✅ Final Interview-Style Statement:
   "In JavaScript, all declarations (var, let, const) are hoisted. But only var is initialized as undefined and attached to the global object. 
   let and const are hoisted to a separate memory (Script scope) and remain uninitialized until execution reaches their line — this inaccessible period is called Temporal Dead Zone. 
   let prevents redeclaration, const prevents both redeclaration and reassignment."






*/









const LetConstHoisted = () => {
  return (
    <div>LetConstHoisted</div>
  )
}

export default LetConstHoisted