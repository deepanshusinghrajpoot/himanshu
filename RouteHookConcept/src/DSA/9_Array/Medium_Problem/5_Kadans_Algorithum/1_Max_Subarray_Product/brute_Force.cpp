



/*


=========== MAXIMUM PRODUCT SUBARRAY (BRUTE FORCE) ===========

Problem:
--------------------------------------------------
Find the maximum product of a CONTIGUOUS subarray.

--------------------------------------------------
Core Idea:
--------------------------------------------------

• Try ALL possible subarrays
• Compute product for each subarray
• Track the maximum product found

--------------------------------------------------
Algorithm Flow:
--------------------------------------------------

For every starting index i:
→ Initialize product = 1

For every ending index j (j ≥ i):
→ product = product × arr[j]
→ Update maxProduct

--------------------------------------------------
Why This Works:
--------------------------------------------------

• Every possible contiguous subarray is considered
• Guarantees correct maximum product
• Handles:
  - Positive numbers
  - Negative numbers
  - Zero values

--------------------------------------------------
Example:
--------------------------------------------------

Array:
[2, 3, -2, 4]

Subarrays & Products:
[2] = 2
[2,3] = 6
[2,3,-2] = -12
[2,3,-2,4] = -48
[3] = 3
[3,-2] = -6
[3,-2,4] = -24
[-2] = -2
[-2,4] = -8
[4] = 4

Maximum Product = 6

--------------------------------------------------
Time Complexity:
--------------------------------------------------
O(N²)

--------------------------------------------------
Where does O(N²) come from?
--------------------------------------------------

• Outer loop runs N times
• Inner loop runs up to N times
• Total operations = N × N

--------------------------------------------------
Space Complexity:
--------------------------------------------------
O(1)

--------------------------------------------------
Why O(1)?
--------------------------------------------------

• Uses only constant extra variables
• No additional data structures

--------------------------------------------------
Limitations:
--------------------------------------------------

• Inefficient for large N
• Recomputes overlapping subarray products

--------------------------------------------------
Optimized Approach:
--------------------------------------------------

• Two-pass scan OR
• Kadane’s-style max/min tracking
• Time Complexity → O(N)

--------------------------------------------------
One-Line Interview Answer:
--------------------------------------------------
"Brute force checks all subarrays, leading to O(N²)
time but guarantees correctness."

===================================================





| Test Case | Input            | Output |
| --------- | ---------------- | ------ |
| 1         | `2 3 -2 4`       | `6`    |
| 2         | `-2 0 -1`        | `0`    |
| 3         | `-2 3 -4`        | `24`   |
| 4         | `0 0 0`          | `0`    |
| 5         | `-1 -3 -10 0 60` | `60`   |
| 6         | `-2 -3 0 -2 -40` | `80`   |
| 7         | `1`              | `1`    |
| 8         | `-1`             | `-1`   |




*/




#include<bits/stdc++.h>
using namespace std;



int max_product_sub_array(vector<int>&arr){

    int maxProduct = INT_MIN;
    
    for(int i=0; i<arr.size(); i++){
        int product = 1;
        for(int j=i; j<arr.size(); j++){
            product *= arr[j];
            if(product > maxProduct){
                maxProduct = product;
            }
        }

    }

    return maxProduct;
}



int main(){

    vector<vector<int>> testCases = {
        {2, 3, -2, 4},
        {-2, 0, -1},
        {-2, 3, -4},
        {0, 0, 0},
        {-1, -3, -10, 0, 60},
        {-2, -3, 0, -2, -40},
        {1},
        {-1}
    };

    for(int i = 0; i < testCases.size(); i++){
        cout << "Test Case " << i + 1 << ": ";
        for(int x : testCases[i]) cout << x << " ";
        cout << "\nMax Product = "
             << max_product_sub_array(testCases[i]) << "\n\n";
    }

    return 0;
}