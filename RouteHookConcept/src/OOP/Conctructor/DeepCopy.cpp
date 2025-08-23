#include<bits/stdc++.h>
#include<iostream>
using namespace std;

/*

Deep Copy
---------

A deep copy, on other hand, not only copies the member values but also makes copies of
any dynamically allocated memory that the members point to.




*/


class Student {

    public:
      string name;
      double* cgpaPtr;

    Student (string name, double cgpa){
        this->name = name;
        cgpaPtr = new double;   // asume address 555
        *cgpaPtr = cgpa;
    }

    Student (Student & orgObj){
        this->name = orgObj.name;
        cgpaPtr = new double;   // asume address 567
        *cgpaPtr = *orgObj.cgpaPtr;
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


    s2.name = "Deepanshu Singh";
    s2.getInfo();

    return 0;
}