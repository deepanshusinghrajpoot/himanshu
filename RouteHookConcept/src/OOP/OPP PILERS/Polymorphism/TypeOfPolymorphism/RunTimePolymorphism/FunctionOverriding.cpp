/*



Run Time Polymorphism
---------------------

(1). Function Overriding

    base class & derive class both contain the same function with different implementation.

    The base class function is said to be overridden.


*/


#include<bits/stdc++.h>
#include<iostream>
using namespace std;


class Parent {
    public:
       void getInfo(){
          cout<<"parent class"<<endl;
       }
};



class Child : public Parent{
    public:
        void getInfo(){
            cout<<"Child Class"<<endl;
        }
};


int main(){

    Child c1;
    c1.getInfo();

    return 0;
}


// output:- Child Class