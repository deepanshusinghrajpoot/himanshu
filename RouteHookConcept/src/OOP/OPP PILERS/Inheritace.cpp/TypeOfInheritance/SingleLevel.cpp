

/*

 Type Of Inheritance
 -------------------

 (1) Single level inheritance
 (2) Multiple inheritance
 (3) Multi level inheritance



 Single Level Inheritance
 ------------------------

 Single Level Inheritance → When a class (child) inherits directly from only one parent class. ✅
 
 parent
   |
   |
   |
 child




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