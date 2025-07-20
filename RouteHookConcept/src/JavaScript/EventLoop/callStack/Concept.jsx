
/*

lll    "JavaScript is single-threaded, meaning it has only one call stack, and it can execute one piece of code at a time. 
    However, it can handle asynchronous operations efficiently using a mechanism called the Event Loop, along with the callback queue 
    and Web APIs (in browsers) or libuv (in Node.js)."

lll ✅ Correct Explanation:
     ✔ JavaScript is a loosely typed (or weakly typed) language, 
     
     meaning:   
              Variables are not bound to a specific data type
              We can assign different types of values to the same variable at different times

              var a;
              console.log(a);  // undefined

              a = 10;
              console.log(a);  // 10 (number)

              a = "Deepanshu Singh";
              console.log(a);  // "Deepanshu Singh" (string)




    📦 APIs in the Browser

   🔹 What Are Web APIs?
lll      Web APIs are built-in features provided by the browser, not JavaScript itself. They allow developers to:

           Make network requests (fetch)
           Set timers (setTimeout)
           Manipulate the DOM (document.querySelector)
           Store data (localStorage)
           Access location, console, events, and more.

   🔍 Clarifying JavaScript vs Web APIs
        "JavaScript alone doesn’t have built-in capabilities for tasks like timers, DOM manipulation, or HTTP requests. 
        These features are provided by the browser’s environment, specifically through Web APIs, which JavaScript accesses to perform 
        asynchronous and interactive operations."

   🌐 window, Web APIs & Global Objectg
        In the browser environment, the JavaScript engine itself does not contain features like setTimeout, fetch, or document. 
        Instead, the browser provides these features through a global object called window.

                window is the global object in the browser, and it exposes all Web APIs to JavaScript.

                Features like console, document, location, and localStorage are accessible via window.

    When JavaScript code runs, it has automatic access to the window object, so these features are globally available even without writing window. explicitly.

   ✅ Examples:

           setTimeout(() => console.log("Hi!"), 1000);
           // same as
           window.setTimeout(() => console.log("Hi!"), 1000);

           console.log(location.href); // uses window.location.href


    
           
    -------- libuv(in browser)

lll    "libuv is a C-based library used by Node.js to implement its event loop and handle asynchronous I/O operations like file access, networking, and timers.

    It gives Node.js the ability to perform non-blocking I/O by delegating heavy or blocking tasks to a background thread pool, while the main JavaScript thread stays responsive. 
    This is what enables Node.js to be single-threaded but still highly performant and asynchronous under the hood.

    libuv essentially acts as the runtime layer that abstracts away OS-specific APIs and provides a consistent, efficient event-driven model to Node.js."








*/