/*

(2). Static Keyword with Objects
--------------------------------

. A static variable exists for the entire lifetime of the program.

. Static members belong to the class, not to individual objects.

. Only one copy is shared among all objects of the class.

. They are declared inside the class but defined outside.

. Can be accessed using object name or class name.




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

