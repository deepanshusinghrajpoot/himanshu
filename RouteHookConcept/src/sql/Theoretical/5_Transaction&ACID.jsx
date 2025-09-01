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





🔹 ACID Properties of Transactions
-----------------------------------

Atomicity → All operations of a transaction are completed or none are applied.
Example: If money is deducted from A but not added to B → rollback.


Consistency → Transaction takes the database from one valid state to another valid state.
Example: Total money before and after transfer remains the same.


Isolation → Transactions are executed independently without interference.
Example: Two people transferring money at the same time won’t affect each other’s result.


Durability → Once a transaction is committed, the changes are permanent even after system failure.
Example: After transfer is successful, the updated balances remain even if server crashes.


👉 Interview Short Answer:
“A transaction is a unit of work in DBMS. ACID properties ensure it is reliable: Atomicity (all or none), Consistency (valid state), Isolation (no interference), and Durability (permanent changes).”





*/