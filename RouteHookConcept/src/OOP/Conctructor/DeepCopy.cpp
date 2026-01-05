#include<bits/stdc++.h>
#include<iostream>
using namespace std;

/*

Deep Copy
---------

A deep copy, on other hand,
not only copies the member values but makes copies of
any dynamically allocated memory on heap that the members point to.




*/


class Student {

    public:
      string name;
      double* cgpaPtr;        //  👉 This means cgpaPtr is a pointer to a double.

    Student (string name, double cgpa){
        this->name = name;
        cgpaPtr = new double;    // creates a new memory (say address 555)
        *cgpaPtr = cgpa;         // store value (cgpa) in that memory
    }

    Student (Student & orgObj){
        this->name = orgObj.name;
        cgpaPtr = new double;       // creates NEW memory (say address 567)
        *cgpaPtr = *orgObj.cgpaPtr; // copies value, not address    *cgpaPtr is same as  *this->cgpaptr
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


/*




🔑 Pointer Concepts in C++
-----------------------------

1. Pointer only stores addresses

A pointer variable does not store a value directly, it stores the memory address of another variable.

int a = 10;
int* p = &a;   // p stores the address of a


👉 p contains address of a, not the value 10.




2. Dereferencing a pointer (*)
------------------------------

To access the value at the address stored by a pointer, we use the * operator.

cout << *p;  // prints 10


👉 *p means “go to the address stored in p and read the value”.





3. Pointer to pointer
---------------------

A pointer can store the address of another pointer.

int a = 10;
int* p = &a;
int** q = &p;


👉 q stores the address of p, and *q gives the value of p (address of a).





4. Dynamic memory with new
--------------------------

We can allocate memory during runtime using new.

int* p = new int;  // creates memory for 1 integer
*p = 20;


👉 A new memory block is created (say address 555), and p stores 555.






5. Deleting memory (delete)
---------------------------

Memory allocated with new must be freed using delete to avoid memory leaks.

delete p;  // frees memory at address 555
p = nullptr; // good practice







6. Shallow Copy vs Deep Copy
----------------------------

Shallow Copy: Two objects share the same memory address (dangerous).

Deep Copy: Each object gets its own separate memory, but with the same value.

// shallow copy
this->cgpaPtr = orgObj.cgpaPtr;  

// deep copy
cgpaPtr = new double;
*this->cgpaPtr = *orgObj.cgpaPtr;









7. Null Pointer
---------------

A pointer that doesn’t point anywhere (safe initialization).

int* p = nullptr;










8. Dangling Pointer
-------------------

A pointer pointing to a freed memory.

int* p = new int(10);
delete p;   // memory freed
// p is now dangling (still stores old address)


👉 Always assign p = nullptr; after delete.







9. Pointer Arithmetic
---------------------

Since pointers store addresses, we can move them using + or -.

int arr[3] = {10, 20, 30};
int* p = arr;
cout << *p;     // 10
cout << *(p+1); // 20


📌 In short for interview:


Pointers store addresses.
* is used to access values (dereference).
new allocates, delete frees memory.
Deep copy uses *this->ptr = *obj.ptr.

Avoid dangling/null pointer issues.
Pointer arithmetic helps in arrays.











🔑 Key Concept: How Pointer Works Here
---------------------------------------

cgpaPtr is a pointer variable → it stores an address of a memory location on the heap.

*cgpaPtr → accesses the value stored at that address.

new double → allocates memory in heap and returns its address.

By creating a new memory in copy constructor, you ensured a deep copy (separate memory for each object).








Yes ✅ both are the same in meaning. Let me explain carefully:
--------------------------------------------------------------

Code 1
cgpaPtr = new double;
*this->cgpaPtr = *orgObj.cgpaPtr;

Code 2
cgpaPtr = new double;
*cgpaPtr = *orgObj.cgpaPtr;

Why same?

👉 Inside a non-static member function of a class, when you write cgpaPtr, it is automatically treated as this->cgpaPtr.

So:

*this->cgpaPtr → Dereference the pointer that belongs to the current object.

*cgpaPtr → Same thing (compiler implicitly adds this->).


👉 Both work identically and copy the value into a new memory block (deep copy).

🔑 Rule of thumb:

Writing this-> is optional (but sometimes used for clarity).

*cgpaPtr and *this->cgpaPtr are equivalent inside class methods.




*/