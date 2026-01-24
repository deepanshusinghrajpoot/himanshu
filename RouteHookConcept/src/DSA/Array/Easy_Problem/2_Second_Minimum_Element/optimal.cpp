  






#include<bits/stdc++.h>
using namespace std;


int second_minimum_element_array(vector<int>&arr){

    int minimum = arr[0];
    int secondMinimum = -1;
    for(int i=0; i<arr.size(); i++){

        if(arr[i] < minimum){
            secondMinimum = minimum;
            minimum = arr[i];
        }
        else if(arr[i] < secondMinimum && arr[i] != minimum){
            secondMinimum = arr[i];
        }
        
    }

    return secondMinimum;

}


int main(){

    vector<int>arr{2, 4, 1, 6, 7, 3, 5, 8, 9};
    cout<<"Second Minimum Element In The Array:- ";
    cout<<second_minimum_element_array(arr);

    return 0;
}