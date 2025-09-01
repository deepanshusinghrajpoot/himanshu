/*


✅ Approach 2: Optimized Divisor Sum (O(√n))

Instead of looping till n-1, loop till √n and add divisors in pairs.




*/

#include<bits/stdc++.h>
#include <iostream>
using namespace std;

bool isPerfect(int n) {
    if (n <= 1) return false;  // No perfect numbers ≤ 1

    int sum = 1; // 1 is always a divisor
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            sum += i;
            if (i != n / i) sum += n / i;  // add the pair divisor
        }
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


👉 Time Complexity: O(√n)
👉 Space Complexity: O(1)


*/