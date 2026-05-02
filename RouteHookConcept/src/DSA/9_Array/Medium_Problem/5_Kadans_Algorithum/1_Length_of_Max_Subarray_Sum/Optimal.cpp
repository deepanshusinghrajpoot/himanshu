














#include<bits/stdc++.h>
using namespace std;


int lengthOfMaxSubarraySum(vector<int>&arr){

       int maxi = INT_MIN;
       int startIndex = 0;
       int endIndex = 0;
  
       int sum = 0;
       for(int i=0; i<arr.size(); i++){

           int start;
           if(sum == 0) start = i;
           sum += arr[i];

           if(sum > maxi){
             maxi = sum;
             startIndex = start;   endIndex = i;
           }

           if(sum < 0){
             sum = 0;
           }
       }

       return endIndex - startIndex + 1;
}


int main(){

    vector<int>arr{1, -2, 3, 4, -1, 2, 1, -5, 4};

    cout<<"Length of Maximum Sub Array Sum:- ";     // [3, 4, -1, 2, 1]
    cout<<lengthOfMaxSubarraySum(arr);


    return 0;
}