

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



    Access Modifiers
    ----------------

    private:  data & methods accessible inside class 

    public:   data & methods accessible to everyone

    protected: data & methods accessible inside class & to its derived class


    Note:- All properties and methods inside the class are private by default.




    what is setter and getter?
    --------------------------

    setter: A setter is use to set the value of a private property.
    getter: A getter is use to get the value of a private property.


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





