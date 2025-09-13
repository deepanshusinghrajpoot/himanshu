/*



Polymorphism
------------

Polymorphism is the ability of objects to take on different forms or behave in different 
way depending on the context in which they are used.

eg:- Classical Example

  (1) Constructor Overloading  :- When a class has more than one constructor with the same name but different number or type of parameters, it is called constructor overloading.


Type of Ploymorphism
--------------------

(1). Compile Time Polymorphism → When the decision about which method/function/operator to call is made at compile time.
👉 Example: Function Overloading, Operator Overloading, Constructor Overloading.


(2). Run Time Polymorphism → When the decision about which method to call is made at runtime, using inheritance and virtual functions.
👉 Example: Function Overriding with virtual functions.





*/



// Example of COnstructor Overloading

#include<bits/stdc++.h>
#include<iostream>
using namespace std;


class Student {
    public:
      string name;

    
    Student(){
        cout<<"non-parametarise constructor!"<<endl;
    }

    Student(string name){
        this->name = name;
        cout<<"parametarise constructor!"<<endl;
    }
    
};


int main(){

    Student s1("Himanshu Singh");

    return 0;
}