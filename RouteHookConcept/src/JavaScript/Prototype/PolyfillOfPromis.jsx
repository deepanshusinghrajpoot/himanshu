import React from 'react'



/*

✅ Let's Clarify Step by Step:


✅ 1. Resolve with asynchronous function:

new Promise((resolve, reject) => {
  setTimeout(() => resolve("resolved"), 1000);
}).then((res) => console.log("Then:", res));
🟢 Correct Understanding:
.then() runs after the asynchronous resolve() call is executed. ✅









❌ 2. Resolve synchronous task:

new Promise((resolve, reject) => {
  resolve("immediate");
}).then((res) => console.log("Then:", res));

🟡 Correction Needed:
Even if resolve() is called synchronously, the .then() block will NOT run immediately. It is still queued in the microtask queue.
that mean first execute resolve(val);









✅ Native Promises are always asynchronous, even when resolved immediately.
So, the .then() executes after the current call stack is cleared.


✅ 3. Reject with asynchronous function:

new Promise((resolve, reject) => {
  setTimeout(() => reject("error"), 1000);
}).catch((err) => console.log("Catch:", err));


🟢 Correct. .catch() executes when the asynchronous rejection happens. ✅









❌ 4. Reject with synchronous task:

new Promise((resolve, reject) => {
  reject("immediate error");
}).catch((err) => console.log("Catch:", err));


🟡 Correction Needed:
Even with a synchronous reject(), .catch() doesn't execute immediately.
Like .then(), .catch() also runs in the microtask queue, after the current stack finishes.


*/








const PolyfillOfPromis = () => {



function PromisMyPolyFill(executor){

     let onResolve,
         onReject,
         isFullfilled = false,
         isRejected = false, 
         isCalled = false,
         value;



    function resolve(val){

        isFullfilled = true;
        value = val;

        if(typeof onResolve === "function"){
            isCalled = true;
            onResolve(val);
        }
        
    }



     function reject(val) {

         isRejected = true;
         value = val;

         if(typeof onReject  === "function"){
             isCalled = true;
             onReject(val);
         }
     }



    this.then = function (callback) {
         
        onResolve = callback;

        if(isFullfilled && !isCalled){
            isCalled = true;
            onResolve(value);
        }


        return this;
    }



    this.catch = function (callback) {

        onReject = callback;

        if(isRejected && !isCalled){
             isCalled = true;
             onReject(value);
        }

        return this;
    }


    try{
        executor(resolve, reject);
    }
    catch(err){
        reject(err);
    }

}




let myPromis = new PromisMyPolyFill((resolve, reject) => {

    setTimeout(()=>{
        resolve(5000)
    },5000)

})



myPromis.then((res) => console.log("success :- ", res))
        .catch((err) => console.log("error :- ", err));



  return (
    <div><h1>PolyfillOfPromis</h1></div>
  )

}

export default PolyfillOfPromis