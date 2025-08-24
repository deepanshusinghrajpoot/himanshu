
/*

Destructor
----------

Destructor is opposite of Constructor

Constructor :- Is used to allocate the memory  
Destructor  :- Is used to deallocate the memory  

Note :- When we do not make a destructor to deallocate the object,  
        then compiler automatically provides a default destructor. 
        
        lll If we are not make destructor to compiler make a default destructor automatically

Dynamic memory allocation and deallocation are done by our own implementation  
of Constructor and Destructor.  

--------------------------------------------------------------------------------

But when we allocate memory dynamically using :- new keyword  
then this memory is deallocated using :- delete keyword  



*/







#include<bits/stdc++.h>
#include<iostream>
using namespace std;


class Student {

    public:
      string name;
      double* cgpaPtr;

    Student (string name, double cgpa){
        this->name = name;
        cgpaPtr = new double;   // asume address 555
        *cgpaPtr = cgpa;
    }

    // destructor
    ~Student(){
        cout<< "Hi, I delete everything" <<endl;
        delete cgpaPtr;
    }


    void getInfo(){
        cout<< name << endl;
        cout<< *cgpaPtr << endl;
    }
};


int main() {

    Student s1("rahul kumar", 8.9);
    
    s1.getInfo();

    return 0;
}