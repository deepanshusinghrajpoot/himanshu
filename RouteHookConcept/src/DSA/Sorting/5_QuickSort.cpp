/*


5. Quick Sort
--------------

Select first element as pivota and placed at right position





*/








#include<iostream>
#include<bits/stdc++.h>
using namespace std;


int partition(vector<int>&arr, int low, int high){
        

     int pivot = arr[low];
     int i = low;
     int j = high;

     while(i < j){

        while(arr[i] <= pivot && i <= high - 1) i++;
        while(arr[j] > pivot && j >= low + 1) j--;

        if(i < j){
            int temp = arr[i];
            arr[i]  = arr[j];
            arr[j]  = temp;
        }
     }



     int temp = arr[low];
     arr[low] = arr[j];
     arr[j] = temp;


     return j;
}






void quick_sort(vector<int>&arr, int low, int high){

    if(low < high){

        int pIndex = partition(arr, low, high);

        quick_sort(arr, low, pIndex - 1);

        quick_sort(arr, pIndex + 1, high); 

    }

}







int main(){

    int n;
    cout<<"Enter size of arr : ";
    cin>>n;

    vector<int>arr(n);

    cout<<"Enter all element of the arr : ";
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }


    quick_sort(arr, 0, n-1);

    cout<<"Sorted arr : ";
    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }


    return 0;
}



/*




| Case         | Time Complexity | Space Complexity |
| ------------ | --------------- | ---------------- |
| Best Case    | O(n log n)      | O(log n)         |
| Average Case | O(n log n)      | O(log n)         |
| Worst Case   | O(n²)           | O(n)             |




*/

