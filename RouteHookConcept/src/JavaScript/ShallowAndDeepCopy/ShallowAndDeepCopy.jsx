import React from 'react'


/*



✅ Shallow Copy vs Deep Copy in JavaScript



What is a Shallow Copy?
lll A shallow copy copies only the first level of properties. If the object contains nested objects or arrays, 
they are copied by reference, not as new independent copies.



Shallow Copy Example

let obj = {
    name: "Deepanshu Singh",
    age: 25,
    social: {
        facebook: "abc@gmail.com",
        twitter: "xyz@gmail.com"
    }
};

let obj2 = { ...obj };  // Shallow Copy using Spread Operator

obj2.social.facebook = "changed@gmail.com";

console.log(obj.social.facebook);  // changed@gmail.com
console.log(obj2.social.facebook); // changed@gmail.com
🔧 Conclusion: Nested objects share the same reference.








Ways to Create Shallow Copy
---------------------------

✔ Using Spread Operator:
let copy = { ...originalObject };


✔ Using Object.assign():
let copy = Object.assign({}, originalObject);

Both create shallow copies — nested structures are still shared by reference.









What is a Deep Copy?
lll A deep copy creates a completely independent copy of an object, including all nested objects or arrays. 
Changes to the copied object do not affect the original object.







Deep Copy using JSON.stringify()

let obj = {
    name: "Deepanshu",
    social: {
        facebook: "abc@gmail.com"
    }
};

let obj2 = JSON.parse(JSON.stringify(obj));

obj2.social.facebook = "changed@gmail.com";

console.log(obj.social.facebook);  // abc@gmail.com
console.log(obj2.social.facebook); // changed@gmail.com
🚨 Limitation: Doesn't work with functions, undefined, Date, Map, Set, etc.




🚨 Limitation Meaning:
lll When we use JSON.stringify() and JSON.parse() to create a deep copy, 
    some data types do NOT survive the conversion properly.

lll Specifically, it:

❌ Ignores functions
❌ Removes undefined
❌ Breaks Date objects
❌ Loses Map, Set, Symbol, RegExp, etc.



💥 Let's see examples for each limitation:

1. ❌ Function is lost

let obj = {
  name: "Deepanshu",
  greet: function () {
    console.log("Hello");
  }
};

let obj2 = JSON.parse(JSON.stringify(obj));
console.log(obj2); // 👉 { name: 'Deepanshu' }   ❌ 'greet' is gone




2. ❌ undefined is removed

let obj = {
  name: "Deepanshu",
  age: undefined
};

let obj2 = JSON.parse(JSON.stringify(obj));
console.log(obj2); // 👉 { name: 'Deepanshu' }   ❌ 'age' is gone







3. ❌ Date becomes a string

let obj = {
  joined: new Date()
};

let obj2 = JSON.parse(JSON.stringify(obj));
console.log(typeof obj.joined);  // 👉 object
console.log(typeof obj2.joined); // 👉 string ❌









4. ❌ Map and Set are lost

let obj = {
  data: new Map([["a", 1]]),
  list: new Set([1, 2, 3])
};

let obj2 = JSON.parse(JSON.stringify(obj));
console.log(obj2); 
// 👉 { data: {}, list: {} } ❌ They’re now empty plain objects
✅ When to use JSON.parse(JSON.stringify(obj))?
Only when:

Your object has simple values: strings, numbers, booleans, arrays, plain nested objects

You don't care about functions, undefined, Dates, Maps, Sets










✅ Recursive Deep Copy Function
Here is the corrected deep copy function:

function makeDeepCopy(obj) {
    if (obj === null || typeof obj !== "object") {
        return obj;  // Return primitive value
    }

    let copiedVal = Array.isArray(obj) ? [] : {};

    for (let key in obj) {
        if (obj.hasOwnProperty(key)) {
            copiedVal[key] = makeDeepCopy(obj[key]);  // Recursive call
        }
    }

    return copiedVal;
}






Deep Copy Example with Function

let obj = {
    name: "Deepanshu",
    address: {
        city: "Kanpur",
        pin: 208001
    }
};

let obj2 = makeDeepCopy(obj);

obj2.address.city = "Lucknow";

console.log(obj.address.city); // Kanpur
console.log(obj2.address.city); // Lucknow




✅ Quick Interview Summary
Feature	                              Shallow Copy	                                        Deep Copy
Copies nested objects?	              No (references shared)	                            Yes (completely independent)
Methods	                              Spread Operator, Object.assign()	                    JSON methods, Recursive function
Use case	                          Simple objects, no deep nesting	                    Complex, nested structures, avoid shared references


  





 */



const ShallowAndDeepCopy = () => {
  return (
    <div><h1>ShallowAndDeepCopy</h1></div>
  )
}

export default ShallowAndDeepCopy