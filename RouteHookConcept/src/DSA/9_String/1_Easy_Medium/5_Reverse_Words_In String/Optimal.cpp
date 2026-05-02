





#include<bits/stdc++.h>
using namespace std;



    string reverse_sentence(string s){

        int left = 0;
        int right = s.size() - 1;

        while(left < right){
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;

            left++;
            right--;
        }


        return s;
    }


    string reverseWords(string s) {

       string sss = reverse_sentence(s);
       
       string ans = "";

       string word = "";

       for(int i=0; i<sss.length(); i++){
          
          char ch = sss[i];

          if(ch == ' '){
            if(!word.empty()){
                ans += reverse_sentence(word);
                ans += ' ';
                word = "";
            }
          }
          else{
            word += ch;
          }

       }
       if(!word.empty()) ans += reverse_sentence(word);

       
       if(ans[ans.size() - 1] == ' '){
          ans.pop_back();
       }
       return ans;
    }



int main(){

    string sentence = "    Hellow Deepanshu Kaise ho!    ";

    cout<<"Reverse word in given string:- ";
    cout<<reverseWords(sentence);

    return 0;
}