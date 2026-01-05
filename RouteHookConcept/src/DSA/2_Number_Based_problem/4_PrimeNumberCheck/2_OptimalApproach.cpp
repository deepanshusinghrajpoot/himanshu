/*


concept
-------
         |
         |devidend
---------|-------------------
divisor  |remender
         |
         |
         |


number = 36


1 * 36 = 36
2 * 18 = 36
3 * 12 = 36
4 * 9  = 36 
6 * 6  = 36

9
12
18
36








✅ Approach 2: Optimized (Check till √n)
----------------------------------------

👉 If a number n is divisible by any number,
it must be ≤ √n.


*/

#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(int n) {
    if (n <= 1) return false;  
    if (n == 2) return true;   
    if (n % 2 == 0) return false;  // even numbers > 2 are not prime

    for (int i = 3; i <= sqrt(n); i += 2) {
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

🔹 Explanation

We already checked if the number is even (n % 2 == 0) before this loop.
That means if the number is divisible by 2, we already returned false.
So, no need to check even divisors again (4, 6, 8, …).
Hence, we skip even numbers and check only odd divisors.
👉 That’s why we start from 3 and increment by 2 → we only test odd numbers (3, 5, 7, 9, …).



⏱ Time Complexity: O(√N) (much faster)
💾 Space Complexity: O(1)





*/