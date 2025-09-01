
/*






Run Time Polymorphism
---------------------

(1). Virtual Function

    A virtual function is a member function in the base class that can be 
    redefined (overridden) in a derived class. 
    It supports achieving run time polymorphism.

Properties
----------
1. Virtual functions are **dynamic in nature** (decided at runtime).
2. Defined using the keyword **virtual** inside a base class.
3. Overridden in a derived (child) class.

4. When called using a base class pointer/reference, 
   the **derived class version executes at runtime**.
   
5. Helps implement **dynamic method dispatch**.





*/




#include<bits/stdc++.h>
#include<iostream>
using namespace std;



class Parent{
    public:
       void getInfo(){
           cout<<"Parent Class"<<endl;
       }

       virtual void hello(){
            cout<<"Hello from parent"<<endl;
       }
};


class Child : public Parent {
    public:
       void hello(){
          cout<<"Hello from child"<<endl;
       }
};



int main(){

    Child c1;
    c1.hello();

    return 0;
}