/*



✅ Approach 3: Using Bitwise XOR (Best & Safe)
-----------------------------------------------


*/


#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Enter two numbers: ";
    cin >> a >> b;

    cout << "Before Swap: a=" << a << ", b=" << b << endl;

    a = a ^ b;
    b = a ^ b;
    a = a ^ b;

    cout << "After Swap: a=" << a << ", b=" << b << endl;
    return 0;
}


/*

👉 Time Complexity: O(1)
👉 Space Complexity: O(1)
✅ Works for all integers without overflow


*/