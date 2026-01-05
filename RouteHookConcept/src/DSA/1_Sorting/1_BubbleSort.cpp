/*


1. Bubble Sort
--------------

Push maximum element at the last by adjecent swaping.


*/



#include<iostream>
#include<bits/stdc++.h>
using namespace std;



void bubbleSort(int  arr[], int n){ 
     for(int i=n-1; i>=1; i--){
        int didSwap = 0;
        for(int j=0; j<=i-1; j++){
            if(arr[j] > arr[j+1]){
                int temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
                
                didSwap = 1;
            }
        }
        if(didSwap == 0) break;
     }
}


int main(){
    
    int n;
    cout<<"Enter the size of arr : ";
    cin>>n;
    int arr[n];

    cout<<"Enter the all Elements of arr : ";
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }

    bubbleSort(arr, n);

    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }

    return 0;
}



/*

T.C = O(n^2) (average , worst case sinario)
S.C = O(1)


T.C = O(n) best case


*/