/*

Question:- What is value of this in global scope?
-------------------------------------------------

lll✅ this in Global Space – Interview Notes
   
   The value of this in global space depend on the inviornment where javaScript is running.
   
lll  when javasScript code is execute in global space the value of this depend on the global object.

   The global object depends on the environment where the JavaScript is running:
   In browsers, the global object is window, so this === window.
   In Node.js, the global object is global, but at the top level of a module, this refers to an empty object {}, not global.
   So, the value of this in the global space is environment-dependent.


🔁 Why is it different?
   Because JavaScript is used in multiple environments like browsers, Node.js, Web Workers, Deno, etc.
   Each provides its own version of the global object.

✅ Final Interview Answer:
“The value of this in the global space is the global object. In a browser, it's window. 
In Node.js, it's global, although at the top level of a Node module, this is {}. 
So, the actual value of this depends on where the code is running.”




Question:- What is value of this inside a function? (Strict vs Non-Strict Mode)
-------------------------------------------------------------------------------

✅ this keyword Inside Function — Strict vs Non-Strict Mode (Interview Notes)
    In JavaScript, when you console.log(this):
    In global space, this refers to the global object (window in browsers).
    Inside a regular function, the behavior depends on whether you are using strict mode or non-strict mode.


⚡ Non-Strict Mode Example:

console.log(this); 
// Output: window

function x() {
  console.log(this); 
}
// In non-strict mode:
x(); 
// Output: window

🧠 Explanation: In non-strict mode, this inside a regular function defaults to the global object (window).


🔒 Strict Mode Example:

"use strict";
console.log(this); 
// Output: window

function x() {
  console.log(this); 
}
x(); 
// Output: undefined

🧠 Explanation: In strict mode, this inside a function is undefined — it does not automatically point to the global object.



🚀 Why this Happens? (This Substitution)
   This Substitution Rule says:
            In non-strict mode, if this becomes null or undefined, JavaScript automatically substitutes it with the global object (like window).
            In strict mode, JavaScript does not substitute — this stays undefined.


lll ✅ Final Interview Answer:
“The value of this inside a regular function depends on strict mode.
In non-strict mode, it points to the global object (window).
In strict mode, it becomes undefined.
it happens because of 'this substitution' — a rule that exists only in non-strict mode.”




Question:- What is value of this inside a function? (Depends on How a Function is Called)
-----------------------------------------------------------------------------------------


✅ this Depends on How a Function is Called — (Interview Notes)

In JavaScript, the value of this is determined at the time the function is called, not where it is defined.

lll Simple Rule:
        If a function is called without any object reference, this will be undefined (in strict mode) or window (in non-strict mode).
        If a function is called with an object reference, this points to that object.

🧠 Example 1 — Function Call (without reference)

"use strict";

function x() {
  console.log(this);
}

x();  
// Output: undefined (because called without any object reference)


🧠 Example 2 — Function Call (with object reference)

"use strict";

function x() {
  console.log(this);
}

window.x();  
// Output: window (because called with window as the reference)


🚀 Important Points:
         In strict mode, if a function is called normally (without an object), this is undefined.
         If called through an object (like window.x()), this points to that object.
         This behavior is dynamic — it depends how you call the function, not where you define it.


✅ Final Interview Answer:
“The value of this depends on how the function is called.
If called without a reference, this is undefined (in strict mode).
If called with an object reference, this becomes that object.”




Question:- What is value of this inside an object method?
---------------------------------------------------------


✅ this Inside an Object's Method — (Interview Notes)

 1. In JavaScript, when a function is a property of an object, it is called a method.

 2. Method vs Function:
           Function: A standalone block of code (not attached to any object).
           Method: A function that is attached to an object as a property.

 3. Important Rule:
           When a method is called using an object (obj.x()), this inside the method refers to the object that called it.


🧠 Example — Method inside an Object

const obj = {
  a: 10,
  x: function () {
    console.log(this);
  }
};

obj.x();
// Output: obj
// because the function 'x' is called with 'obj' as the reference


🚀 Important Points:
         When calling obj.x(), JavaScript automatically sets this = obj.
         The value of this always depends on how the method is called, not how or where it is defined.
         If you separate the method from the object and call it independently, this can become undefined (in strict mode) or window (in non-strict mode).


❗ Small Warning Example:

const obj = {
  a: 10,
  x: function () {
    console.log(this);
  }
};

const y = obj.x;
y(); 
// Output: undefined (in strict mode) 
// because now 'y' is a normal function call, no object reference


✅ Final Interview Answer:
"If a function is part of an object, it is called a method.
When a method is called using the object, the value of this refers to the object.
this depends on how the method is invoked, not where it is defined."




Question:- what is method borrowing? (call, apply, bind)
--------------------------------------------------------


✅ this with call(), apply(), and bind() — (Interview Notes)

lll What is Method Borrowing?
     In JavaScript, you/we can reuse a method of one object for another object by explicitly setting this.
     We use call(), apply(), or bind() to control what this should point to.


lll🧠 call() Method
    call() immediately invokes the function, and you/we manually pass the value of this as the first argument.
    Arguments are passed one-by-one (comma-separated).


const obj1 = {
  name: "Deepanshu",
  greet: function (city) {
    console.log(`Hello, I'm ${this.name} from ${city}`);
  }
};

const obj2 = { name: "Singh" };

obj1.greet.call(obj2, "Delhi");
// Output: Hello, I'm Singh from Delhi


lll 🧠 apply() Method
     apply() is similar to call(), but arguments are passed as an array.

obj1.greet.apply(obj2, ["Noida"]);
// Output: Hello, I'm Singh from Noida


lll 🧠 bind() Method
     bind() does NOT immediately invoke the function.
     It returns a new function with this permanently set to the value you provide.
     You have to call the returned function manually.

const newFunc = obj1.greet.bind(obj2, "Gurgaon");
newFunc();
// Output: Hello, I'm Singh from Gurgaon




example(2)

let name = {
    firstName: "Deepanshu",
    lastName: "Singh",
};

let printFullName = function (hometown, state) {
    console.log(this.firstName + " " + this.lastName + " from " + hometown + ", " + state);
};

// Using call()
printFullName.call(name, "Dehradun", "Uttarakhand");
// Output: Deepanshu Singh from Dehradun, Uttarakhand

let name2 = {
    firstName: "Sachin",
    lastName: "Tendulkar",
};

// Borrowing the function with call()
printFullName.call(name2, "Mumbai", "Maharashtra");
// Output: Sachin Tendulkar from Mumbai, Maharashtra


// Correct way with apply()
printFullName.apply(name2, ["Mumbai", "Maharashtra"]);
// Output: Sachin Tendulkar from Mumbai, Maharashtra

// Using bind()
let printMyName = printFullName.bind(name2, "Mumbai", "Maharashtra");
printMyName();
// Output: Sachin Tendulkar from Mumbai, Maharashtra




📊 Summary Table:

    Method	         Calls Immediately?	        Arguments Style         	Returns
    call	           ✅ Yes	                   Comma separated	         Nothing
    apply	           ✅ Yes	                   Array	                   Nothing
    bind	           ❌ No (returns fn)	       Comma separated	         Function


    
✅ Final Interview Answer:
"In JavaScript, call, apply, and bind are used to control the value of this manually.
call() and apply() invoke the function immediately, whereas bind() returns a new function where this is permanently set."




Question:- What is value of this inside an arrow function?
----------------------------------------------------------


✅ this Inside Arrow Functions – (Interview Notes)

lll 🧠 Core Concept:
      Arrow functions do not have their own this.
      Instead, they inherit this from their enclosing lexical context (i.e., the outer scope where they are defined).

lll 🧠 What is Lexical Context?
      Lexical context simply means:
      "Where the function is physically written in the code."


Arrow functions capture this from the nearest non-arrow function or global context.

📌 Example:

const obj = {
  a: 10,
  x: () => {
    console.log(this);
  }
};

obj.x();

📌 Output:
Window (in browser) 
or
Global (in Node.js)


🧠 Why?
Because arrow functions don't bind their own this.
this inside x points to the outer scope, not to obj.
In this case, the outer scope is the global space.

✅ Interview Final One-Liner:
"Arrow functions do not create their own this; they inherit it from the lexical (outer) scope."



example(2)

const obj = {
  a: 10,
  x: function () {
    const y = () => {
      console.log(this);
    };
    y();
  }
};

obj.x();

✅ Step-by-Step Breakdown:

1. obj.x() is called.
obj is the object.

x is a normal function (not an arrow function).

2. Inside x(), we define y as an arrow function.
Arrow functions don't have their own this.

So, y will inherit this from its surrounding (lexical) scope.

3. What is the lexical scope for y()?
It’s the x() function.

4. What is the value of this inside x()?
Because x() is called as obj.x(),
the value of this inside x() is obj.

5. So what is the value of this inside y()?
y() inherits this from x(), which is obj.


6. Final Output:
obj
It will print the obj itself.

✅ This shows that arrow functions inherit this from the nearest normal function around them.






Question:- What is value of this inside DOM event handlers?
-----------------------------------------------------------


🧠 How this behaves inside DOM event handlers?
When a function is triggered as an event handler in the browser (like onclick, onmouseover, etc.),

The value of this inside the handler points to the DOM element that received the event.

🎯 Example:

<button onclick="alert(this)">Click me</button>

When you click the button:
    this refers to the <button> element itself.
    alert(this) will show: [object HTMLButtonElement].

📢 Final Interview Line:
"Inside a regular DOM event handler, this refers to the HTML element that fired the event."














Question:- this behavior is different in class and constructor.
---------------------------------------------------------------



*/