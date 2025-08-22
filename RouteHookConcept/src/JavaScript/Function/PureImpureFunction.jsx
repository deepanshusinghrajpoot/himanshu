import React from 'react'

/*


✅ Pure Function in JavaScript
lll A Pure Function strictly follows two important rules:

1️⃣ Same Output for Same Input
A pure function always returns the same output for the same input, no matter when or how many times it's called.


✅ Example: Pure Function (Consistent Output)

function greet(name) {
    return `Hello ${name}`;
}

console.log(greet("Deepanshu"));  // Hello Deepanshu
console.log(greet("Deepanshu"));  // Hello Deepanshu

Why Pure?
✔ Output depends only on input
✔ No dependence on external state

❌ Example: Impure Function (Depends on External State)

let name = "Deepanshu";

function greet() {
    return `Hello ${name}`;
}

console.log(greet());  // Hello Deepanshu
name = "Himanshu";
console.log(greet());  // Hello Himanshu


Why Impure?
✖ Output changes with external variable name




2️⃣ No Side Effects
lll A pure function does not modify external state

It doesn't alter global variables, DOM, files, database, etc.


✅ Example: Pure Function (No Side Effect)

let sheepCount = 0;

function addSheep(count) {
    return count + 1;
}

sheepCount = addSheep(sheepCount);
console.log(sheepCount);  // 1
Why Pure?
✔ Only returns a value, does not modify external state



❌ Example: Impure Function (Has Side Effect)

let count = 0;

function increaseCount() {
    count++;   // Modifying external variable
    return count;
}

console.log(increaseCount());  // 1
console.log(increaseCount());  // 2


Why Impure?
✖ Changes global count variable, creates side effect






⚡️ Common Examples of Impure Functions
Function	                           Why Impure?
Math.random()	                       Returns different value each time
new Date()	                         Gives different date-time
DOM Manipulation	                   Alters external page content
API Calls	                           Depends on server response



🔥 Why Use Pure Functions?
✅lll Predictable and consistent behavior
✅lll Easy to test and debug
✅lll No hidden side effects
✅ Encourages clean, functional code
✅ Improves maintainability



🎯 Summary: Pure vs Impure
lll ✅ Pure Function:
        Same output for same input
        No side effects

        lll output does not depend on external state

❌ Impure Function:
        Output depends on external state
        Creates side effects

        lll A pure function does modify external state

        

*/




const PureImpureFunction = () => {
  return (
    <div>PureImpureFunction</div>
  )
}

export default PureImpureFunction