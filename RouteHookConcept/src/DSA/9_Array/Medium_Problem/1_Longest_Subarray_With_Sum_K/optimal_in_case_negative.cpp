


/*



=========== LONGEST SUBARRAY WITH SUM = K (HASHING) ===========

Problem:
Find the length of the longest subarray whose sum equals K.
Array can contain:
✔ Positive
✔ Negative
✔ Zero elements


Note:- Optimal In Case array contain negative elements
-----------------------------------------------------------
Approach:
-----------------------------------------------------------

• Use Prefix Sum + Hash Map
• Store FIRST occurrence of each prefix sum
• Check if (currentSum − K) already exists

-----------------------------------------------------------
Algorithm:
-----------------------------------------------------------

Initialize:
sum = 0
maxLen = 0
map<prefixSum, index>

For each index i:
1️⃣ sum += arr[i]

2️⃣ If sum == K
   → maxLen = max(maxLen, i + 1)

3️⃣ If (sum − K) exists in map
   → subarray length = i − map[sum − K]
   → update maxLen

4️⃣ Store sum in map if not already present
   (store FIRST occurrence only)

-----------------------------------------------------------
Why FIRST occurrence?
-----------------------------------------------------------

• Gives maximum possible subarray length
• Later occurrences reduce length

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------

Using map (ordered):
• Each find/insert = O(log N)
• Loop runs N times

Total:
O(N log N)

-----------------------------------------------------------
Why O(N log N)?
-----------------------------------------------------------

• N iterations
• Each iteration performs:
  - find() → O(log N)
  - insert() → O(log N)

Constants ignored → O(N log N)

-----------------------------------------------------------
If unordered_map is used:
-----------------------------------------------------------

• find() and insert() → O(1) average

Time Complexity:
O(N)

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------

O(N)
→ Hash map stores prefix sums

-----------------------------------------------------------
Key Interview Takeaway:
-----------------------------------------------------------

"This approach works for arrays containing
positive, negative, and zero values.
Time complexity is O(N log N) with map,
and O(N) average with unordered_map."

===========================================================



*/













#include<bits/stdc++.h>
using namespace std;


int longest_subarray_with_sum_k(vector<int>&arr, int k){
     

      map<int, int>mp;

      int maxLen = 0;
      int sum = 0;
      
      for(int i=0; i<arr.size(); i++){
           
          sum += arr[i];

          if(sum == k){
               maxLen = max(maxLen, i+1);
          }
          
          int rem = sum - k;

          if(mp.find(rem) != mp.end()){

              int len = i - mp[rem];
              maxLen = max(maxLen, len);
          }

          if(mp.find(sum) == mp.end()){
              mp[sum] = i;
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