/*



3. Insertion Sort
-----------------


Insert a element at the right position for each element.




*/


#include<iostream>
#include<bits/stdc++.h>
using namespace std;


void insertionSort(int arr[], int n){
    
    for(int i=0; i<=n-1; i++){
        int j = i;
        while(j>0){
            if(arr[j-1] > arr[j]){
                int temp = arr[j - 1];
                arr[j-1] = arr[j];
                arr[j] = temp;
            }
            j--;
        }
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

    insertionSort(arr, n);


    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }

    return 0;
}


/*


T.C = O(n^2)
S.C = O(1)



*/