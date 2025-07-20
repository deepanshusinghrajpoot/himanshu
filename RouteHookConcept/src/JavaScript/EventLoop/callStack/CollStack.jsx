import React from 'react'


const CollStack = () => {

/*     
      ✅ Interview-Ready: JavaScript Execution Context & Call Stack
          🧠 "When any JavaScript code runs, the JavaScript engine first creates a Global Execution Context (GEC). 
           This GEC is then pushed onto the Call Stack."

          ✨ "The Global Execution Context has two main phases:

           Memory Creation Phase (Hoisting Phase) – All variables and function declarations are stored in memory with initial values (undefined for variables, full definition for functions).

           Code Execution Phase – The code is executed line-by-line, and values are assigned or computed."

          🔁 "Every time a function is invoked, a new Execution Context is created for that function and pushed onto the Call Stack. When the function finishes execution, its context is popped off the stack, 
          returning control to the previous context."



       🧪 JavaScript Execution Context with Call Stack – Full Example
          👉 Sample Code:

                 var x = 10;

                 function outer() {
                        var y = 20;

                        function inner() {
                              var z = 30;
                              console.log(x + y + z);
                        }

                        inner();
                 }

                 outer();



        🧠 Step-by-Step Execution:

            Step 1: Global Execution Context (GEC)
                  Memory Phase:

                          x → undefined

                          outer → function definition

                  Execution Phase:

                          x = 10 → stored in memory

                          outer() is called → new Execution Context created

            📌 Call Stack now:
                      | outer Execution Context |
                      | Global Execution Context |

            Step 2: outer() Execution Context
                   Memory Phase:

                          y → undefined

                          inner → function definition

                   Execution Phase:

                          y = 20

                          inner() is called → new Execution Context created

            📌 Call Stack now:
                        | inner Execution Context |
                        | outer Execution Context |
                        | Global Execution Context |

            Step 3: inner() Execution Context
                   Memory Phase:

                          z → undefined

                   Execution Phase:

                          z = 30

                          console.log(x + y + z) runs → Output: 60

            ✅ JS looks for:

                  x → not in inner → not in outer → found in global: 10

                  y → found in outer: 20

                  z → found in inner: 30

                 🖨️ So it logs: 10 + 20 + 30 = 60

          📦 Unwinding the Stack:

                  inner() finishes → inner context popped

                  outer() finishes → outer context popped

                  Global context stays till end

          📌 Final Call Stack:
                     (empty – everything has returned)

          🔁 Final Output:
                    60








      ✅ Interview-Ready: Event Loop in JavaScript
 lll      🔄 "The Event Loop is a core mechanism in JavaScript that continuously checks the Call Stack and the Callback Queue."

 lll      👉 "Its primary role is to move pending asynchronous callbacks (like from setTimeout, fetch, or event handlers) from the Callback Queue to the Call Stack – but only when the Call Stack is empty."

          ⌛ "This enables JavaScript to handle asynchronous operations while remaining single-threaded., by deferring non-blocking tasks to the browser's Web APIs and bringing them back via the Event Loop once ready."
   
        

      ✅ Microtask Queue vs Callback Queue – Explained
         🧠 JavaScript uses two main queues to handle asynchronous operations:

          Callback Queue (Macrotask Queue) – for setTimeout, setInterval, DOM events, etc.

          Microtask Queue – for Promises, queueMicrotask(), and MutationObserver.

                     🔄 queueMicrotask() — Manual Microtask Scheduling
                         ✅ What is it?
                         queueMicrotask() is a built-in function in JavaScript that lets you/we manually schedule a callback to run as a microtask, just like .then() of a Promise.

                         🧠 Why use it?
                         To guarantee that a task runs:

                         After the current call stack is cleared

                         Before any macrotasks like setTimeout

                              🚀 Example:
                                        console.log("Start");

                                        queueMicrotask(() => {
                                              console.log("Inside microtask");
                                        });

                                        console.log("End");

                                🖨️ Output:
                                         Start
                                         End
                                         Inside microtask

                                ✅ Why? Because queueMicrotask() waits for the current stack to clear, then runs before timers/events.



                     🧬 MutationObserver — Watching DOM Changes
                            ✅ What is it?
                            MutationObserver is a Web API that lets you observe changes to the DOM (like node additions, attribute changes, etc.) — and runs its callback in the microtask queue.

                            Think of it as a DOM watcher that reacts as soon as a change happens — before other async callbacks.

                            🧠 Use Case:
                            Useful for tracking real-time DOM changes without relying on polling or manual event handling.



         🔄 How They Work with the Event Loop:
    lll    ✔️ Microtask Queue has higher priority than the Callback Queue (Macrotask Queue).

            That means after each task from the Call Stack is completed, the Event Loop will first:

                Check and empty the Microtask Queue, before moving on to the Callback Queue (Macrotask Queue).

                Only when the Microtask Queue is empty will it begin processing tasks from the Callback Queue (Macrotask Queue).
         


          .            .                                 .                          .
          .            .                                 .                          .
          .            .                                 .                          .
          .            .                                 .                          .
          .    Call    .                                 .    Web API               .
          .    Stack   .                                 .                          .
          .            .                                 .                          .
          .            .                                 .                          .
          .            .                                 .                          .
          .            .                                 .                          .
          .            .                                 .                          .
          .            .                                 .                          .
          .            .                                 .                          .
          .            .                                 .                          .
          .            .                                 .                          .
          ..............                                 ............................
                        Microtask Queue
                    ...........................               .    .   
                    .    .     .    .    .    .               .    .
                    . p1 . p2  . p3 .    .    .     <----------    .
                    ...........................                    .
            🔁 EventLoop                                           .
                    ...........................                    .   rgister callback function in web API after done async task pushed to callback queue
                    .    .     .    .    .    .                    .
                    .cb1 .cb2  .cb3 .    .    .     <---------------
                    ...........................  
                          Callback Queue (Macrotask Queue)





    🧪 JavaScript Execution Context with setTimeout – Full Example
           
            console.log("Start");

            setTimeout(() => {
                    console.log("Inside setTimeout");
            }, 5000);

            console.log("End");

        🧠 Step-by-Step Execution Explained
            Step 1: Global Execution Context is Created
                     Memory Phase:

                              All variables and functions are allocated.

                     Execution Phase:

                              Line-by-line execution begins.

        📍 Line-by-line Execution:

                    console.log("Start")
                    → Printed immediately
                    ✅ Output: Start

                    setTimeout(...)
                    → This is not executed by JavaScript directly, it's handed off to the Web API (Timer)

                   🔹 The callback () => console.log("Inside setTimeout") is registered with a timer of 5000ms.

                   🔹 Once the timer finishes, the callback is moved to the Callback Queue.

                    console.log("End")
                    → Printed immediately
                   ✅ Output: End

         Now, the Call Stack is empty, and the Event Loop moves the callback from the Callback Queue into the Call Stack, where it's executed.

        📌 Call Stack Timeline:

                [Start] → Call Stack: console.log("Start")

                [setTimeout] → Sent to Web API → Call Stack continues

                [End] → Call Stack: console.log("End")

                [After delay] → Call Stack is empty → Callback from setTimeout pushed

                [Callback runs] → Call Stack: console.log("Inside setTimeout")

                🔁 Final Output (in Console):
                                  Start
                                  End
                                  Inside setTimeout



    🧪 JavaScript Execution Context with setTimeout – Full Example

                console.log("Start");

                setTimeout(() => {
                      console.log("setTimeout");
                }, 0);

                Promise.resolve().then(() => {
                      console.log("Promise");
                });

                console.log("End");


              🧠 Phase-by-Phase Execution
              🧱 1. Global Execution Context is created
                   Call Stack: Global Execution Context is pushed.

              ▶️ Code starts executing top to bottom:
                  ✅ console.log("Start")
                  Added to Call Stack → executed → logs:
                     Start
                  Call Stack: now empty again after console.log completes.

                  ✅ setTimeout(() => {...}, 0)
                  This goes to the Web APIs environment (not executed immediately).

                  After 0ms delay, its callback is pushed into the Callback Queue (Macrotask Queue).

                  But remember: JavaScript doesn't just run the callback at 0ms—it waits until the Call Stack is empty, and Microtasks are cleared first.

                  ✅ Promise.resolve().then(() => {...})
                  The .then() callback is pushed into the Microtask Queue immediately (no delay).

                  ✅ console.log("End")
                  Added to Call Stack → executed → logs:
                     End

                  Call Stack: now empty.

                  🌀 Event Loop Begins:
                      Now, the Call Stack is empty, so the Event Loop takes over.

                  🥇 1st Priority: Microtask Queue
                   It finds the .then() callback inside the Microtask Queue.

                   Moves it to the Call Stack → executes:
                       Promise

                  🥈 2nd Priority: Callback Queue(Macrotask Queue)
                   Now, it checks the Callback Queue (setTimeout’s callback is there).

                   Moves it to the Call Stack → executes:
                       setTimeout

               📦 Final Output in Console:
                            Start
                            End
                            Promise
                            setTimeout

               💡 Key Concepts to Highlight in Interviews:
                JavaScript is single-threaded but non-blocking, thanks to the Event Loop.

                Microtasks (like Promises) are always executed before macrotasks (like setTimeout).

                setTimeout(..., 0) still waits until all microtasks finish, even with 0ms delay.


    
    🛑 Callback Queue Starvation (a.k.a. Macrotask Starvation)
        ✅ What is it?
lll     Starvation happens when the Callback Queue (Macrotasks) never get a chance to run — because the Microtask Queue keeps getting filled again and again.

        🔁 Why does it happen?
        Because the Event Loop always empties the Microtask Queue before it touches the Callback Queue.

        So if new microtasks are constantly added (e.g., with queueMicrotask() or Promise.then() inside each microtask), the Callback Queue gets ignored… forever!

       🚨 Example of Starvation:

       setTimeout(() => {
            console.log("This will never run!");
       }, 0);

      function repeatMicrotask() {
         queueMicrotask(() => {
            repeatMicrotask();
         });
      }

      repeatMicrotask();
      🧠 What happens?
      The setTimeout() callback goes to the Callback Queue.

      queueMicrotask() keeps scheduling more microtasks.

      The Event Loop never gets a chance to move to the Callback Queue because it's stuck processing microtasks.

      Result: "This will never run!" — ❌ Starved!

     💡 Real-World Implication
     If you're not careful when chaining microtasks (e.g., in recursive promises or observers), you can block user interactions, timers, or network responses — even though JS is non-blocking.

     ✅ How to Avoid Callback Queue Starvation?
     Don’t infinitely schedule microtasks in loops.

     Break up heavy microtask work with setTimeout(..., 0) or requestAnimationFrame().

     Use microtasks for short, quick tasks only.

*/


    // Example of Call Stack in JavaScript
             var x = 10;

             function outer() {
                     var y = 20;

                     function inner() {
                           var z = 30;
                           console.log(x + y + z);
                     }

                     inner();
             }

             outer();


    // Example of Call Stack with setTimeout
             console.log("Start1");
    
             setTimeout(() => {
                    console.log("setTimeout of Call Stack with setTimeout");
             }, 0);
    
             console.log("End1");

    
    // Example of Call Stack with setTimeout and Promise
             console.log("Start2");

             setTimeout(() => {
                   console.log("setTimeout of Call Stack with setTimeout and Promise");
             }, 0);

             Promise.resolve().then(() => {
                   console.log("Promise");
             });

             console.log("End2");



    return (
        <div>
            <h1>Event Loop All question</h1>
        </div>
    )
}


export default CollStack