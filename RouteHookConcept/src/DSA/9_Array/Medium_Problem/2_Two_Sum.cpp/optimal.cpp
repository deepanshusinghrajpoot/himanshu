
/*





=========== TWO SUM (HASH MAP – OPTIMIZED) ===========

Problem:
-----------------------------------------------------------
Given an array and a target,
return indices (i, j) such that:

arr[i] + arr[j] = target

-----------------------------------------------------------
⚠️ IMPORTANT BUG IN GIVEN CODE:
-----------------------------------------------------------

map<int,int> mp; ❌ is declared INSIDE the loop

❌ This clears the map on every iteration
❌ Previously stored elements are LOST

-----------------------------------------------------------
✅ CORRECT PLACEMENT:
-----------------------------------------------------------

map<int,int> mp;  → must be OUTSIDE the loop

-----------------------------------------------------------
Correct Code Logic:
-----------------------------------------------------------

• Use Hash Map to store:
  key   → array value
  value → index

• For each element:
  a = arr[i]
  b = target - a

• Check if b already exists in map
• If YES → pair found
• If NO  → store a in map

-----------------------------------------------------------
Algorithm Flow:
-----------------------------------------------------------

1️⃣ Create empty map mp
2️⃣ Traverse array from left to right
3️⃣ For each element:
    • a = arr[i]
    • b = target - a
4️⃣ If mp contains b
    → return { mp[b], i }
5️⃣ Else store:
    mp[a] = i
6️⃣ If no pair found → return {-1, -1}

-----------------------------------------------------------
Example:
-----------------------------------------------------------

Array: [2, 7, 11, 15]
Target = 9

i = 0 → a = 2, b = 7
Map = {2:0}

i = 1 → a = 7, b = 2
✔ 2 found in map

Answer:
Indices = (0, 1)

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------

O(N × log N)

-----------------------------------------------------------
Why O(N × log N)?
-----------------------------------------------------------

• Loop runs N times
• Each map operation (find / insert) = O(log N)
• Total = N × log N

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------

O(N)
→ Hash map stores up to N elements

-----------------------------------------------------------
Valid For:
-----------------------------------------------------------

✔ Positive numbers
✔ Negative numbers
✔ Zero values
✔ Unsorted array

-----------------------------------------------------------
Why This Is Better Than Brute Force?
-----------------------------------------------------------

• Brute Force → O(N²)
• Hash Map     → O(N log N)

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------

"Using a hash map reduces Two Sum from O(N²)
to O(N log N) by trading space for time."

===========================================================








*/






#include<bits/stdc++.h>
using namespace std;



vector<int>two_sum(vector<int>&arr, int target){

    for(int i=0; i<arr.size(); i++){

        int a = arr[i];
        int b = target - a;

        map<int,int>mp;

        if(mp.find(b) != mp.end()){
            return {mp[b], i};
        }

        mp[a] = i;
    }


    return {-1, -1};
}




int main(){

    vector<int>arr{3, 4, 2, 5, 6, 0, 8, 9};

    cout<<"Two Sum Problem :- ";
    vector<int>ans = two_sum(arr, 12);
    for(int i=0; i<ans.size(); i++){
        cout<<ans[i]<<" ";
    }

    return 0;
}