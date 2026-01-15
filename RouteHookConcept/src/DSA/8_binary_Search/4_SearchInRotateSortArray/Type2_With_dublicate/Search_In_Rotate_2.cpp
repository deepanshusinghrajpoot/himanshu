/*



=== SEARCH IN ROTATED SORTED ARRAY (WITH DUPLICATES) ===

Array Example:
Index:   0   1   2   3   4   5   6
Array:  [2   5   6   0   0   1   2]
Target = 0

Initial:
low = 0, high = 6

-----------------------------------------------------
Step 1:
mid = (0+6)/2 = 3 → arr[3] = 0 🎯 FOUND

-----------------------------------------------------
(Important Duplicate Case Handling)

When:
arr[low] == arr[mid] == arr[high]

Example:
[2  2  2  3  4  2  2]
 ↑     ↑           ↑
low   mid        high

Action:
low  = low + 1
high = high - 1
👉 shrink search space (cannot decide sorted half)

-----------------------------------------------------
General Flow (when not all equal):

Case 1️⃣: Left half sorted
arr[low] ≤ arr[mid]

Check:
Is target in [arr[low] .. arr[mid]] ?
YES → move LEFT
NO  → move RIGHT

Case 2️⃣: Right half sorted
arr[mid] ≤ arr[high]

Check:
Is target in [arr[mid] .. arr[high]] ?
YES → move RIGHT
NO  → move LEFT

-----------------------------------------------------
Visual Pointer Example:
[2  5  6 | 0  0  1  2]
          ↑
        TARGET

-----------------------------------------------------
Time Complexity:
Average: O(log N)
Worst (many duplicates): O(N)

Space Complexity:
O(1)

Takeaway:
Duplicates break sorting check → shrink bounds → then apply rotated binary search

=====================================================









*/






#include<bits/stdc++.h>
using namespace std;


int search_in_rotate_sort_arr(vector<int>&arr, int target){

    int low = 0;
    int high = arr.size() - 1;

    while(low <= high){
       
         int mid = low + (high - low)/2;

         if(arr[mid] == target)  return mid;

         if(arr[low] == arr[mid] && arr[mid] == arr[high]){
            low = low + 1;
            high = high - 1;
            continue;
         }

         if(arr[low] <= arr[mid]){
            if(arr[low] <= target && target <= arr[high]){
                high = mid - 1;
            }else{
                low = mid + 1;
            }
         }else{
            if(arr[mid] <= target &&  target <= arr[high]){
                low = mid + 1;
            }else{
                high = mid - 1;
            }
         }
    }

    return -1;
}



int main(){

    vector<int>arr{8, 8, 9, 12, 34, 56, 78, 90, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 7, 8, 8, 8};

    cout<<"Target Eelement Index:- "<<search_in_rotate_sort_arr(arr, 2);
    return 0;
}