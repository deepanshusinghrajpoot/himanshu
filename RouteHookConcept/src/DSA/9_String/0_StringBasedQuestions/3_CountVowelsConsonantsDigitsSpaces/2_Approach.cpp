/*


🔹 Problem Statement

Given a string, count the number of:

Vowels → a, e, i, o, u (both cases)
Consonants → other alphabets
Digits → 0–9
Spaces




*/



#include <iostream>
#include <cctype>   // for isalpha, isdigit, isspace, tolower
using namespace std;

int main() {
    string str;
    cout << "Enter a string: ";
    getline(cin, str);   // take full line input

    int vowels = 0, consonants = 0, digits = 0, spaces = 0;

    for(char ch : str) {
        ch = tolower(ch); // case-insensitive check

        if(isalpha(ch)) {  // check if alphabet
            if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
                vowels++;
            else
                consonants++;
        }
        else if(isdigit(ch))
            digits++;
        else if(isspace(ch))
            spaces++;
    }

    cout << "Vowels: " << vowels << endl;
    cout << "Consonants: " << consonants << endl;
    cout << "Digits: " << digits << endl;
    cout << "Spaces: " << spaces << endl;

    return 0;
}


/*
  
   T.C = O(n)
   S.C = O(1)


*/