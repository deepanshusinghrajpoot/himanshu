

/*



1. Using Frequency Array (Efficient for ASCII)
----------------------------------------------

👉 Count first, then scan.



🔹 Input: "swiss"
🔹 Output: w


*/







#include<iostream>
#include<bits/stdc++.h>
using namespace std;



char firstNonRepeatingChar(string s){

    int freq[256] = {0};

    for(char ch : s)  freq[ch]++;

    for(char ch : s){
        if(freq[ch] == 1) return ch ;
    }

    return  '\0';
}


int main(){

    string s;
    cout<<"Enter the a string s : ";
    getline(cin, s);

    cout<<"first non-reoeating charactor : "<<firstNonRepeatingChar(s)<<endl;

    return 0;
}


/*

T.C = O(n)
S.C = O(1)


*/



