/*


✅ Anagram Check

👉 Definition: Two strings are anagrams if they contain the same characters in the same frequency, but possibly in a different order.
Example: "listen" and "silent" ✅ anagrams.






1. Sorting Approach (Basic)
---------------------------

Sort both strings.

If sorted versions are equal → anagrams.








*/






#include<iostream>
#include<bits/stdc++.h>
using namespace std;



bool isAnagram(string s1, string s2){

     if(s1.length() != s2.length()) return false;

     sort(s1.begin(), s1.end());
     sort(s2.begin(), s2.end());


     return s1 == s2;
}


int main(){

    string s1, s2;
    cout<<"Enter String s1 : ";
    cin>>s1;
    cout<<"Enter String s2 : ";
    cin>>s2;

    if(isAnagram(s1, s2)) cout<<"Yes, It is anagram!";
    else cout<<"Not, It is not a anagram!";


    return 0;
}


/*

⏱ Time Complexity: O(n log n) (sorting)
💾 Space Complexity: O(1)

*/