
/*



=========== MAXIMUM PRODUCT SUBARRAY (TWO PASS METHOD) ===========

Problem:
--------------------------------------------------
Find the maximum product of a CONTIGUOUS subarray.

Array may contain:
• Positive numbers
• Negative numbers
• Zero

--------------------------------------------------
Why Simple Approach Fails:
--------------------------------------------------

• Negative × Negative = Positive
• Zero breaks the product chain
• Maximum product can start or end ANYWHERE

--------------------------------------------------
Core Idea:
--------------------------------------------------

• Traverse array from LEFT → RIGHT
• Traverse array from RIGHT → LEFT
• Track running product
• Reset product when it becomes ZERO

--------------------------------------------------
Why Two Passes?
--------------------------------------------------

• Left-to-right handles normal cases
• Right-to-left handles cases where
  maximum product comes after an ODD
  number of negative elements

--------------------------------------------------
Algorithm Flow:
--------------------------------------------------

1️⃣ Initialize:
• product = 1
• maxProduct = -∞

--------------------------------------------------
2️⃣ First Pass (Left → Right):
--------------------------------------------------

For each element:
• product = product × arr[i]
• Update maxProduct
• If product == 0 → reset product to 1

--------------------------------------------------
3️⃣ Second Pass (Right → Left):
--------------------------------------------------

Repeat same logic from the end:
• product = product × arr[i]
• Update maxProduct
• Reset on zero

--------------------------------------------------
Why Reset on Zero?
--------------------------------------------------

• Zero destroys product continuity
• Any subarray crossing zero gives product = 0
• So start fresh after zero

--------------------------------------------------
Example:
--------------------------------------------------

Array:
[2, 3, -2, 4]

Left → Right:
Products: 2 → 6 → -12 → -48

Right → Left:
Products: 4 → -8 → -24 → -48

Max Product = 6

--------------------------------------------------
Why This Works:
--------------------------------------------------

• Handles:
  - Even negatives
  - Odd negatives
  - Zero-separated subarrays
• Covers all possible subarrays implicitly

--------------------------------------------------
Time Complexity:
--------------------------------------------------
O(N)

--------------------------------------------------
Where does O(N) come from?
--------------------------------------------------

• One pass left → right
• One pass right → left
• Total = 2N → O(N)

--------------------------------------------------
Space Complexity:
--------------------------------------------------
O(1)

--------------------------------------------------
Why O(1)?
--------------------------------------------------

• Only constant variables used
• No extra arrays or data structures

--------------------------------------------------
Edge Cases:
--------------------------------------------------

• Single element array
• All negatives
• Array containing zero
• All zeros

--------------------------------------------------
One-Line Interview Answer:
--------------------------------------------------
"Using two directional scans handles negative numbers
and zeros to compute maximum product in O(N) time."

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

    int product = 1;
    int maxProduct = INT_MIN;

    for(int i=0; i<arr.size(); i++){

        product *= arr[i];

        if(product > maxProduct){
            maxProduct = product;
        }

        if(product == 0){
            product = 1;
        }
    }

    
    product = 1;

    for(int i =arr.size()-1;  i>=0; i--){
       
        product *= arr[i];

        if(product > maxProduct){
            maxProduct = product;
        }

        if(product == 0){
            product = 1;
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