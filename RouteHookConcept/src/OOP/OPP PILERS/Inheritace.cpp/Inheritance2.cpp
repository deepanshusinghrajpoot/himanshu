

/*

        Inheritance
        -----------

        When properties & member functions of base class are passed on to the derived class.

            
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



Mode of Inheritance
-------------------

| (Parent Class) Base Class | Derived Class (Private Inheritance) | Derived Class (Protected Inheritance) | Derived Class (Public Inheritance) |
|---------------------------|-------------------------------------|---------------------------------------|------------------------------------|
| Private                   | Not Inherited                       | Not Inherited                         | Not Inherited                      |
| Protected                 | Private                             | Protected                             | Protected                          |
| Public                    | Private                             | Protected                             | Public                             |


📖 Explanation Line by Line
1. Base Class → Private Members

Not inherited in any mode.
👉 Derived class objects cannot access base class private members. 
They are only accessible inside the base class itself (unless you use friend functions).



2. Base Class → Protected Members

If derived privately, they become private in derived class.
If derived protectedly, they remain protected in derived class.
If derived publicly, they remain protected in derived class.

👉 Protected means: accessible inside the base and derived classes, but not outside (via object).



3. Base Class → Public Members

If derived privately, they become private in derived class.
If derived protectedly, they become protected in derived class.
If derived publicly, they remain public in derived class.

👉 So public inheritance maintains the same access level, while private/protected inheritance restricts it.



*/



#include<bits/stdc++.h>
#include<iostream>
using namespace std;



class Person {

 public:
       string name;
       int age;

  Person(string name, int age){
    this->name = name;
    this->age = age;
  }
   
};


class Student : public Person {
    
    // name, age, rollno

    public:
       int rollno;

       Student(string name, int age, int rollno) : Person(name, age){
          this->rollno = rollno;
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

    Student s1("rahul kumar", 21, 1234);

    s1.getInfo();

    return 0;
}