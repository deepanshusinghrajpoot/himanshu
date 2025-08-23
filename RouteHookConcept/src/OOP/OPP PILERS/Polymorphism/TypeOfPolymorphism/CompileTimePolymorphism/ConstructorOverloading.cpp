/*

  Compile Time Polymorphism
  -------------------------

  (1):- Constructor Overloading

  When a class has more than one constructor with the same name but different number or type of parameters, 
  it is called constructor overloading.

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