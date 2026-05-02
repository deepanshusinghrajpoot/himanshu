

/*

Function Code (Brute Force Rotation Check)
------------------------------------------


Time Complexity: O(N²)
Space Complexity: O(N)

*/





#include<iostream>
#include<bits/stdc++.h>
using namespace std;



bool checkStringRotateOfAnother(string s1, string s2){

    if(s1.size() != s2.size()) return false;


    for(int i=0; i<s1.size(); i++){

        string rotate = s1.substr(i) + s1.substr(0, i);

        if(rotate == s2) return true;

    }

    return false;
}



int main(){

    string s1, s2;
    cout<<"Enter the string s1 : ";
    cin>>s1;
    cout<<"Enter the string s2 : ";
    cin>>s2;

    if(checkStringRotateOfAnother(s1, s2)) cout<<"Yes , This string is rotate of s2";
    else cout<<"No, This string is not rotate of s2";

    return 0;
}





/*








Form a rotated version
----------------------

string rotated = s1.substr(i) + s1.substr(0, i);



👉 Here’s the trick:
---------------------

s1.substr(i) → takes substring from index i to end.
s1.substr(0, i) → takes substring from start to index i-1.

Concatenating both simulates a rotation at position i.


Example:

s1 = "ABCD", n = 4

i = 0 → "ABCD"
i = 1 → "BCDA"
i = 2 → "CDAB" ✅
i = 3 → "DABC"




*/
