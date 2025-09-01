/*




// if you want to more explore OOP concept then read
friend function 
friend class



*/



#include<bits/stdc++.h>
#include<iostream>
using namespace std;



class ABC{
    public:
       ABC(){
         cout<<"constructor"<<endl;
       }

       ~ABC(){
         cout<<"destructor"<<endl;
       }
};


int main(){
    if(true){
        static ABC obj;
    }

    cout<<"end of main function"<<endl;
}

