/*



14. Swap Two Numbers Without Using 3rd Variable


✅ Approach 1: Using Addition & Subtraction
--------------------------------------------


*/




#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Enter two numbers: ";
    cin >> a >> b;

    cout << "Before Swap: a=" << a << ", b=" << b << endl;

    a = a + b;  // Step 1
    b = a - b;  // Step 2
    a = a - b;  // Step 3

    cout << "After Swap: a=" << a << ", b=" << b << endl;
    return 0;
}

/*

👉 Time Complexity: O(1)
👉 Space Complexity: O(1)
⚠️ May cause overflow if numbers are very large

*/