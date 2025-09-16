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



*/





class Teacher {
 
 private:
    double salary;




 public:

 
    // properties or attribute
    string name;
    string dept;
    string subject;
   



    
    // Non-parameterize constructor
    Teacher(){
        cout<< "Hi, I'm a constructor. I am call automatically at the time of object creation." << endl;
         name = "Default Name";
         dept = "Default Department";
         subject = "Default Subject";
         salary = 237645726;
    }


    // Parametrize constructor
    Teacher(string n, string d, string s){
         name = n;
         dept = d;
         subject = s;
    }
    

    Teacher(string name, string dept, string subject, double salary){
         this->name = name;
         this->dept = dept;
         this->subject = subject;
         this->salary = salary;
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

    // objects
    Teacher t1;    // at time of object creation, constructor is invoked automatically. Here compliper make constructor automaticaly. 
                   // Constructor is made by compiler or programmer.
    t1.getInfo();



    Teacher t2("Rohan Singh", "Information Technology", "C++", 25000);
    
    Teacher t3(t2);  // default copy constructor call 


    t1.name = "Deepanshu Singh";
    t1.subject = "C++";
    t1.setSalary(50000.50); // setting salary using setter
    


    cout << t1.name << endl;
    cout << t1.getSalary() << endl;
    cout << t1.dept << endl;


    return 0;
}


