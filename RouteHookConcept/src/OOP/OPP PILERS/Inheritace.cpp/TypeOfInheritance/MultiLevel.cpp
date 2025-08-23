
/*
    Multiple Level Inheritance
    --------------------------

        Person (name, age)
               |
               |
               v
        Student (rollNo)
               |
               |
               v
        GraduateStudent (researchArea)

    Multilevel Inheritance → When a class is derived from another derived class, forming a chain of inheritance. ✅
*/




#include<bits/stdc++.h>
#include<iostream>
using namespace std;



class Person{
    public:
       string name;
       int age;
};


class Student : public Person{ 
    public:
       int rollno;
};


class GradStudent : public Student{
    public:
       string reasearch;
};


int main () {

    GradStudent s1;

    s1.name = "tony stark";
    s1.age = 1244;
    s1.reasearch = "Quantum Physics";


    cout<<"Graduate Student Name: "<<s1.name<<endl;
    cout<<"Graduate Student Age: "<<s1.age<<endl;
    cout<<"Graduate Student Reasearch: "<<s1.reasearch<<endl;

    return 0;
}