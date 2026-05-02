






#include<bits/stdc++.h>
using namespace std;


void right_rotate_one_place(vector<int>&arr){

    int n = arr.size();
    int temp = arr[n-1];
    for(int i=n-1; i>=1; i--){
        arr[i] = arr[i-1];
    }
    arr[0] = temp;

}



int main(){

    vector<int>arr{2, 4, 3, 1, 5, 6, 7, 0, 8, 9};

    cout<<"Right rotate array by one place:- ";
    right_rotate_one_place(arr);
    for(int i=0; i<arr.size(); i++){
        cout<<arr[i]<<" ";
    }

    return 0;
}