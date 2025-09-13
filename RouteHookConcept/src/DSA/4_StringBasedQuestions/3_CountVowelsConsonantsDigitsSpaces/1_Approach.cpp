
#include<iostream>
using namespace std;



void printNumberofVowelConsonantDigitSpace(string s){

    int vowel = 0, consonant = 0, digit = 0, space = 0;

    for(int i=0; i<s.length(); i++){
       
         if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U'){
            vowel++;
         }
         else if((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z')){
            consonant++;
         }
         else if(s[i] >= '0' && s[i] <= '9'){
            digit++;
         }
         else if(s[i] == ' '){
            space++;
         }
    }



    cout<<"total vowel : "<<vowel<<endl; 
    cout<<"total consonant : "<<consonant<<endl; 
    cout<<"total digit : "<<digit<<endl; 
    cout<<"total space : "<<space<<endl; 
     
}





int main(){


    string s;
    cout<<"Enter a string :";
    getline(cin, s);


    printNumberofVowelConsonantDigitSpace(s);

    return 0;
}


/*


T.C = O(n);
S.C = O(1);


*/