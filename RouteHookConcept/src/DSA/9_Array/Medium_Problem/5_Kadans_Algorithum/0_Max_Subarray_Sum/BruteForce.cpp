






#include<bits/stdc++.h>
using namespace std;


int maxSubarraySum(vector<int>&arr){

    int maxi = INT_MIN;

    for(int i=0; i<arr.size(); i++){
         int sum = 0;
         for(int j=i; j<arr.size(); j++){
               sum += arr[j];
               maxi = max(maxi, sum);
         } 
    }

    return maxi;
}



int main(){

    vector<int>arr{1, -2, 3, 4, -1, 2, 1, -5, 4};

    cout<<"Maximum Sub Array Sum:- ";
    cout<<maxSubarraySum(arr);

    return 0;
}