/*


2. Selection Sort
-----------------

Search minimum element and placed at the first position.



*/



#include<iostream>
#include<bits/stdc++.h>
using namespace std;


void selectionSort(int arr[], int n){

    for(int i=0; i<=n-1; i++){
        int min = i;
        for(int j=i; j<=n-1; j++){
            if(arr[j] < arr[min]) min = j;
        }

        int temp = arr[min];
        arr[min] = arr[i];
        arr[i] = temp;
    }
}


int main(){
    int n;
    cout<<"Enter a the size of arr : ";
    cin>>n;
    int arr[n];

    cout<<"Enter the all elements of arr : ";
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }

    selectionSort(arr, n);


    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }

    return 0;
}




/*

T.C = O(n^2)
S.C = O(1)


*/