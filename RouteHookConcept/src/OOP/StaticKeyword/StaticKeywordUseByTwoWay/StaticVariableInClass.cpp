

#include<bits/stdc++.h>
using namespace std;

class A {
public:
    static int x;   // static variable (shared by all objects)

    void incX() {
        x++;
    }
};





// static variable must be defined outside the class
int A::x = 0;





int main() {

    A obj1;
    A obj2;

    obj1.x = 100;   // modifies static x (shared)
    obj2.x = 200;   // modifies same static x again

    cout << obj1.x << endl;  // Output: 200
    cout << obj2.x << endl;  // Output: 200

    return 0;

}
