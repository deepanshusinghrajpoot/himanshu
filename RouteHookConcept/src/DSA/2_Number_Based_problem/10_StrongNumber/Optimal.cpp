/*

✅ Definition: Strong Number

A number is called a Strong Number if the sum of the factorials of its digits is equal to the number itself.

Examples:
   145 → 1! + 4! + 5! = 1 + 24 + 120 = 145 ✅ (Strong Number)
   123 → 1! + 2! + 3! = 1 + 2 + 6 = 9 ❌ (Not Strong)





✅ Code in C++ (Efficient)


*/


#include<bits/stdc++.h>
#include <iostream>
using namespace std;

// Function to calculate factorial of a digit (0–9)
int factorial(int n) {
    int fact = 1;
    for (int i = 1; i <= n; i++) {
        fact *= i;
    }
    return fact;
}

bool isStrong(int n) {
    int original = n;
    int sum = 0;

    while (n > 0) {
        int digit = n % 10;
        sum += factorial(digit);
        n /= 10;
    }

    return sum == original;
}

int main() {
    int n;
    cout << "Enter number: ";
    cin >> n;

    if (isStrong(n))
        cout << n << " is a Strong Number" << endl;
    else
        cout << n << " is NOT a Strong Number" << endl;

    return 0;
}



/*



✅ Complexity Analysis

Suppose the number has d digits.

For each digit, we compute factorial (max 9! = 362880).
→ Factorial of single digit is O(1) (constant time).

So:

   Time Complexity: O(d) = O(log10(n))
   Space Complexity: O(1)






*/