/*

=== MINIMUM IN ROTATED SORTED ARRAY (WITH DUPLICATES) ===

Array Example:
Index:   0   1   2   3   4   5   6
Array:  [2   2   2   0   1   2   2]

Initial:
low = 0, high = 6
ans = +∞

-----------------------------------------------------
Duplicate Case Handling:
When:
arr[low] == arr[mid] == arr[high]

Example:
[2  2  2  0  1  2  2]
 ↑     ↑           ↑
low   mid        high

Action:
low  = low + 1
high = high - 1
👉 cannot decide sorted half → shrink window

-----------------------------------------------------
Step 1:
mid = (1+5)/2 = 3 → arr[mid] = 0

Left part NOT sorted
Minimum candidate = arr[mid] = 0
ans = min(∞, 0) = 0

👉 discard right part
high = mid - 1 = 2

-----------------------------------------------------
Step 2:
mid = (1+2)/2 = 1 → arr[mid] = 2

Left part sorted:
arr[low] ≤ arr[mid]

Minimum candidate = arr[low] = 2
ans = min(0, 2) = 0

👉 discard left part
low = mid + 1 = 2 (stop)

-----------------------------------------------------
Final Answer:
Minimum Element = 0

Visual Pointer:
[2  2  2 | 0 | 1  2  2]
            ↑
         MINIMUM

-----------------------------------------------------
Time Complexity:
Average: O(log N)
Worst (many duplicates): O(N)

Space Complexity:
O(1)

Takeaway:
Duplicates hide rotation → shrink bounds → then apply rotated logic

=====================================================






*/




#include<bits/stdc++.h>
using namespace std;

int mini_rotate_dublicate_sort_arr(vector<int>&arr){

    int low = 0;
    int high = arr.size() - 1;

    int ans = INT_MAX;

    while(low <= high){

        int mid = low + (high - low)/2;

        if(arr[low] == arr[mid] && arr[mid] == arr[high]){

            ans = min(ans, arr[low]);
            low = low + 1;
            high = high - 1;
            continue;
            
        }

        if(arr[low] <= arr[mid]){
            ans = min(ans, arr[low]);
            low = mid + 1;
        }
        else{
            ans = min(ans, arr[mid]);
            high = mid - 1;
        }

    }

    return ans;
}


int main(){

    vector<int>arr{9, 12, 34, 56, 78, 90, 90, 90, 90, 90, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 4, 6, 7};

    cout<<"Minimum ELement In Rotate Sorted Array:- "<<mini_rotate_dublicate_sort_arr(arr);
    
    return 0;
}