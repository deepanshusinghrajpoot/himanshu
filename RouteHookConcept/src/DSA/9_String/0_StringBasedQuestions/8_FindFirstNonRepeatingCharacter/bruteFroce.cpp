

/*



Brute force approach
--------------------





*/





#include<iostream>
#include<bits/stdc++.h>
using namespace std;



char firstNonRepeatingChar(string s){

    map<char, int>map;

    for(char ch : s) map[ch]++;

    for(char ch : s){
        if(map[ch] == 1) return ch;
    }

    return '\0';
}


int main(){

    string s;
    cout<<"Enter the a string s : ";
    getline(cin, s);

    cout<<"first non-reoeating charactor : "<<firstNonRepeatingChar(s)<<endl;

    return 0;
}



/*


T.C = O(logn)
S.C = O(n)



*/






