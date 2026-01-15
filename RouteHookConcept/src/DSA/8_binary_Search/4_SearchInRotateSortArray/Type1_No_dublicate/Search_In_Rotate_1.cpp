

/*



======= SEARCH IN ROTATED SORTED ARRAY – VISUAL =======

Array Example:
Index:   0   1   2   3   4   5   6
Array:  [4   5   6   7   0   1   2]
Target = 0

Initial:
low = 0, high = 6

Step 1:
mid = (0+6)/2 = 3 → arr[3] = 7

Left part sorted:
arr[low] ≤ arr[mid] → [4 5 6 7]

Target NOT in left range [4..7]
👉 move RIGHT

low = mid + 1 = 4, high = 6

Step 2:
mid = (4+6)/2 = 5 → arr[5] = 1

Right part sorted:
arr[mid] ≤ arr[high] → [0 1 2]

Target in right range [0..2]
👉 move LEFT

low = 4, high = mid - 1 = 4

Step 3:
mid = (4+4)/2 = 4 → arr[4] = 0 🎯 FOUND

Final Answer:
Index = 4

Visual Pointer:
[4  5  6  7 | 0 | 1  2]
              ↑
            TARGET

-------------------------------------------------------
Key Check:
- One half is always SORTED
- Decide which half → check target range → discard other half

-------------------------------------------------------
Time Complexity:
O(log N)

Space Complexity:
O(1)

Takeaway:
Find sorted half → check range → shrink search space

=======================================================


*/






#include<bits/stdc++.h>
using namespace std;



int search_rotate_sort_arr(vector<int>&arr, int target){

    int low = 0;
    int high = arr.size() - 1;

    while(low <= high){

        int mid = low + (high - low)/2;

        if(arr[mid] == target) return mid;

        if(arr[low] <= arr[mid]){
            if(arr[low] <= target &&  target <= arr[mid]){
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

    vector<int>arr{89, 123, 456, 678, 2, 4, 6, 7, 9, 24, 67};

    cout<<"Target Element:- "<<search_rotate_sort_arr(arr, 9);


    return 0;
}