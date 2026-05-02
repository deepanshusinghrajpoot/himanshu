
/*




=========== LONGEST SUBARRAY WITH SUM = K (SLIDING WINDOW) ===========

⚠️ Important:
This approach works ONLY when the array contains:
✔ Positive elements
❌ NOT valid for negative numbers

-----------------------------------------------------------
Problem:
-----------------------------------------------------------

Find the length of the longest subarray
whose sum equals K.

-----------------------------------------------------------
Core Idea (Sliding Window):
-----------------------------------------------------------

• Use two pointers: LEFT and RIGHT
• Expand window by moving RIGHT
• Shrink window by moving LEFT when sum > K
• Maintain current window sum

-----------------------------------------------------------
Why Sliding Window Works Here?
-----------------------------------------------------------

• Array has ONLY positive numbers
• Increasing window → sum increases
• Shrinking window → sum decreases
• Sum changes monotonically (predictable)

-----------------------------------------------------------
Window Movement Logic:
-----------------------------------------------------------

1️⃣ Add arr[right] to sum
2️⃣ If sum > K
   → move LEFT forward
   → subtract arr[left]
3️⃣ If sum == K
   → update max length
4️⃣ Move RIGHT forward

-----------------------------------------------------------
Visualization:
-----------------------------------------------------------

Array: [1, 2, 3, 1, 1, 1, 1]
K = 3

Window:
[1, 2] → sum = 3 ✔
Length = 2

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------

O(N)

-----------------------------------------------------------
Why O(N)?
-----------------------------------------------------------

• LEFT moves at most N times
• RIGHT moves at most N times
• Each element added and removed once

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------

O(1)
→ No extra data structures used

-----------------------------------------------------------
Key Interview Takeaway:
-----------------------------------------------------------

"Sliding Window gives O(N) time complexity
but works ONLY for positive arrays.
For negative numbers, hashing is required."

===========================================================




*/





#include<bits/stdc++.h>
using namespace std;


int longest_subarray_with_sum_k(vector<int>&arr, int k){
     
      
       int right = 0;
       int left = 0;

       int maxLen = 0;
       int sum = arr[0];

       while(right < arr.size()){

           while(left <= right && sum > k){
              sum -= arr[left];
              left++;
           }

           if(sum == k)  maxLen = max(maxLen, right - left + 1);

           right++;
           if(right < arr.size()) sum += arr[right];

       }

       return maxLen;
}



int main(){


    vector<int>arr{9, 4, 3, 5, 6, 7, 0, 1};

    cout<<"Longest Sub Array With Sum K :- ";
    cout<<longest_subarray_with_sum_k(arr, 18);

    return 0;
}