
/*













======= RECURSIVE BINARY SEARCH – CORE CONCEPTS =======

🟢 Condition:
Array must be SORTED

🟢 Parameters:
low → start index
high → end index
target → value to find

🟢 Base Case:
if (low > high) → return -1

🟢 Mid Calculation:
mid = low + (high - low) / 2

🟢 Decision:
arr[mid] == target → return mid
arr[mid] > target  → search left (low, mid-1)
arr[mid] < target  → search right (mid+1, high)

🟢 Key Idea:
Each call reduces search space by HALF

🟢 Time Complexity:
O(log N)

🟢 Space Complexity:
O(log N)  (recursion stack)

🟢 Takeaway:
Sorted data + halving range → Recursive Binary Search

=====================================================








*/











#include<bits/stdc++.h>
using namespace std;



int binary_search(vector<int>&arr, int low, int high, int target){
      
    if(low > high)  return -1;

    int mid = low + (high - low)/2;

    if(arr[mid] == target) return mid;
    else if(arr[mid] > target) return binary_search(arr, low, mid-1, target);
    else return binary_search(arr, mid+1, high, target);
     
}



int main(){

    vector<int>arr{2, 4, 5, 6, 9, 12, 34, 78};
    int n = arr.size() - 1;
    cout<<binary_search(arr, 0, n-1, 9);

    return 0;
}