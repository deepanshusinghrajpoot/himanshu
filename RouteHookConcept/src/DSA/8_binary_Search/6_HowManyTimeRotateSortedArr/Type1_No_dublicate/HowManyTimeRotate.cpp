








/*









==== NUMBER OF ROTATIONS IN SORTED ARRAY – VISUAL ====

Array Example:
Index:   0   1   2   3   4   5   6
Array:  [4   5   6   7   0   1   2]

👉 Number of rotations = index of MINIMUM element

Initial:
low = 0, high = 6
ans = +∞, index = -1

-----------------------------------------------------
Step 1:
mid = (0+6)/2 = 3 → arr[mid] = 7

Left part sorted:
arr[low] ≤ arr[mid] → [4 5 6 7]

Minimum candidate = arr[low] = 4
ans = 4, index = 0

👉 discard left part
low = mid + 1 = 4

-----------------------------------------------------
Step 2:
mid = (4+6)/2 = 5 → arr[mid] = 1

Left part NOT sorted
Rotation lies here

Minimum candidate = arr[mid] = 1
ans = 1, index = 5

👉 discard right part
high = mid - 1 = 4

-----------------------------------------------------
Step 3:
mid = (4+4)/2 = 4 → arr[mid] = 0

Left part sorted:
arr[low] ≤ arr[mid]

Minimum candidate = arr[low] = 0
ans = 0, index = 4

👉 discard left part
low = mid + 1 = 5 (stop)

-----------------------------------------------------
Final Answer:
Minimum element index = 4
Number of rotations = 4

Visual Pointer:
[4  5  6  7 | 0 | 1  2]
              ↑
         ROTATION POINT

-----------------------------------------------------
Time Complexity:
O(log N)

Space Complexity:
O(1)

Takeaway:
Rotations = index of smallest element

=====================================================










*/


#include<bits/stdc++.h>
using namespace std;



int how_many_time_rotate_sorted_array(vector<int>&arr){

    int low = 0;
    int high = arr.size() - 1;

    int ans = INT_MAX;
    int index = -1;

    while(low <= high){

        int mid = low + (high - low) / 2;

        if(arr[low] <= arr[mid]){
            if(arr[low] < ans){
                index = low;
                ans = arr[low];
            } 
            low = mid + 1;
        }
        else{
            if(arr[mid] < ans){
                index = mid;
                ans = arr[mid];
            }
            high = mid - 1;
        }
    }

    return index;
}



int main(){

    vector<int>arr{9, 12, 34, 56, 78, 90, 0, 1, 2, 4, 6, 7};

    cout<<"How many time rotate a sorted array:- "<<how_many_time_rotate_sorted_array(arr);
    
    return 0;
}