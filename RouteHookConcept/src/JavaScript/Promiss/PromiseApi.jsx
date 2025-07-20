/*

✅ Promise API Full Notes – Interview Level 🚀

1️⃣ Promise.all()
    Use case: Run multiple promises in parallel and wait for all of them to finish successfully.
    If any one fails: It immediately rejects with the error of the first failed promise.


const p1 = new Promise((resolve, reject) => {
  setTimeout(() => resolve("P1 Success"), 3000);
});

const p2 = new Promise((resolve, reject) => {
  setTimeout(() => reject("P2 Failed"), 1000);
});

const p3 = new Promise((resolve, reject) => {
  setTimeout(() => resolve("P3 Success"), 2000);
});

Promise.all([p1, p2, p3])
  .then(res => {
    console.log(res); // Output: [P1 Success, P2 Success, P3 Success]
  })
  .catch(err => {
    console.error(err); // If any promise fails, catch the first error
  });

🧠 Important:
    Result is an array of values if all succeed.
    If any one fails, no array — it immediately goes to .catch().



2️⃣ Promise.allSettled()
       Use case: Run multiple promises in parallel, and wait for all to settle (either success or failure).
       It never fails itself — we always get an array showing status of each promise.


Promise.allSettled([p1, p2, p3])
  .then(res => {
    console.log(res);
  });

🔎 Result looks like:
[
  { status: "fulfilled", value: "P1 Success" },
  { status: "rejected", reason: "P2 Failed" },
  { status: "fulfilled", value: "P3 Success" }
]


🧠 Important:
       Even if some promises fail, you get result for each.
       Good for "show result even if some API failed".



3️⃣ Promise.race()
       Use case: Run multiple promises in parallel, but only care about the first one to settle (resolve OR reject).

Promise.race([p1, p2, p3])
  .then(res => {
    console.log("Winner:", res);
  })
  .catch(err => {
    console.error("Error:", err);
  });

🔎 Behavior:
   Whichever settles first (resolve or reject) — Promise.race() finishes with that. 
   If the first settled promise rejects, then it goes to catch.

   
   
🧠 Important:
   Great for timeouts — "whichever API responds first".



4️⃣ Promise.any()
  Use case: Run multiple promises, but only care about the first successful one (first fulfilled).
  If all promises fail, returns AggregateError.

Promise.any([p1, p2, p3])
  .then(res => {
    console.log("First Success:", res);
  })
  .catch(err => {
    console.error("All failed:", err.errors); // err.errors is an array of all errors
  });

🔎 Behavior:
   First successful promise wins ✅.
   If all promises fail, .catch() runs with a list of errors (AggregateError).


🧠 Important:
   Safer than race() if you only want success and don't care about failures.



⚡ Bonus Tip – Interview Line
✅ Settled means the promise is either fulfilled (success) or rejected (failure) — either way, it has finished.


*/