import React from 'react'

/*



🔥 1. What is async?
lll The async keyword is used to define a function that always returns a Promise.
lll Even if you/we return a simple value, it is automatically wrapped in a Promise.


async function getData() {
  return "Hello World";
}

getData().then(res => console.log(res)); // Output: Hello World






🔥 2. What is await?
lll await keyword pauses execution inside an async function until the Promise resolves or rejects.
lll It makes asynchronous code look like synchronous code, improving readability.




async function fetchData() {
  const response = await fetch("https://api.github.com/users");
  const data = await response.json();
  console.log(data);
}
⚠️ Note: await only works inside async functions.





🔥 3. How async/await works behind the scenes?
async functions return a Promise.
When await is used, JS engine:
Suspends the execution of the current async function.
Moves to other tasks (non-blocking).
Resumes execution after the Promise resolves.

lll:- It's syntactic sugar over .then() and .catch() chaining.





🔥 4. Async function vs Normal function
Normal Function	                       Async Function
Returns a value	                       Always returns a Promise
No automatic promise wrapping	         Non-promise return values get wrapped in a Promise

Example:

function normal() {
  return "hello";
}

async function asyncFunc() {
  return "hello";
}

console.log(normal());         // "hello"
console.log(asyncFunc());      // Promise { "hello" }





🔥 5. Async/Await Example

const promise = new Promise((resolve) => {
  setTimeout(() => resolve("Data Received"), 2000);
});

async function getData() {
  console.log("Fetching...");
  const data = await promise;
  console.log(data);
}

getData();


Output:

Fetching...
(Data prints after 2 seconds) Data Received






🔥 6. Error Handling with Async/Await
Use try-catch to handle errors:

async function getData() {
  try {
    const res = await fetch("https://invalid-url.com");
    const data = await res.json();
    console.log(data);
  } catch (error) {
    console.log("Error occurred:", error);
  }
}

getData();




🔥 7. lll How is it better than .then() and .catch()?
✅ Async/await provides cleaner, more readable code.
✅ Removes deep .then() chaining (Callback Hell).
✅ Easy error handling with try-catch.




Example Comparison:

// With .then()
fetch(url)
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.log(err));

// With async/await
async function getData() {
  try {
    const res = await fetch(url);
    const data = await res.json();
    console.log(data);
  } catch (err) {
    console.log(err);
  }
}



🔥 8. lll Behind the Scenes: Call Stack and Event Loop
await pauses only the function, not the entire program.
While waiting for the Promise to resolve: Other code runs (Event Loop continues).
Once resolved:Resumed execution is added back to the Call Stack.






🔥 9. Real-Time Example: Parallel Promises

const p1 = new Promise((resolve, reject) => setTimeout(() => resolve("P1 Done"), 3000));
const p2 = new Promise((resolve, reject) => setTimeout(() => resolve("P2 Done"), 2000));

async function getData() {
  console.log("Start");

  const res1 = await p1;   // Waits 3 sec
  console.log(res1);

  const res2 = await p2;   // Already resolved after 2 sec, but printed after p1
  console.log(res2);

  console.log("End");
}

getData();
Tip: Use Promise.all to run them truly parallel if needed.






🔥 10. Interview Conclusion
Q: What is async/await?
A modern way to handle Promises, making async code readable and structured like synchronous code.

Q: Async function vs Normal function?
Async function always returns a Promise; normal functions don't.

Q: Is async/await better than .then()?
Yes, more readable, but both depend on use case.







*/



const AsyncAwait = () => {
  return (
    <div><h1>AsyncAwait</h1></div>
  )
}

export default AsyncAwait