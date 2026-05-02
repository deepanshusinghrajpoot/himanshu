


#include<iostream>
#include<bits/stdc++.h>
using namespace std;


bool isAnagram(string s1, string s2){

    if(s1.length() != s2.length()) return false;

    unordered_map<char, int>unmap;

    for(char ch : s1)  unmap[ch]++;
    for(char ch : s2) unmap[ch]--;

    for(auto it : unmap){
        if(it.second != 0) return false;
    }

    return true;
}



int main(){

    string s1, s2;
    cout<<"Enter a string s1 : ";
    cin>>s1;

    cout<<"Enter a string s2 : ";
    cin>>s2;

    if(isAnagram(s1, s2)) cout<<"Yes, It is anagram!";
    else cout<<"Not, it is not a anagram!";

    return 0;
}


/*


T.C = O(1) -> average , and best case
T.C = O(n) -> worst case


S.C = O(n)



*/