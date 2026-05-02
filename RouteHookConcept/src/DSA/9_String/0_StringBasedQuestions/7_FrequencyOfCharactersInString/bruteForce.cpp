




#include<iostream>
#include<bits/stdc++.h>
using namespace std;

void frequecyOfCharOfString(string s){

     map<char, int>map;

     for(char ch :  s) map[ch]++;

     for(auto it : map){
         cout<<it.first << " -> " <<it.second<<endl;
     }
}


int main(){

    string s;
    cout<<"Enter a string s : ";
    getline(cin, s);

    frequecyOfCharOfString(s);

    return 0;

}


/*

T.C = O(logn)

S.C = O(n)


*/