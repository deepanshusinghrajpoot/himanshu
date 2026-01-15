

/*


=============== BINARY SEARCH – VISUAL VIEW =================

🟢 Problem:
Find target in a sorted array using Binary Search

🟢 Example Input:
arr = [2, 4, 6, 8, 10, 12, 14]
target = 10

Index:   0   1   2   3   4    5    6
Array:  [2   4   6   8   10   12   14]

🟢 Initial Pointers:
low = 0
high = 6

🟢 Iteration 1:
mid = (0 + 6) / 2 = 3
arr[mid] = 8  < 10
👉 Move RIGHT

low = mid + 1 = 4
high = 6

🟢 Iteration 2:
mid = (4 + 6) / 2 = 5
arr[mid] = 12 > 10
👉 Move LEFT

low = 4
high = mid - 1 = 4

🟢 Iteration 3:
mid = (4 + 4) / 2 = 4
arr[mid] = 10 == target 🎯
👉 FOUND

🟢 Final Output:
Index = 4

🟢 Visual Pointer Movement:
[2  4  6  8 | 10 | 12  14]
           ↑
         TARGET

🟢 Why This Works:
- Sorted order guarantees direction decision
- Each step removes half the array
- low & high always enclose valid search space

🟢 Time Complexity:
O(log N)

🟢 Space Complexity:
O(1)

🟢 Interview Takeaway:
Binary Search = shrink window until mid hits target.

============================================================


*/










#include<bits/stdc++.h>
using namespace std;



int binary_search(vector<int>&arr, int target){

    int low = 0;
    int high = arr.size() - 1;

    while(low <= high){

        int mid = low + (high - low) / 2;

        if(arr[mid] == target) return mid;
        else if(arr[mid] > target) high = mid - 1;
        else low = mid + 1;
    }

    return -1;
}



int main(){

    vector<int>arr{2, 4, 5, 6, 9, 12, 34, 78};
    cout<<binary_search(arr, 9);

    return 0;
}