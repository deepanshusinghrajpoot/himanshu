
#include<iostream>
#include<bits/stdc++.h>
using namespace std;


vector<string> findWord(string sentence){
      
    vector<string>words;
    string word = "";

    for(int i=0; i<sentence.length(); i++){

        char c = sentence[i];

        if(c == ' '){
            if(!word.empty()){
                words.push_back(word);
                word = "";
            }
        }
        else{
            word += c;
        }
    }

    if(!word.empty()) words.push_back(word);

    return words;
}






int main(){

    string s;
 
    cout<<"Enter the sentence!";
    getline(cin, s);  
    
 
    vector<string>words = findWord(s);


    for(string s : words){
        cout<<s<<endl;
    }

    for(int i=0; i<words.size(); i++){
      cout<<i<<" -> "<<words[i]<<endl;
    }

    return 0;
}