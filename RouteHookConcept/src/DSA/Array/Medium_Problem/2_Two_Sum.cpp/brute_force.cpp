



/*




=========== TWO SUM (BRUTE FORCE APPROACH) ===========

Problem:
-----------------------------------------------------------
Given an array and a target value,
find indices of TWO numbers such that:

arr[i] + arr[j] = target

Return indices (i, j)
If no pair exists → return (-1, -1)

-----------------------------------------------------------
Approach Used:
-----------------------------------------------------------

Brute Force using TWO nested loops

-----------------------------------------------------------
Core Idea:
-----------------------------------------------------------

• Fix first element using outer loop (i)
• Check every next element using inner loop (j)
• Compare sum of arr[i] + arr[j] with target

-----------------------------------------------------------
Algorithm Flow:
-----------------------------------------------------------

1️⃣ Loop i from 0 to n-1
2️⃣ Loop j from i+1 to n-1
3️⃣ If arr[i] + arr[j] == target
    → return {i, j}
4️⃣ If no pair found
    → return {-1, -1}

---------






*/















#include<bits/stdc++.h>
using namespace std;



vector<int>two_sum(vector<int>&arr, int target){

    for(int i=0; i<arr.size(); i++){
        for(int j=i+1; j<arr.size(); j++){
            if(arr[i] + arr[j] == target){
                return {i, j};
            }
        }
    }

    return {-1, -1};
}




int main(){

    vector<int>arr{3, 4, 2, 5, 6, 0, 8, 9};

    cout<<"Two Sum Problem :- ";
    vector<int>ans = two_sum(arr, 12);
    for(int i=0; i<ans.size(); i++){
        cout<<ans[i]<<" ";
    }

    return 0;
}