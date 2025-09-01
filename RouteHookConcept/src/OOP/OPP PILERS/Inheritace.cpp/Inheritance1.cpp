

/*

        Inheritance
        -----------

       lll When properties & member functions of base class are passed on to the derived class.

            
            class A (Parent, Base)
               |
               |
               |
               |
               |      (inherit)
               -----> class B (Child, Derived)



       It is use for code reusability

       
       In Inheritance
       --------------

       1. Constructor calling order
       ----------------------------
       first call base class constructor
       then call derived class constructor
       or 
       first allocate memory of child class object
       then allocate memory of derived class constructor


       2. Destructor calling order
       ---------------------------
       It is opposit to constructor

       first deallocate memory of child class object
       then deallocate memory of parent class object



       lll 👉 “In inheritance, the base class constructor is called first, then the derived class constructor. 
       For destruction, it’s the opposite — derived class destructor first, then base class destructor.”


*/


#include<bits/stdc++.h>
#include<iostream>
using namespace std;



class Person {

   public:
       string name;
       int age;

   Person(){
        cout<< "Parent constructor ..." <<endl;
   }

   ~Person(){
        cout<< "Parent destructor ..." <<endl;
   }
};


class Student : public Person {
    
    // name, age, rollno

    public:
       int rollno;

       Student () {
        cout<< "Child constructor.." <<endl;
       }

       ~Student () {
        cout<< "Child destructor.." <<endl;
       }

       void getInfo(){
        cout<<"Student Name: "<< name <<endl;
        cout<<"Student Age: "<< age <<endl;
        cout<<"Student Rollno: "<< rollno << endl;
       }
};



int main () {

    Student s1;
    s1.name = "Deepanshu Singh";
    s1.age = 21;
    s1.rollno = 1234;

    s1.getInfo();

    return 0;
}