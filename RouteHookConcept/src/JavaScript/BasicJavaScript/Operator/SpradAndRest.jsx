import React from 'react'


/*




✅ ... Spread and Rest Operator – Dual Role
🔹 1. Spread Operator
Purpose: Expands elements from arrays, strings, or objects.

// Arrays
const arr1 = [1, 2];
const arr2 = [...arr1, 3, 4];
console.log(arr2); // [1, 2, 3, 4]

// Strings
console.log([..."user"]); // ["u", "s", "e", "r"]

// Objects
const obj1 = { a: 1, b: 2 };
const obj2 = { ...obj1, c: 3 };
console.log(obj2); // { a: 1, b: 2, c: 3 }









🔹 2. Rest Operator
Purpose: Collects remaining parameters into an array (opposite of spread).
Used in:

Function parameters

Object or array destructuring

// Function parameters
function sum(...args) {
  return args.reduce((a, b) => a + b, 0);
}

console.log(sum(1, 2, 3, 4)); // 10

// Destructuring example
const [a, b, ...rest] = [1, 2, 3, 4, 5];
console.log(rest); // [3, 4, 5]

const { name, ...info } = {
  name: "Deepanshu",
  age: 22,
  city: "Gorakhpur"
};
console.log(info); // { age: 22, city: "Gorakhpur" }






✅ Summary
Use Case	                    Operator	                               Example
Spread (expand)	                ...	                                       [...arr], {...obj}, ..."abc"
Rest (collect)	                ...	                                       function(...args), ...[a, b]






🧠 Tip:
Both use the same symbol (...), but Spread is for unpacking, and Rest is for packing values.








*/







const SpradAndRest = () => {
  return (
    <div><h1>Sprad And Rest</h1></div>
  )
}

export default SpradAndRest