#include<iostream>
#include<bits/stdc++.h>
using namespace std;

    int search(vector<int>& nums, int target) {
       
       int n = nums.size();
       int low = 0;
       int high = n-1;

       while(low <= high){

         int mid = low + (high - low)/2;

         if(nums[mid] == target) return mid;
         if(nums[mid] < target) low = mid + 1;
         else high = mid - 1;

       } 

       return -1;
    }

        int main(){

        int n;
        cout<<"Enter the size of vector : ";
        cin>>n;
        vector<int>arr(n);

        cout<<"Enter the all elements of vector which is also in sorted form : ";
        for(int i=0; i<n; i++){
            cin>>arr[i];
        }


        int target;
        cout<<"Enter the target element which we want to search in the vector : ";
        cin>>target;

        cout<<"Element exist at the index number : ";
        cout<<search(arr, target)<<endl;

        return 0;
    }


    // T.C = O(log n)
    // S.C = O(1)