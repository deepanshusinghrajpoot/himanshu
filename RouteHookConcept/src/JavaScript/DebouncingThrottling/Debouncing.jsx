import React from 'react'



/*



✅ Debouncing in JavaScript
✔lll Debouncing is a technique used to improve performance by limiting the rate at which a function executes, especially for high-frequency events like:


Search inputs (auto-suggestions)
Window resizing
Button click spamming prevention
Scroll events



✅ Real-life Example for Interviews
Scenario: You’re asked to build a Flipkart-style search bar with auto-suggestions.
✔ lll Typing "laptop" fires API calls after every keystroke — wasteful & poor performance.
✔ Using Debouncing, API calls happen only after typing stops for a fixed time, reducing server load.




✅ Debouncing Definition
lll Debouncing ensures that a function executes only after a specified delay has passed since the last event trigger.

✅ Throttling
Throttling ensures that a function executes at most once in a specified time interval, even if it's triggered continuously


✅ Debouncing Code Example in React
import { useState } from "react";

export default function DebouncingExample() {
    let counter = 0;

    const getData = () => {
        console.log("Fetching Data... ", counter++);
    };

    const debounce = function (fn, delay) {
        let timer;
        return function (...args) {
            const context = this;
            clearTimeout(timer);
            timer = setTimeout(() => {
                fn.apply(context, args);
            }, delay);
        };
    };

    const betterFunction = debounce(getData, 1000);  // Fires after 1 second of pause

    return (
        <input type="text" onKeyUp={betterFunction} placeholder="Search..." />
    );
}

✅ Explanation

✔ getData() simulates an API call
✔ debounce() returns a wrapper function
✔ If the user keeps typing, clearTimeout() prevents function execution
✔ After 1 second pause, getData() runs




✅ Why this and arguments Used
✔ this maintains correct context (useful for methods inside objects)
✔ arguments captures all arguments passed during the event trigger
✔ In modern JavaScript, (...args) is the preferred syntax




✅ Debouncing vs Throttling Quick Difference
Debouncing	                                      Throttling
lll Function fires after delay ends	              lll Function fires at regular intervals
Ideal for Search, Resize, Input fields	          Ideal for Scroll, Mouse movement




✅ Final Interview Statement
"Debouncing controls the rate of function execution, especially for high-frequency events. 
It improves performance by ensuring the function runs only after the user pauses, such as during search auto-suggestions. It's implemented using setTimeout() and clearTimeout() to delay the execution."





*/






const Debouncing = () => {

    let counter = 0;
    const  getData =  function () {
        console.log("counter :- ", counter++ );
    }

  
   
    const debouncing = ( fn, delay) => {
       
       let timer;

       return function (...args) {
          const context = this;
          clearTimeout(timer);

          timer = setTimeout(()=>{
             fn.apply(context, args);
          }, delay)
       }
    }



     
    const betterFunction = debouncing(getData, 1000);
    








  return (
    <div>
        <h1>Debouncing</h1>
        <input type="text"  onKeyUp={betterFunction} placeholder="Search..." />
    </div>
    
  )
}

export default Debouncing