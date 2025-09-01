

#include<iostream>
#include<string>
using namespace std;


/*


    Classes & Objects
    -----------------

    . Class is a blueprint/template that defines properties (data) 
      and behaviors (functions).

    . Object is an instance of a class, representing a real-world entity.

    . Many objects can be created from one class.

    
    Real life example
    -----------------

    👉 “A class is like a blueprint, and an object is a real-world instance of it.
        For example, consider a Teacher class. It has properties like name, dept, subject, and salary.
        From this class, I can create objects like Teacher t1 (Deepanshu Singh, Computer Science, C++ teacher) or
        Teacher t2 (Rahul Sharma, Mathematics, Algebra teacher).


    Access Modifiers
    ----------------

    private:  data & member function accessible only inside class 

    protected: data & member function accessible inside base class & to its derived class

    public:   data & member function accessible to everyone

    Note:- All properties and methods inside the class are private by default.




    what is setter function and getter function?
    -------------------------------------------

    setter: A setter function is use to set the value of a private property.
    getter: A getter function is use to get the value of a private property.


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
    Teacher t1;

    t1.name = "Deepanshu Singh";
    t1.dept = "Computer Science";
    t1.subject = "C++";
    t1.setSalary(50000.50); // setting salary using setter
    


    cout << t1.name << endl;
    cout << t1.getSalary() << endl;


    return 0;
}






























