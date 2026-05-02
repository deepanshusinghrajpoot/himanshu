






#include<bits/stdc++.h>
using namespace std;


int largest_element_array(vector<int>&arr){

    int largest = arr[0];
    int secondLargest = -1;
    for(int i=0; i<arr.size(); i++){
        if(arr[i] > largest){
            largest = arr[i];
        }
    }
    for(int i=0; i<arr.size(); i++){
        if(arr[i] > secondLargest && arr[i] != largest){
            secondLargest = arr[i];
        }
    }

    return secondLargest;
}


int main(){

    vector<int>arr{2, 4, 1, 6, 7, 3, 5, 8, 9};
    cout<<"Largest In The Array:- ";
    cout<<largest_element_array(arr);

    return 0;
}