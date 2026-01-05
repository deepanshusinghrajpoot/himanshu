/*


Great 👍 this is a favorite interview topic.
Let me give you a short and crisp answer + example so you can directly say it.




🔹 Transaction
---------------

A transaction is a sequence of one or more SQL operations performed as a single unit of work. 
Either all operations succeed (commit) or none of them (rollback).


👉 Example: Bank Transfer

Step 1: Deduct ₹1000 from Account A
Step 2: Add ₹1000 to Account B

Both must succeed together → otherwise rollback.


2️⃣ Why are ACID properties important in transactions?

Answer:

“ACID properties are important because they prevent data inconsistency, ensure correctness of transactions, and protect 
the database from partial updates, system crashes, and concurrent access issues.”


🔹 ACID Properties of Transactions
-----------------------------------

A transaction in DBMS is a single logical unit of work.
To make transactions reliable, DBMS follows ACID properties — Atomicity, Consistency, Isolation, and Durability.

lll Atomicity means either all operations happen or none happen.
    For example: if money is deducted from Account A but not added to Account B, the whole transaction is rolled back.

lll Consistency means the database remains in a valid state before and after the transaction.
    For example: the total money in both accounts remains the same before and after transfer.

lll Isolation means transactions run independently without interfering with each other.
    For example: if two people transfer money at the same time, one transaction doesn’t affect the other’s result.

lll Durability means once a transaction is committed, the changes are permanent.
    For example: after a successful transfer, even if the server crashes, the updated balances stay saved.

So, in short — ACID properties ensure every transaction is reliable, consistent, and safe.




*/