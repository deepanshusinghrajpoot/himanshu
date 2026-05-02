







#include<bits/stdc++.h>
using namespace std;


vector<string> find_words(string sentence){

    vector<string>words;
    string word = "";

    for(int i=0; i<sentence.length(); i++){

        char ch = sentence[i];

        if(ch == ' '){
            if(!word.empty()){
                words.push_back(word);
                word = "";
            }
        }
        else{
            word += ch;
        }
    }
    if(!word.empty()) words.push_back(word);

    return words;
}



string reverse_word_in_sentence(string sen){

      vector<string>words = find_words(sen);

      string sentence = "";

      for(int i=words.size()-1; i>=0; i--){
        sentence += words[i];
        sentence += ' ';
      }

      return sentence;
}




int main(){

    string sentence = "Hellow Deepanshu Kaise ho!";

    cout<<"Reverse word in given string:- ";
    cout<<reverse_word_in_sentence(sentence);

    return 0;
}