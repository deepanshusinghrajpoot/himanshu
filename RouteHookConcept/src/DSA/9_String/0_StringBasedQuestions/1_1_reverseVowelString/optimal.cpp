

#include<bits/stdc++.h>
using namespace std;



bool isVowel(char ch){
     return  ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' 
             || ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U'; 
}



string reverseVowel(string s){

     int left = 0;
     int right = s.length()-1;
     
     while(left < right){
        
        while(left < right && !isVowel(s[left])) left++;
        while(left < right && !isVowel(s[right])) right--;

        if(left < right){
            char ch = s[left];
            s[left] = s[right];
            s[right] = ch;

            left++;
            right--;
        }
        
     }

     return s;

}





int main(){

    string s;
    cout<<"Enter the word:- ";

    cin>>s;

    cout<<reverseVowel(s);
    
  
    return 0;
}
