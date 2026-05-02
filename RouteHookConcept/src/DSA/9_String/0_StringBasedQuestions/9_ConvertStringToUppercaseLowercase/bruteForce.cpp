




#include<iostream>
#include<bits/stdc++.h>
using namespace std;



string converUpperCase(string s){

    for(int i=0; i<s.size(); i++){
        if(islower(s[i])) s[i] = toupper(s[i]);
    }

    return s;
}


string convertLowerCase(string s){

    for(int i=0; i<s.size(); i++){
        if(isupper(s[i])) s[i] = tolower(s[i]);
    }

    return s;
}






int main(){

    string s1, s2;
    cout<<"Enter the string s1 in lower case : ";
    getline(cin, s1);

    cout<<"String s1 convert into upper case : ";
    cout<<converUpperCase(s1)<<endl;


    cout<<"Enter the string s2 in upper case : ";
    getline(cin, s2);
    cout<<"String s2 convert into lower case : ";
    cout<<convertLowerCase(s2)<<endl;

    return 0;
}


/*


T.C = O(n);
S.C = O(1);


*/