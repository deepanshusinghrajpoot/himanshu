






#include<bits/stdc++.h>
using namespace std;


void left_rotate_one_place(vector<int>&arr){

    int temp = arr[0];
    for(int i=0; i<=arr.size()-2; i++){
        arr[i] = arr[i+1];
    }
    arr[arr.size()-1] = temp;

}



int main(){

    vector<int>arr{2, 4, 3, 1, 5, 6, 7, 0, 8, 9};

    cout<<"Left rotate array by one place:- ";
    left_rotate_one_place(arr);
    for(int i=0; i<arr.size(); i++){
        cout<<arr[i]<<" ";
    }

    return 0;
}