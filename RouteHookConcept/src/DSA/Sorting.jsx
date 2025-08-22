import React from 'react'



/*



Insertion Sort
--------------

#include <bits/stdc++.h> 
void insertionSort(int n, vector<int> &arr){
    // Write your code here.
    
    for(int i=0; i<=n-1; i++){
        int j = i;
        while(j > 0){
            if(arr[j-1] > arr[j]){
                swap(arr[j], arr[j-1]);
            }
            j--;
        }
    }
}

T.C = O(n^2)
S.C = O(1)










Bubble Sort
-----------

#include <bits/stdc++.h> 
void bubbleSort(vector<int>& arr, int n)
{   
    
    for(int i=n-1; i>=1; i--){
        int didSwap = 0;
        for(int j=0; j<=n-2; j++){
            if(arr[j]>arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                
                didSwap = 1;
            }
        }
        if(didSwap == 0) break;
    }
   

}


T.C = O(n^2)
S.C = O(1)







Insertion Sort
--------------
#include <bits/stdc++.h> 
void insertionSort(int n, vector<int> &arr){
    // Write your code here.
    
    for(int i=0; i<=n-1; i++){
        int j = i;
        while(j > 0){
            if(arr[j-1] > arr[j]){
                swap(arr[j], arr[j-1]);
            }
            j--;
        }
    }
}

T.O = O(n^2)
S.C = O(1);







Merge Sort
----------

#include<bits/stdc++.h>
using namespace std;


void merge(vector<int>&arr, int low, int mid, int high){

    int left = low;
    int right = mid + 1;

    vector<int>temp;

    while(left <= mid && right <= high){
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

    while(right <= high){
        temp.push_back(arr[right]);
        right++;
    }

    for(int i=low; i<=high; i++){
        arr[i] = temp[i-low];
    }
}

void merge_sort(vector<int>&arr, int low, int high){

    if(low >= high) return;

    int mid = low + (high - low)/2;

    merge_sort(arr, low, mid);
    merge_sort(arr, mid+1, high);

    merge(arr, low, mid, high);
}

void mergeSort(vector < int > & arr, int n) {
    // Write your code here.
    
    merge_sort(arr, 0, n-1);
    
}


T.C = O(nlogn);
O.C = O(n);







Quick Sort
----------

#include <bits/stdc++.h> 

int partition(vector<int>&arr, int low, int high){

    int i=low;
    int j=high;
    int pivot = arr[low];

    while(i<j){
        
        while(arr[i] <= pivot && i <= high-1) i++;
        while(arr[j] > pivot && j >= low+1) j--;

        if(i < j){
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }

    }
    
    swap(arr[j], arr[low]);

    return j;
    
}

void quick_sort(vector<int>&arr, int low, int high){

    if(low < high){

        int pIndex = partition(arr, low, high);

        quick_sort(arr, low, pIndex-1);
        quick_sort(arr, pIndex+1, high);
    }

}

vector<int> quickSort(vector<int> arr)
{
   // Write your code here.
    
    int n = arr.size();

    quick_sort(arr, 0, n-1);

    return arr;
}


T.C = O(nlogn)
S.C = o(1)









*/












const Sorting = () => {
  return (
    <div>Sorting</div>
  )
}

export default Sorting