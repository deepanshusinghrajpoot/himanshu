#include<bits/stdc++.h>
#include<iostream>
using namespace std;

/*

Shallow Copy
-------------------

A shallow copy of an object copies all of the member values from one object to another.




*/


class Student {

    public:
      string name;
      double* cgpaPtr;

    Student (string name, double cgpa){
        this->name = name;
        cgpaPtr = new double;
        *cgpaPtr = cgpa;
    }

    Student (Student & orgObj){
        this->name = orgObj.name;
        this->cgpaPtr = orgObj.cgpaPtr;
    }


    void getInfo(){
        cout<< name << endl;
        cout<< *cgpaPtr << endl;
    }
};


int main() {

    Student s1("rahul kumar", 8.9);
    
    Student s2(s1);

    s1.getInfo();
    *(s2.cgpaPtr) = 9.2;
    s1.getInfo();

    return 0;
}