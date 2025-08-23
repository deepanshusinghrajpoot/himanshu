
/*

Abstraction
-----------

(Using Abstract Classes)

. Abstraction is the process of hiding implementation details 
  and showing only essential features to the user.

. Abstract classes are used to provide a base class 
  from which other classes can be derived.

. They cannot be instantiated (objects of abstract classes 
  cannot be created).

. Abstract classes are created using at least one **pure virtual function**.

. They are meant to be inherited by derived classes 
  which provide the actual implementation.

*/


#include<bits/stdc++.h>
using namespace std;


// A class that contains at least one pure virtual function 
// automatically becomes an Abstract Class.

class Shape {
public:
    virtual void draw() = 0;  // pure virtual function
};


class Circle : public Shape {
    public:
      void draw(){
        cout<<"Drawing a circle"<<endl;
      }
};



int main(){

    Circle c1;
    c1.draw();
    
    return 0;
}


