

/*



Hierarchical Inheritance
------------------------


                  parent
                     |
                     |
                     |
            ------------------
            |                |
            |                | 
          child-1          child-2

Hierarchical Inheritance → When multiple child classes inherit from a single parent class. ✅


*/


#include<bits/stdc++.h>
#include<iostream>
using namespace std;




class Person{
    public:
       string name;
       int age;
};


class Student : public Person {
    public:
      int rollno;    
};


class Teacher : public Person {
    public:
      string subject; 
};



int main(){

    Teacher t1;
    t1.name = "Deepanshu";
    t1.subject = "Computer Science";

    Student s1;
    s1.name = "Himanshu";
    s1.rollno = 36154182;

    cout<<"Teacher Name: "<<t1.name<<endl;
    cout<<"Teacher Rollno: "<<t1.subject<<endl;

    cout<<"Student Name: "<<s1.name<<endl;
    cout<<"Student Rollno: "<<s1.age<<endl;

    return 0;
}

