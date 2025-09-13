





#include<iostream>
using namespace std;



string removeDublicate(string s){

     string result;
     for(int i=0; i<s.length(); i++){
        bool found = false;
        for(int j=0; j<result.length(); j++){
            if(s[i] == result[j]){
                found = true;
                break;
            }
        }
        if(!found) result += s[i];
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


T.C = O(n^2)
S.C = O(1)


*/