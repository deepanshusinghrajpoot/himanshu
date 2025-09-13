

/*


2. Frequency Count (Best Approach)
----------------------------------

Count frequency of each character in both strings.


Compare counts.





*/




#include<iostream>
#include<bits/stdc++.h>
using namespace std;



bool isAnagram(string s1, string s2){

    if(s1.length() != s2.length()) return false;

    int freq[256] = {0};

    for(char ch : s1) freq[ch]++;
    for(char ch : s2) freq[ch]--;

    for(int i=0; i<256; i++){
        if(freq[i] != 0) return false;
    }

    return true;
}



int main(){

    string s1, s2;
    cout<<"Enter string s1 : ";
    cin>>s1;

    cout<<"Enter string s2 : ";
    cin>>s2;

    
    if(isAnagram(s1, s2)) cout<<"Yes, It is a anagram!";
    else cout<<"Not, It is not a anagram!";

    return 0;
}





/*

T.C = O(n)
S.C = O(1)

*/