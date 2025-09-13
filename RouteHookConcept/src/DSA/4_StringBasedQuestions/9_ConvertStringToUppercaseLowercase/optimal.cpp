

// Optimal Approch which is use to convert a string into lower and upper case



#include<iostream>
#include<bits/stdc++.h>
using namespace std;


string toUpperCase(string s){
  

    for(int i=0; i<s.size(); i++){
        if(s[i] >= 'a' && s[i] <= 'z'){
             s[i] = s[i] - 'a' + 'A';
        }
    }
    
    return s;
}


string toLowerCase(string s){
    
    for(int i=0; i<s.size(); i++){
        if(s[i] >= 'A' && s[i] <= 'Z'){
            s[i] = s[i] - 'A' + 'a';
        }
    }

    return s;
}


int main(){

    string s1, s2;
    cout<<"Enter the string s1 in lower case : ";
    getline(cin, s1);

    cout<<"String s1 convert into upper case : ";
    cout<<toUpperCase(s1)<<endl;


    cout<<"Enter the string s2 in upper case : ";
    getline(cin, s2);
    cout<<"String s2 convert into lower case : ";
    cout<<toLowerCase(s2)<<endl;

    return 0;
}



/*

T.C = O(n)
S.C = O(1)

*/

