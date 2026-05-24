
#include<iostream>
#include<bits/stdc++.h>
using namespace std;


void merge(vector<int>&arr, int low, int mid, int high){

    vector<int>temp;

    int left = low;
    int right = mid+1;
    

    while(left <= mid  && right <= high){
        if(arr[left] <= arr[right]){
            temp.push_back(arr[left]);
            left++;
        }else{
            temp.push_back(arr[right]);
            right++;
        }
    }


    while(left <= mid){
        temp.push_back(arr[left]);
        left++;
    }

    while(right <=  high){
        temp.push_back(arr[right]);
        right++;
    }


    for(int i=low; i<=high; i++){
        arr[i] = temp[i-low];
    }
}


void mergeSort(vector<int>&arr, int low, int high){
   

    if(low >= high) return;

    int mid = low + (high - low)/2;

    mergeSort(arr, low, mid);

    mergeSort(arr, mid+1, high);

    merge(arr, low, mid, high);
}


int main(){

    int n;
    cout<<"Enter the size of arr : ";
    cin>>n;

    vector<int>arr(n);

    cout<<"Enter the arr element of arr : ";
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }

    
    mergeSort(arr, 0, n-1);

    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }

    return 0;
}


/*



🔹 Time Complexity (T.C)

Divide step:

At each level, the array is divided into 2 halves.

Division itself is O(1) work (just calculating mid).

Merge step:

Merging two halves of size n takes O(n) time.
At each level of recursion, the total merging work across subproblems is O(n).

Recursion depth:
The array keeps dividing in half until size = 1.
Depth of recursion = log₂(n).

O(n) × O(logn) = O(nlogn)
-------------------------

✅ Best Case = O(n log n)
✅ Average Case = O(n log n)
✅ Worst Case = O(n log n)


🔹 Space Complexity (S.C)

Temporary array (temp):

During merging, we use an extra array to hold elements.
This requires O(n) extra space.

Recursion stack:

Depth of recursion is O(log n).
So, recursion stack takes O(log n) space.


Total = 𝑂(𝑛)+𝑂(log⁡𝑛)≈𝑂(𝑛)


✅ Auxiliary Space = O(n)






✅ Final Answer

Time Complexity: O(n log n) (all cases)
Space Complexity: O(n)
---------------------------------------


👉 Bubble Sort vs Merge Sort:

Bubble Sort = O(n²) worst-case.

Merge Sort = O(n log n) (much faster for large inputs).




*/