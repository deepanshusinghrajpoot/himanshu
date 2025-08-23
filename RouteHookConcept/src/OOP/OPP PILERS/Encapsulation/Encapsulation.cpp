
#include<bits/stdc++.h>
#include<iostream>
using namespace std;



/*

   OOPS Pilers
   -----------

   (1) Encapsulation
   (2) Abstraction
   (3) Inheritance
   (4) Polymorphism


   Encapsulation
   -------------

   Encapsulation is wrapping up of data & member function in a single unit called class.

           ------------------------------------------------------
           |  data/properties/attributes   |   member function  |
           ------------------------------------------------------

   Encapsulation is use for data hiding.
   we can hide properties using access modifiers(private).


*/



class Teacher {

    private:
        double salary; // data  hiding
    
    public:
        string name;
        string dept;
        string subject;


};



int main () {

    Teacher t1;

    t1.name = "Himanshu Singh";

    cout<< t1.name << endl;

    
    return 0;
}