
/*

✅ Frequency of Characters in a String
1. Basic Loop + Array (ASCII)

👉 Works well for normal English letters.


*/





#include<bits/stdc++.h>
#include<bits/stdc++.h>
using namespace std;


void frequencyOfChar(string s){
   
     int freq[256] = {0};

     for(char ch : s) freq[ch]++;

     for(int i=0; i<256; i++){
        if(freq[i] > 0){
            cout<< (char)i << " -> " << freq[i] <<endl; 
        }
     }
}


int main(){

    string s;
    cout<<"Enter the string : ";
    getline(cin, s);

    frequencyOfChar(s);

    return 0;
}



/*

T.C = O(n)
S.C = O(1)

*/