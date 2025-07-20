import React from 'react'



/*

✅ What is a Polyfill?
✔ lll  Ployfill are basically our won implementation of an inbuild function in javaScript
✔ lll  A Polyfill is code that adds missing functionality in older browsers by providing your/our own implementation for methods that may not exist natively.
✔ It's often used to replicate modern JavaScript features in environments that don't support them.





lll Example: Writing your own bind() method if the browser doesn't support it.   


✅ Polyfill for bind() — Step-by-Step Interview Approach

Requirement
             bind() creates a copy of a function
             Sets the this context
             Allows preset arguments
             Supports additional arguments during function call




✅ Basic Example

let name = {
    firstName: "Deepanshu",
    lastName: "Singh",
};

let printName = function () {
    console.log(`${this.firstName} ${this.lastName}`);
};

let printMyName = printName.bind(name);
printMyName();  // Output: Deepanshu Singh



✅ Step 1: Basic Polyfill

Function.prototype.mybind = function (...args) {
    let obj = this;
    return function () {
        obj.call(args[0]);
    };
};




Limitation: Cannot handle arguments passed to mybind() or the returned function.


✅ Step 2: Handle Arguments to mybind()

Function.prototype.mybind = function (...args) {
    let obj = this;
    let params = args.slice(1);

    return function () {
        obj.apply(args[0], params);
    };
};
✔ Supports preset arguments:

let printName = function (hometown) {
    console.log(`${this.firstName} ${this.lastName} from ${hometown}`);
};

let printMyName = printName.mybind(name, "Gorakhpur");
printMyName();  // Output: Deepanshu Singh from Gorakhpur






✅ Step 3: Handle Arguments During Function Call
✔ Final working polyfill:

Function.prototype.mybind = function (...args) {
    let obj = this;
    let params = args.slice(1);

    return function (...args2) {
        obj.apply(args[0], [...params, ...args2]);
    };
};
✔ Now fully supports preset and runtime arguments:

let printName = function (hometown, state) {
    console.log(`${this.firstName} ${this.lastName} from ${hometown}, ${state}`);
};

let printMyName = printName.mybind(name, "Gorakhpur");
printMyName("Uttar Pradesh");  
// Output: Deepanshu Singh from Gorakhpur, Uttar Pradesh







✅ Final Interview Notes
✔ Polyfill mimics missing native methods for compatibility
✔ bind() polyfill sets this context and handles both preset and runtime arguments
✔ This demonstrates deep understanding of:
✔️ call() and apply()
✔️ Function context
✔️ Closures
✔️ Spread operator






*/


/*










let name = {
    firstName:"Deepanshu Singh",
    dist:"Gorakhpur",
}


function xyz(state, salary) {
    console.log(`${this.firstName} - ${this.dist} - ${state} - ${salary}`);
}



✅ Polyfill for call method 


Function.prototype.myCall = function (context = {}, ...args){
    if (typeof this !== "function") {
        throw new Error(this + " is not callable");
    }

    context.fn = this;
    context.fn(...args);
    delete context.fn;  // ✅ cleanup
};


console.log("Polyfil of call method");
xyz.myCall(name, "Uttar Pardesh", "100000000");





✅ Polyfill for apply method 

Function.prototype.myApply = function (context = {}, args = []) {
    if (typeof this !== "function") throw new Error(this + " is not callable");
    if (!Array.isArray(args)) throw new TypeError("Create list from array-like object");

    context.fn = this;
    context.fn(...args);
    delete context.fn;  // ✅ cleanup
};


console.log("Polyfil of apply method");
xyz.myApply(name, ["Uttar Pardesh" , "2000000000"]);







✅ Polyfil for bind method  

Function.prototype.myBind = function (context = {}, ...args1) {
    if (typeof this !== "function") throw new Error(this + " can't be bound");

    const self = this;
    return function (...args2) {
        return self.apply(context, [...args1, ...args2]);
    };
};



console.log("Polyfil of bind method");
let x = xyz.myBind(name, "Uttar Pardesh");
x("3000000000");



*/

















const PolyfillOfCallApplyBind = () => {



      let  name = {
           firstName:"Deepanshu",
           lastName:"Singh"
      }


      const print = function (dist, state){
        console.log(`${this.firstName}   ${this.lastName}   ${dist}   ${state}`)
      }


      const printName = print.bind(name, "Gorakhpur");
      printName("Uttar Pardesh");



      Function.prototype.myBind = function (...args) {
         
          let self = this;
          let params = args.slice(1);
          return function (...args2) {
             return self.apply(args[0], [...params, ...args2] );  
          }

      }

      const printName2 = print.myBind(name, "Gorakhpur");
      printName2("Uttar Pardesh");


  return (
    <div><h1>PolyfillOfBindMethod</h1></div>
  )
}

export default PolyfillOfCallApplyBind
