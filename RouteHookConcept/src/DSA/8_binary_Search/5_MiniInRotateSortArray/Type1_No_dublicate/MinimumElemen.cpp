




#include<bits/stdc++.h>
using namespace std;


int minimum_element_rotate_sort(vector<int>&arr){

    int low = 0;
    int high = arr.size() - 1;

    int ans = INT_MAX;

    while(low <= high){

        int mid = low + (high - low)/2;

        if(arr[low] <= arr[mid]){
            ans = min(ans, arr[low]);
            low = mid + 1;
        }
        else{
            ans = min(ans, arr[mid]);
            high = mid - 1;
        }
    }

    return ans;
}


int main(){


    vector<int>arr{9, 12, 34, 56, 78, 90, 0, 1, 2, 4, 6, 7};

    cout<<"Minimum ELement In Rotate Sorted Array:- "<<minimum_element_rotate_sort(arr);
    
    return 0;
}