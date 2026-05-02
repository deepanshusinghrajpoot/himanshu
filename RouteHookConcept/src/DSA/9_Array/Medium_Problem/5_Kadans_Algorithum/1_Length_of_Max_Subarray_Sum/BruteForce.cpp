














#include<bits/stdc++.h>
using namespace std;


int lengthOfMaxSubarraySum(vector<int>&arr){

    int maxi = INT_MIN;
    int maxLength = 0;

    for(int i=0; i<arr.size(); i++){
        int sum = 0;
        for(int j=i; j<arr.size(); j++){
            sum += arr[j];
            if(sum > maxi){
                maxi = sum;
                maxLength = j - i + 1;
            }
        }
    }

    return maxLength;
}


int main(){

    vector<int>arr{1, -2, 3, 4, -1, 2, 1, -5, 4};

    cout<<"Length of Maximum Sub Array Sum:- ";     // [3, 4, -1, 2, 1]
    cout<<lengthOfMaxSubarraySum(arr);


    return 0;
}