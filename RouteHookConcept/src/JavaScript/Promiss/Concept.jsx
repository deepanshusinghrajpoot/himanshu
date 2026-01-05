/*

Question: What is callback and what issues of cllback?
------------------------------------------------------

✅ what is callback?
lll when a function is pass as an argument to another function, it is called a callback.

✅ Importance of Callbacks
Callbacks are a super powerful way of handling asynchronous operations in JavaScript.
lll Asynchronous programming exists because callbacks exist.
They allow JavaScript to continue running without blocking the main thread while waiting for operations like:
            Server requests
            File loading
            Timers
            User events
      👉 Without callbacks, JavaScript would not be able to do async programming.


❌ Issues with Callbacks

1. Callback Hell
lll When many callbacks are nested inside each other.

Code becomes:
    Difficult to read
    Difficult to maintain
    Difficult to debug

This structure is also called the "Pyramid of Doom."
Here, the code growing horizontaly


✅ Example of callback hell:

createOrder(cart, function (orderId) {
  proceedToPayment(orderId, function (paymentInformation) {
    showOrderSummary(paymentInformation, function () {
      updateWalletBalance();
    });
  });
});


2. Inversion of Control
lll When we pass a callback function to another function, we give control to that function.

Now we don't control:
     When the callback will be executed
     Whether the callback will be executed
     How many times the callback will be called
  
It can cause bugs if the other function misbehaves.

✅ Simple Example:

function fetchData(callback) {
  setTimeout(() => {
    const data = { name: "Deepanshu" };
    callback(data); // What if this line is forgotten? You lose control.
  }, 1000);
}


🎯 Final Interview Summary:
"Callbacks are essential for async programming in JavaScript, but they can create problems like Callback Hell and Inversion of Control."





question: catch the soul of the promises?
-----------------------------------------

✅ What are Promises?
  lll Promises are used to handle asynchronous operations in JavaScript.
  lll Promise is simply an object that represents the eventual completion (or failure) of an async operation and its resulting value.


🚀 How things worked before Promises (Callback Style)

const cart = ["shoes", "pants", "kurta"];

createOrder(cart, function (orderId) {
    proceedToPayment(orderId);
});

Here, createOrder takes a callback function.
After the order is created, it calls the callback and passes the orderId.



❌ Problem:
    We have no control over when or how createOrder will call the callback.
    Inversion of control happens: We hand over the callback, and pray it gets called correctly.


🌟 How things work after Promises (Promise Style)

const cart = ["shoes", "pants", "kurta"];

const promise = createOrder(cart); 
// createOrder() now returns a Promise object

promise.then(function (orderId) {
    proceedToPayment(orderId);
});

✅ Now:
  createOrder immediately returns a Promise object.
  We attach the next steps (then) to the Promise.
  No need to pass the callback manually inside createOrder.
  You keep control of what happens after the Promise resolves.
  Promise holds the data internally until it’s ready:

Initial State: { data: undefined }
After successful operation: { data: orderId }
If failed: Promise goes to a rejected state.


🎯 Final Interview Summary:
"Promises solve the problems of callbacks by giving us better control over async flows and avoiding inversion of control. 
They make async code look cleaner, more manageable, and predictable."




✅ Real Example of Promises in Action

const GITHUB_API = "https://api.github.com/users/akshaymarch7";
const user = fetch(GITHUB_API);

// When you apply a debugger or inspect `user`, you will see:
{
  [[Prototype]]: Promise,
  [[PromiseState]]: "pending",
  [[PromiseResult]]: undefined
}

// The Promise is still pending at the time of fetching.

console.log(user); // Prints a Promise object

// Now attach a .then() to handle the resolved data:
user.then(function (data) {
  console.log(data);
});

🧠 Important Points:

When you call fetch, it immediately returns a Promise.
Initially, the Promise is in "pending" state.
Once the API call succeeds, the Promise moves to "fulfilled" (resolved) state and then() gets called with the response data.

✅ Callback Hell Problem
Before Promises, chaining multiple async tasks with callbacks used to look like this 👇

createOrder(cart, function (orderId) {
  proceedToPayment(orderId, function (paymentInformation) {
    showOrderSummary(paymentInformation, function () {
      updateWalletBalance();
    });
  });
});

⚠️ Problems with Callback Hell:

Code becomes nested, ugly, and hard to maintain.
It’s difficult to handle errors properly.
Logic becomes tightly coupled and hard to reuse.



✅ Callback Hell problem solving with Promises (Promise Chaining)
Now with Promises, we avoid the deep nesting:

createOrder(cart)
.then(function (orderId) {
  return proceedToPayment(orderId);             // return is important here
})
.then(function (paymentInformation) {
  return showOrderSummary(paymentInformation);
})
.then(function (paymentInformation) {
  return updateWalletBalance(paymentInformation);
})
.catch(function (error) {
  console.log(error); // Always handle errors at the end
});



🎯 Advantages:
      Code is flat, clean, and readable.
      Easy error handling with .catch().
      Functions are more independent and reusable.

🎯 Final Interview Statement:
"Promises help avoid callback hell by allowing cleaner chaining of async operations and giving better control over error handling and code structure."








*/




import React from "react";


const Concept = () => {

          const cart = ["shoes", "pants", "kurta"];

          const promise = createOrder(cart);

          promise
               .then(function (orderId) {
                     console.log("Order ID:", orderId);
                     return orderId;
               })
               .then(function (orderId) {
                     return proceedToPayment(orderId);
               })
               .then(function (paymentInfo) {
                     console.log(paymentInfo);
               })
               .catch(function (err) {
                     console.log(err.message);
               });
               



// lll How to create our won promise
//------------------------------------
// Create Order function
function createOrder(cart) {
  return new Promise(function (resolve, reject) {
    if (!validateCart(cart)) {
      const err = new Error("Cart is not valid");
      reject(err);
    }
    const orderId = "12345";
    setTimeout(function () {
      resolve(orderId);
    }, 5000); // simulate async operation
  });
}

// Proceed to Payment function
function proceedToPayment(orderId) {
  return new Promise(function (resolve, reject) {
    resolve("Payment Successful for Order ID: " + orderId);
  });
}

// Validate Cart function
function validateCart(cart) {
  return true; // assume cart is always valid
  // return false
}


  return (
    <div>
      <h1>Promise</h1>
    </div>
  )
}


export default Concept;