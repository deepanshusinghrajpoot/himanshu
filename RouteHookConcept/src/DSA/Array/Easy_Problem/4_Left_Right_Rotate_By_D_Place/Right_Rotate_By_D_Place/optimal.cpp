














#include<bits/stdc++.h>
using namespace std;


void reverse_array(vector<int>&arr, int left, int right){

    while(left < right){
        swap(arr[left], arr[right]);
        left++;
        right--;
    }

}


void right_rotate_by_d_place(vector<int>&arr, int k){

    int n = arr.size();

    k = k%n;
    int d = n-k;

    reverse_array(arr, 0, d-1);
    reverse_array(arr, d, n-1);
    reverse_array(arr, 0, n-1);

}




int main(){

    vector<int>arr{2, 3, 4, 5, 6, 1, 7, 8, 9, 0};

    cout<<"Rotate D place right of the array :- ";
    right_rotate_by_d_place(arr, 4);
    for(int i=0; i<arr.size(); i++){
         cout<<arr[i]<<" ";
    }

    return 0;
}