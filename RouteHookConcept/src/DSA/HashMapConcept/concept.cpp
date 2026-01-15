/*

🔐 Hashing in C++
==================

map<key, value> vs unordered_map<key, value>




1️⃣ map<key, value> mp
-----------------------

📌 Definition

map stores data in key–value pairs
Keys are unique
Internally implemented using a Balanced Binary Search Tree (Red–Black Tree)
Data is stored in sorted order (ascending by key)

📌 Syntax

map<int, int> mp;

⏱ Time Complexity (map)

| Operation | Best     | Average  | Worst    |
| --------- | -------- | -------- | -------- |
| Insert    | O(log n) | O(log n) | O(log n) |
| Search    | O(log n) | O(log n) | O(log n) |
| Delete    | O(log n) | O(log n) | O(log n) |


📌 Reason: Tree height is always log n


🧠 Space Complexity
----------------------
O(n) → stores n key–value pairs

Extra space for tree pointers (left, right, parent)




2️⃣ unordered_map<key, value> ump
===================================

📌 Definition

Stores key–value pairs using Hash Table
Keys are unique
No ordering maintained
Uses hash function to compute index

📌 Syntax

unordered_map<int, int> ump;

⏱ Time Complexity (unordered_map)

| Operation | Best | Average | Worst |
| --------- | ---- | ------- | ----- |
| Insert    | O(1) | O(1)    | O(n)  |
| Search    | O(1) | O(1)    | O(n)  |
| Delete    | O(1) | O(1)    | O(n)  |


📌 Worst case O(n) happens due to hash collision








📘 map – Important Concepts (C++)
===================================

1️⃣ Find Element
--------------------

mp.find(key) != mp.end()


✔ Key present in map
❌ Key not present if equals mp.end()
⏱ O(log n)



2️⃣ Frequency Count
----------------------
mp[key]++;


Creates key if not present (default 0)

Increments value by 1
⏱ O(log n)



3️⃣ Iteration
----------------
for(auto it : mp){
  cout << it.first << " -> " << it.second << endl;
}


first → key
second → value

Output is sorted by key
⏱ O(n)


*/