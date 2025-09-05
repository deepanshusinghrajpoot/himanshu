/*

Perfect Number

✅ Definition

A Number is called perfect number if sum of its proper divisors is equal to the (excluding the number itself).

✅ Examples
      6 → 1 + 2 + 3 = 6 ✅ Perfect Number
      28 → 1 + 2 + 4 + 7 + 14 = 28 ✅ Perfect Number
      12 → 1 + 2 + 3 + 4 + 6 = 16 ≠ 12 ❌ Not Perfect



✅ Approach 1: Naive Divisor Sum (O(n))
----------------------------------------

Check all divisors from 1 to n-1 and sum them.



*/




#include <iostream>
using namespace std;

bool isPerfect(int n) {
    int sum = 0;
    for (int i = 1; i < n; i++) {   // check all numbers < n
        if (n % i == 0) sum += i;
    }
    return sum == n;
}

int main() {
    int n;
    cout << "Enter number: ";
    cin >> n;
    if (isPerfect(n)) cout << n << " is Perfect\n";
    else cout << n << " is Not Perfect\n";
}



/*


👉 Time Complexity: O(n)
👉 Space Complexity: O(1)



*/

