

/*





✅ Problem: Find the Longest Word in a Sentence

Example:
👉 Input: "I love programming very much"
👉 Output: "programming" (length = 11)





1. Basic Approach (Using Loops, No Extra Libraries)





*/





#include<iostream>
#include<bits/stdc++.h>
using namespace std;



string longestWordInSentence(string s){


    int currLen = 0,    maxLen = 0,    maxStart = 0,   start = 0;

    for(int i=0; i<s.size();  i++){
        
        if(i < s.size() && s[i] != ' '){
            currLen++;
        }
        else{  
            if(currLen > maxLen){
                maxLen = currLen;
                maxStart = start;
            }

            currLen = 0;
            start = i + 1;
        }
    }


    return s.substr(maxStart, maxLen);
}




int main(){
    string s;
    cout<<"Enter the sentence s : ";
    getline(cin, s);


    cout<<"Longest word in the sentence is : "<<longestWordInSentence(s)<<endl;

    return 0;
}



/*


T.C = O(n)
S.C = O(1)





substr(start, length) in C++
substr(pos, len) → returns a substring starting from index pos, of length len.
If len goes beyond the string size, it automatically stops at the end.

*/