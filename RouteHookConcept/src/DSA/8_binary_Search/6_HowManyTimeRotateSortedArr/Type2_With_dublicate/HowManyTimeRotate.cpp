






#include<bits/stdc++.h>
using namespace std;



int how_many_time_rotate_sorted_array(vector<int>&arr){

    int low = 0;
    int high = arr.size() - 1;

    int ans = INT_MAX;
    int index = -1;

    while(low <= high){

        int mid = low + (high - low)/2;

        if(arr[low] == arr[mid] && arr[mid] == arr[high]){

            if(arr[low] < ans){
                index = low;
                ans = arr[low];
            }
            if (arr[high] < ans) {
                ans = arr[high];
                index = high;
            }

            low = low + 1;
            high = high - 1;

            continue;
        }

        if(arr[low] <= arr[mid]){
            if(arr[low] < ans){
                index = low;
                ans = arr[low];
            }
            low = mid + 1;
        }else{
            if(arr[mid] < ans){
                index = mid;
                ans = arr[mid];
            }
            high = mid - 1;
        }
    }

    return index;
}




int main(){

    vector<int>arr{9, 12, 34, 56, 78, 90, 90, 90, 90, 90, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 4, 6, 7};

    cout<<"How many time rotate a sorted array:- "<<how_many_time_rotate_sorted_array(arr);

    return 0;
}