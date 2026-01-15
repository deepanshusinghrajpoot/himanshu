
/*


=========== LOWER_BOUND – VISUAL ARRAY FLOW ===========

Array Example:
Index:   0   1   2   3   4   5
Array:  [1   2   4   4   4   7]
Target = 4

Initial:
low = 0, high = 5

Step 1:
mid = (0+5)/2 = 2 → arr[2] = 4 ≥ target
👉 move LEFT
low = 0, high = mid - 1 = 1

Step 2:
mid = (0+1)/2 = 0 → arr[0] = 1 < target
👉 move RIGHT
low = mid + 1 = 1, high = 1

Step 3:
mid = (1+1)/2 = 1 → arr[1] = 2 < target
👉 move RIGHT
low = mid + 1 = 2, high = 1 (stop)

Final Answer:
lower_bound index = low = 2

Visual Pointer:
[1  2 | 4  4  4  7]
       ↑
   First ≥ target

Time Complexity:
O(log N)  ← Binary Search halves the search space

Space Complexity:
O(1)       ← Only variables low, high, mid used

Takeaway:
lll lower_bound = first index where value ≥ target in sorted array

========================================================






*/



#include<bits/stdc++.h>
using namespace std;



int Lower_Bound(vector<int>&arr, int target){
    
     int low = 0;
     int high = arr.size() - 1;

     while(low <= high){

        int mid = low + (high - low) / 2;

        if(arr[mid] >= target){
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
    cout<<"our writen function:- "<<Lower_Bound(arr, 9);

    cout<<endl;

    int lb = lower_bound(arr.begin(), arr.end(), 9) - arr.begin();
    cout<<"STL writen function:- "<<lb;

    return 0;
}