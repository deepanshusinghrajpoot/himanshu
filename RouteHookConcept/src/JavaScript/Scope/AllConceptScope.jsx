import React from 'react'


/*

✅ Final Correct Interview-Style Answer:

lll Scope in JavaScript
Scope defines where we can access specific variables or functions in code.

lll Lexical Environment
Created whenever an Execution Context is created

It consists of:
Lexical Environment = Local Memory + Reference to Parent Lexical Environment


lll Simple Definition:
"Lexical Environment means the local memory along with a reference to the parent Lexical Environment."
"Lexical Context means where the function is physically present inside the code."


✅ Example with Execution Context, Lexical Environment, and Scope Chain:

function a() {
    function c() {
        console.log(b);  // ReferenceError: b is not defined
    }
    c();
}

a();



Memory Creation Breakdown:
✔ a() is defined inside the Global Scope, so a is Lexically inside Global.
✔ c() is defined inside a(), so c is Lexically inside a.


Scope Chain Working:
c() tries to access b.
First, it looks in its own Local Memory → b not found.
Then, it follows the parent Lexical Environment, which is a()'s scope → b not found.
Finally, it checks the Global Scope → b not found.
Global Lexical Environment’s outer reference is null, so a ReferenceError is thrown.



lll ✅ Scope Chain Definition:
"The process of searching variables from current Local Memory, moving outward to parent Lexical Environments, is called the Scope Chain."


Call Stack and Execution Flow Example:

function a(){
    function c(){
        console.log("Inside c");
    }
    c();
}
a();


✔ Call Stack:

1. GEC pushed → Global Execution Context
2. `a()` called → new EC for `a`
3. Inside `a()`, `c()` called → new EC for `c`
4. `c()` finishes → pop `c()` EC
5. `a()` finishes → pop `a()` EC
6. Global finishes



✅ Final Conclusion (Interview Version):
JavaScript uses Lexical Scoping, meaning scope is determined by where functions/variables are physically written, not where they are called.
Lexical Environment + Scope Chain ensures variable lookup follows a structured, outward search mechanism.
If a variable isn't found in the entire chain, JavaScript throws a ReferenceError.



*/






const AllConceptScope = () => {


  return (
    <div><h1>AllConceptScope</h1></div>
  )
}

export default AllConceptScope