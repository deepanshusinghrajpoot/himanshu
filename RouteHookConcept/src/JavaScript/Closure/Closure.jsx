import React from 'react'



/*

✅ Closure — Perfect Definition
✔ "A Closure is created when a function remembers its lexical environment even after the outer function has finished executing."
OR
✔ lll "Function along with its lexical environment forms a Closure."


✅ Basic Example of Closure

function x() {
    var a = 7;
    function y() {
        console.log(a);  // `y` remembers `a` even after `x` is done
    }
    y();
}
x();

✅ Closure with Return

function x() {
    var a = 7;
    function y() {
        console.log(a);
    }
    return y;  // returns the closure (function y along with its lexical scope)
}

var z = x();   // `z` now holds function `y` with access to `a`
console.log(z);  // prints function definition
z();  // prints 7

lll:- Even though x() has finished, y() remembers a due to closure.



✅ Closure with Multiple Scopes Example

function z() {
    var b = 900;
    function x() {
        var a = 7;
        function y() {
            console.log(a, b);  // y has access to both a and b
        }
        y();
    }
    x();
}
z();
✔ y() can access both a (from x) and b (from z) due to the Closure chain.



✅ Common Uses of Closures
✔ Module Design Pattern (private variables)
✔ Currying                      lll
✔ Memoization (caching results)     lll
✔ setTimeout callbacks           lll
✔ Functions like once
✔ Maintaining state in asynchronous code
✔ Iterators and Generators
✔ Event Listeners


✅ Simple Interview-Ready Statement
"Closure means function remembers variables from its parent scope even if the parent function has finished execution. 
It happens due to Lexical Environment and Scope Chain."








-------------------------------------------------------------------------------------------------------------------


✅ Famous setTimeout Closure Interview Question
Example with var (Incorrect Output due to Closure with Shared Reference):

function x() {
    for (var i = 1; i <= 5; i++) {
        setTimeout(function () {
            console.log(i);
        }, i * 1000);
    }
    console.log("Hello Dunia");
}
x();

Output:
Hello Dunia
6
6
6
6
6
✅ Why 6 Prints?
✔ var is function-scoped, not block-scoped.
✔ By the time the callbacks run (after 1s, 2s, ...), the loop is already finished, and i = 6.
✔ All 5 callbacks share the same reference of i.
✔ So, 6 prints every time.

✅ Correct Solution Using let (Block Scoped):

function x() {
    for (let i = 1; i <= 5; i++) {
        setTimeout(function () {
            console.log(i);
        }, i * 1000);
    }
    console.log("Hello Deepanshu");
}
x();


Output:
Hello Deepanshu
1
2
3
4
5
✔ let is block-scoped, so each iteration creates a new copy of i.
✔ Each callback gets a separate i value due to new block scope.






✅ Smart Interviewer Challenge — Solve with var using Closure:
Closure creates a new copy of i for each iteration.

function x() {
    for (var i = 1; i <= 5; i++) {
        (function close(x) {
            setTimeout(function () {
                console.log(x);
            }, x * 1000);
        })(i);
    }
    console.log("Hello Himanshu");
}
x();
✅ Why It Works?
✔ IIFE (close function) is invoked immediately with i as an argument.
✔ Each close(x) creates a new execution context with a separate copy of x.
✔ Closure preserves this copy until the setTimeout callback executes.
✔ Hence, 1, 2, 3, 4, 5 print with 1-second intervals.

✅ Perfect Interview Conclusion:
"We use closures here to capture a fresh copy of the variable during each iteration. This avoids the shared reference problem caused by var and lets us achieve the same output as block-scoped let."







-------------------------------------------------------------------------------------------------------------------

✅ Important Closure Example

function outest() {
    var c = 20;
    function outer(b) {
        let a = 10;
        function inner() {
            console.log(a, b, c);
        }
        return inner;
    }
    return outer;
}

var close = outest()("Hello World");
close();  // Output: 10 "Hello World" 20
✔ Even after outer and outest finish execution, inner() remembers variables a, b, c — this is Closure.




✅ Advantages of Closure
✔ Function Currying
✔ Memoization
✔ Data Hiding / Encapsulation
✔ Maintaining state in async operations (setTimeout, callbacks)




✅ What is Data Hiding with Closure?
Data Hiding means restricting direct access to variables, exposing only controlled behavior via functions.

Example of Data Hiding

function counter() {
    var count = 0;
    return function incrementCounter() {
        count++;
        console.log(count);
    };
}

var counter1 = counter();
counter1();  // 1
counter1();  // 2

var counter2 = counter();
counter2();  // 1
counter2();  // 2
✔ count is private — cannot access directly:


console.log(count);  // ReferenceError
✔ Only incrementCounter() can modify count — this is Data Hiding.

✅ Object-Oriented Style with Closure

function Counter() {
    var count = 0;
    
    this.incrementCounter = function () {
        count++;
        console.log(count);
    };

    this.decrementCounter = function () {
        count--;
        console.log(count);
    };
}

var counter1 = new Counter();
counter1.incrementCounter();  // 1
counter1.incrementCounter();  // 2
counter1.decrementCounter();  // 1
✔ Private count accessible only through defined methods.
✔ Combines Closure with Constructor pattern.



✅ Disadvantages of Closure
✔ Overuse of closures can lead to memory overconsumption.
✔ Variables captured by closure are not garbage collected as long as the closure exists.

✅ What is Garbage Collector?
✔ Automatic memory management by the JS engine.
✔ Frees up memory that is no longer reachable in code.

Example:

function a() {
    var x = 0;
    return function b() {
        console.log(x);
    };
}

var y = a();
✔ Here, x is kept in memory because b() still uses it (closure), so Garbage Collector can't free x.
✔ If no references to the closure exist, memory is freed:

var y = null;  // Now closure is unreachable, memory is cleared

✅ Final Interview-Ready Statements
Closure: Function + its lexical environment.
Data Hiding: Using closures to keep variables private and only expose required operations.
Garbage Collector: Frees unused memory; closures delay GC if variables are still referenced.




*/

const Closure = () => {
  return (
    <div><h1>Closure</h1></div>
  )
}

export default Closure