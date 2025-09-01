/*

✅ Approach 2: Recursive

*/


#include <iostream>
using namespace std;

long long factorial(int n) {
    if (n == 0 || n == 1) return 1;  // base case
    return n * factorial(n - 1);
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

O(N) (recursive calls from n → 1)

💾 Space Complexity:

O(N) (function call stack)

⚡ Bonus (If interviewer asks about big numbers)

Factorials grow very fast. For large n, values overflow int or long long.
👉 Use arrays / strings / BigInteger (in Java/Python) to store big factorial.
(They sometimes ask up to 100!)

✅ Interview Tip:

First write iterative (O(N), O(1)).

If they ask recursion → explain stack usage.

If they ask about large factorials → suggest BigInteger or array storage.

*/