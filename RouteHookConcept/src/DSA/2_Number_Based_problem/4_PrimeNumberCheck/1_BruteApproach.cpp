
/*

🔹 Problem: Check if a number is Prime

👉 Prime number = A number greater than 1 that has only 2 factors → 1 and itself.
Examples: 2, 3, 5, 7, 11 …
Not Prime: 4 (2×2), 9 (3×3)

✅ Approach 1: Naive (Check all numbers)

Check divisibility from 2 to n-1.

*/



#include <iostream>
using namespace std;

bool isPrime(int n) {
    if (n <= 1) return false;  // 0 and 1 are not prime

    for (int i = 2; i < n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    int n;
    cout << "Enter number: ";
    cin >> n;
    if (isPrime(n)) cout << n << " is Prime";
    else cout << n << " is Not Prime";
}


/*

⏱ Time Complexity: O(N)
💾 Space Complexity: O(1)

*/