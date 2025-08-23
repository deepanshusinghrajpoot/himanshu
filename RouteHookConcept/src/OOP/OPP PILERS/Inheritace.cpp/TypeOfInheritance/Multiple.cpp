

/*


Multiple Inheritance
--------------------



(name, rollno)                         (subject, salary)
Student                                P.hD scholor
  |                                       |
  |                                       |
  -----------------------------------------
                          |
                          |
                 Teaching Assistant
                           

Multiple Inheritance → When a child class inherits features from more than one parent class. ✅


*/



#include<bits/stdc++.h>
#include<iostream>
using namespace std;


class Student {
    public:
       string name;
       int rollno;
};


class GradScholar{
    public:
      int salary;
      string researchArea;
};


class TeacherAssistant : public GradScholar, public Student{
    
};


int main () {

    TeacherAssistant t1;
    t1.name = "Deepanshu Singh";
    t1.rollno = 206532;
    t1.researchArea = "Quantum Physics";
    t1.salary = 30000;


    cout<<"Teacher Assistant Name: "<<t1.name<<endl; 
    cout<<"Teacher Assistant Rollno: "<<t1.rollno<<endl; 
    cout<<"Teacher Assistant ReearchArea: "<<t1.researchArea<<endl; 
    cout<<"Teacher Assistant Salary: "<<t1.salary<<endl;

}
