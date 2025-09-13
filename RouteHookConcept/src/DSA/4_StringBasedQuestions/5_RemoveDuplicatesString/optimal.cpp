

// remove dublicate from string



#include<iostream>
using namespace std;



string removeDublicate(string s){

    bool seen[256] = {false};

    string result;

    for(char ch : s){
        if(!seen[ch]){
            seen[ch] = true;
            result += ch;
        }
    }

    return result;
}


int main(){

    string s;
    cout<<"Enter a string : ";
    getline(cin, s);

    cout<<"After removing dublicate : ";
    cout<<removeDublicate(s)<<endl;

    return 0;
}


/*


T.C = O(n)
S.C = O(1)


*/