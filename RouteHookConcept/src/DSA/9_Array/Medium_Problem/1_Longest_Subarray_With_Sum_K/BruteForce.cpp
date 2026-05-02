/*



=========== LONGEST SUBARRAY WITH SUM K (BRUTE FORCE) ===========

Definition:
Find the LENGTH of the longest subarray
whose elements sum up to exactly K.

-----------------------------------------------------------
Approach Used:
-----------------------------------------------------------
Brute Force using Nested Loops

-----------------------------------------------------------
Core Idea:
-----------------------------------------------------------
• Fix a starting index i
• Keep adding elements from i to j
• Check sum for every subarray
• If sum == K → update maximum length

-----------------------------------------------------------
Algorithm Steps:
-----------------------------------------------------------
1️⃣ Initialize maxLen = 0

2️⃣ For each index i from 0 to N-1:
   • Initialize sum = 0

3️⃣ For each index j from i to N-1:
   • sum += arr[j]
   • If sum == K:
       maxLen = max(maxLen, j - i + 1)

4️⃣ Return maxLen

-----------------------------------------------------------
Array Type Validity:
-----------------------------------------------------------
✔ Works for POSITIVE elements
✔ Works for NEGATIVE elements
✔ Works for ZERO values
✔ Works for MIXED arrays

(Reason: Every possible subarray is checked)

-----------------------------------------------------------
Example:
-----------------------------------------------------------
Array = [1, -1, 5, -2, 3]
K = 3

Valid Subarrays:
[1, -1, 5, -2] → sum = 3 → length = 4
[5, -2]        → sum = 3 → length = 2

-----------------------------------------------------------
Final Answer:
-----------------------------------------------------------
Longest Length = 4

-----------------------------------------------------------
Why This Works:
-----------------------------------------------------------
All subarrays are explicitly evaluated,
so sign of elements does not matter.

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N²)

-----------------------------------------------------------
Where does O(N²) come from?
-----------------------------------------------------------
• Outer loop runs N times
• Inner loop runs up to N times
• Nested loops → N × N

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(1)

-----------------------------------------------------------
Drawback:
-----------------------------------------------------------
Slow for large N due to repeated sum calculation

-----------------------------------------------------------
Optimized Approach:
-----------------------------------------------------------
• Prefix Sum + HashMap
• Time Complexity → O(N)
• Valid for positive, negative, and zero values

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------
"Brute force works for any type of array
but costs O(N²) time."

===========================================================




*/









#include<bits/stdc++.h>
using namespace std;


int longest_subarray_with_sum_k(vector<int>&arr, int k){

    int maxLen = 0;

    for(int i=0; i<arr.size(); i++){
        int sum = 0;
        for(int j=i; j<arr.size(); j++){
            sum += arr[j];
            if(sum == k) maxLen = max(maxLen, j-i+1);
        }
    }

    return maxLen;
}



int main(){


    vector<int>arr{9, 4, 3, 5, 6, 7, 0, 1};

    cout<<"Longest Sub Array With Sum K :- ";
    cout<<longest_subarray_with_sum_k(arr, 18);

    return 0;
}