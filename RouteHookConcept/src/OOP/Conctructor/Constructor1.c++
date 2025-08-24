#include <bits/stdc++.h>
#include <iostream>
using namespace std;



/*

Constructor
-----------

Special method invoked automatically at time of object creation. Used for Initialization.


       properties
       ----------

       1. Constructor have Same name as class
       2. Constructor doesn't have a return type
       3. Constructor is called only once (automaticaly), at object creation
            if we are not make constructor, compiler make default constructor automaticaly.
       4. Memory allocation happens when constructor is called
          So,
            Memory allocation is happen for object not for class.
            


       Type of Constructor
       -------------------

       There are three type of constructor

       1. Non-parameterize constructor
       2. Parameterize constructor
       3. Copy Constructor





       Non-Parameterized Constructor

lll 👉 A constructor which does not take any parameter is called a non-parameterized constructor.
It assigns default values to the object’s data members.

Parameterized Constructor

lll 👉 A constructor which takes parameters is called a parameterized constructor.
It allows us to assign custom values to the object’s data members at the time of creation.

       

*/





class Teacher {
 
 private:
    double salary;




 public:
    // properties or attribute
    string name;
    string dept;
    string subject;

    


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


};


int main () {

    // objects
    Teacher t1;    // at time of object creation, constructor is invoked automatically. Here compliper make constructor automaticaly. 
                   // Constructor is made by compiler or programmer.

    t1.name = "Deepanshu Singh";
    t1.dept = "Computer Science";
    t1.subject = "C++";
    t1.setSalary(50000.50); // setting salary using setter
    


    cout << t1.name << endl;
    cout << t1.getSalary() << endl;


    return 0;
}


