


#include<iostream>
#include<bits/stdc++.h>
using namespace std;




string longestWordInSentence(string s){

    string word, longest;

    stringstream ss(s);  // T.C = O(n)   , S.C = O(n)

    while(ss >> word){          // T.C = O(n)
        if(word.size() > longest.size()){
            longest = word;
        }
    }

    return longest;
}








int main(){
    string s;
    cout<<"Enter the sentence s : ";
    getline(cin, s);


    cout<<"Longest word in the sentence is : "<<longestWordInSentence(s)<<endl;

    return 0;
}



/*


T.C = O(n) + O(n)  = O(n)
S.C = O(n)


*/

