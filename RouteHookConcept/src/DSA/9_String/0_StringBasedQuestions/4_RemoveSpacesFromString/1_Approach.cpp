
// 4. Remove spaces from string


#include<iostream>
#include<bits/stdc++.h>
using namespace std;


string removeSpace(string s){

    string temp;

    for(char ch : s){
        if(ch != ' '){
             temp += ch;
        }
    }

    return temp;
}



int main(){

    string s;
    cout<<"Enter the string : ";
    getline(cin, s);

    cout<<"After removing : ";
    cout<<removeSpace(s)<<endl;

    return 0;
}



/*


T.C = O(n)
S.C = O(1)


*/