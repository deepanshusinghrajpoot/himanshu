/*


=========== UPPER_BOUND – VISUAL ARRAY FLOW ===========

Array Example:
Index:   0   1   2   3   4   5
Array:  [1   2   4   4   4   7]
Target = 4

Initial:
low = 0, high = 5

Step 1:
mid = (0+5)/2 = 2 → arr[2] = 4 ≤ target
👉 move RIGHT
low = mid + 1 = 3, high = 5

Step 2:
mid = (3+5)/2 = 4 → arr[4] = 4 ≤ target
👉 move RIGHT
low = mid + 1 = 5, high = 5

Step 3:
mid = (5+5)/2 = 5 → arr[5] = 7 > target
👉 move LEFT
low = 5, high = mid - 1 = 4 (stop)

Final Answer:
upper_bound index = low = 5

Visual Pointer:
[1  2  4  4  4 | 7]
                ↑
First element > target

Time Complexity:
O(log N)  ← halves search space each step

Space Complexity:
O(1)       ← only low, high, mid variables

Takeaway:
upper_bound = first index where value > target in sorted array

========================================================


*/

#include<bits/stdc++.h>
using namespace std;



int Upper_Bound(vector<int>&arr, int target){
      
    int low = 0;
    int high = arr.size() - 1;

    while(low <= high){

        int mid = low + (high - low)/2;

        if(arr[mid] > target){
            high = mid - 1;
        }
        else{
            low = mid + 1;
        }
    }

    return low;
}



int main(){

    vector<int>arr{2, 4, 5, 6, 9, 12, 34, 78};
    cout<<"our writen function:- "<<Upper_Bound(arr, 1);

    cout<<endl;

    int ub = upper_bound(arr.begin(), arr.end(), 1) - arr.begin();
    cout<<"STL writen function:- "<<ub;

    return 0;
}