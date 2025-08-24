#include <bits/stdc++.h>
#include <iostream>
using namespace std;



/*




       Type of Constructor
       -------------------

       1. Non-parameterize constructor
       2. Parameterize constructor
       3. Copy Constructor



Definition: Constructor Overloading |- is an example of polymorphism

Constructor overloading in Object-Oriented Programming (OOP) is a concept where a class can have multiple constructors 
with the same name but different parameter lists (number or type of parameters).

The compiler determines which constructor to call based on the arguments passed during object creation.




this
----

this is a special pointer in C++ that points to the current object.

this->prop is same as *(this).prop


Copy Constructor
----------------
👉 A constructor which creates a new object as a copy of an existing object is called a copy constructor.

1. Shallow Copy
2. Deep Copy



*/





class Teacher {
 
 private:
    double salary;




 public:

 
    // properties or attribute
    string name;
    string dept;
    string subject;
   

    // Parametrize constructor
    Teacher(string n, string d, string s, double sal){
         name = n;
         dept = d;
         subject = s;
         salary = sal;
    }

     Teacher( Teacher &orgObj){
         this->name = orgObj.name;
         this->dept = orgObj.dept;
         this->subject = orgObj.subject;
         this->salary = orgObj.salary;
    }



    // methods or member functions

    void changeDept(string newDept){
        dept = newDept;
    }





    // setter
    void setSalary(double newSalary){
        salary = newSalary;
    }

    // getter
    double getSalary(){
        return salary;
    }


    void getInfo(){
        cout<< "name :" << name << endl;
        cout<< "dept :" << dept << endl;
        cout<< "sub :" << subject << endl;
        cout<< "salary :" << salary << endl;
    }


};


int main () {



    Teacher t2("Rohan Singh", "Information Technology", "C++", 25000);
    
    Teacher t3(t2);  // copy constructor call 

    t3.getInfo();



    return 0;
}


