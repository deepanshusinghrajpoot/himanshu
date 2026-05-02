
/*






================= MAXIMUM SUBARRAY SUM (KADANE’S ALGORITHM) =================

Problem:
----------------------------------------------------------------
Find the maximum possible sum of a CONTIGUOUS subarray.

----------------------------------------------------------------
Approach Used:
----------------------------------------------------------------
Kadane’s Algorithm

----------------------------------------------------------------
Core Idea:
----------------------------------------------------------------
• Traverse the array once  
• Maintain a running subarray sum  
• Drop the subarray when its sum becomes negative  
• Track the maximum sum encountered  

----------------------------------------------------------------
Variables Conceptually Used:
----------------------------------------------------------------
currentSum → sum of current subarray  
maxSum     → maximum subarray sum found so far  

----------------------------------------------------------------
Step-by-Step Working:
----------------------------------------------------------------

1️⃣ Start with:
   currentSum = 0  
   maxSum = −∞  

2️⃣ For each element in the array:
   • Add element to currentSum  
   • Update maxSum if currentSum is greater  
   • If currentSum becomes NEGATIVE:
       → discard it (set currentSum = 0)

3️⃣ After traversal, maxSum is the answer  

----------------------------------------------------------------
Diagrammatic Explanation:
----------------------------------------------------------------

Array:
[-2, 1, -3, 4, -1, 2, 1, -5, 4]

Running Subarrays:
------------------------------------------------
[-2] ❌
[1] ✅
[1, -3] ❌
[4] ✅
[4, -1] ✅
[4, -1, 2] ✅
[4, -1, 2, 1] ⭐ (MAX)
[-5] ❌
[4] ✅

----------------------------------------------------------------
Final Answer:
----------------------------------------------------------------
Maximum Subarray Sum = 6  
(Subarray = [4, -1, 2, 1])

----------------------------------------------------------------
Why This Works:
----------------------------------------------------------------
• Any subarray with negative sum only reduces future totals  
• Best subarray always starts after a negative prefix  
• Ensures optimal result in a single pass  

----------------------------------------------------------------
Validity:
----------------------------------------------------------------
✅ Works for positive numbers  
✅ Works for negative numbers  
✅ Works for mixed arrays  

----------------------------------------------------------------
Time Complexity:
----------------------------------------------------------------
O(N)

----------------------------------------------------------------
Where does O(N) come from?
----------------------------------------------------------------
• Single traversal of the array  
• Each element processed exactly once  

----------------------------------------------------------------
Space Complexity:
----------------------------------------------------------------
O(1)

----------------------------------------------------------------
One-Line Interview Answer:
----------------------------------------------------------------
“Kadane’s algorithm finds the maximum subarray sum by discarding
negative prefixes during a single traversal.”

================================================================







*/




#include<bits/stdc++.h>
using namespace std;


int maxSubarraySum(vector<int>&arr){

    int sum = 0;
    int maxi = INT_MIN;

    for(int i=0; i<arr.size(); i++){

        sum += arr[i];

        if(sum > maxi) maxi = sum;

        if(sum < 0) sum = 0;
    }

    return maxi;
}



int main(){

    vector<int>arr{1, -2, 3, 4, -1, 2, 1, -5, 4};

    cout<<"Maximum Sub Array Sum:- ";
    cout<<maxSubarraySum(arr);

    return 0;
}