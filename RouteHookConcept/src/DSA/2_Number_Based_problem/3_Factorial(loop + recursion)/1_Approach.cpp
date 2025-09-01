/*

🔹 Problem: Find Factorial of N
---------------------------------

👉 Formula:

n! = n × (n-1) × (n-2) × … × 1

0! = 1 (by definition)

Example:
5! = 5 × 4 × 3 × 2 × 1 = 120

✅ Approach 1: Iterative (Efficient)

*/


#include <iostream>
using namespace std;

long long factorial(int n) {
    long long fact = 1;
    for (int i = 1; i <= n; i++) {
        fact *= i;
    }
    return fact;
}

int main() {
    int n;
    cout << "Enter number: ";
    cin >> n;
    cout << "Factorial of " << n << " = " << factorial(n);
    return 0;
}


/*

⏱ Time Complexity:

O(N) (loop runs N times)

💾 Space Complexity:

O(1) (only one variable)

*/

