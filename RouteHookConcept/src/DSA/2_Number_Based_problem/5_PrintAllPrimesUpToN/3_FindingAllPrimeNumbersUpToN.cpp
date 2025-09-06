/*


Finding all prime number up to N
--------------------------------


🔹 Sieve of Eratosthenes (n = 30)

👉 Start: Assume all numbers are prime initially.
(P = prime candidate, X = crossed out / composite)

2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
P  P  P  P  P  P  P  P  P  P  P  P  P  P  P  P  P  P  P  P  P  P  P  P  P  P  P  P  P






✅ Step 1: i = 2 (prime found)
------------------------------
Start marking multiples of 2 (from 2×2 = 4 onward).
2 → 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30


Arrow visualization:

2 → 4 ❌
2 → 6 ❌
2 → 8 ❌
...


Updated list:

2  3  X  5  X  7  X  9  X 11 X 13 X 15 X 17 X 19 X 21 X 23 X 25 X 27 X 29 X







✅ Step 2: i = 3 (still prime)
-------------------------------
Now mark multiples of 3 (from 3×3 = 9 onward).
3 → 9, 12, 15, 18, 21, 24, 27, 30


Arrow visualization:

3 → 9 ❌
3 → 12 ❌ (already crossed earlier by 2)
3 → 15 ❌
...


Updated list:

2  3  X  5  X  7  X  X  X 11 X 13 X 15 X 17 X 19 X 21 X 23 X 25 X 27 X 29 X





❌ Step 3: i = 4
----------------
Skip because 4 is already ❌ (was crossed out by 2).





✅ Step 4: i = 5 (prime)
-------------------------
Now mark multiples of 5 (from 5×5 = 25 onward).
5 → 25, 30


Arrow visualization:

5 → 25 ❌
5 → 30 ❌ (already crossed earlier)


Updated list:

2  3  X  5  X  7  X  X  X 11 X 13 X 15 X 17 X 19 X 21 X 23 X  X  X  29 X




⛔ Stop when i*i > n

Here, after i = 5 → 5×5 = 25 ≤ 30 ✅
Next i = 6 → 6×6 = 36 > 30 ❌ → Stop.

✅ Final Prime Numbers up to 30
2, 3, 5, 7, 11, 13, 17, 19, 23, 29






📌 Summary (how it works):
Outer loop picks the current prime i.
Inner loop crosses all multiples of i starting from i*i.
Repeat until i*i > n.
Remaining uncrossed numbers are prime.









✅ Approach 3: Precompute Primes (Sieve of Eratosthenes)
---------------------------------------------------------

If interviewer asks: “What if I need to check prime for many numbers?” → Use Sieve.

*/


#include <iostream>
#include <vector>
using namespace std;

void sieveOfEratosthenes(int n) {
    vector<bool> prime(n+1, true);
    prime[0] = prime[1] = false;

    for (int i = 2; i*i <= n; i++) {
        if (prime[i]) {                 // only work if i is prime
            for (int j = i*i; j <= n; j += i) {
                prime[j] = false;    // cross out multiples
            }
        }
    }

    cout << "Prime numbers up to " << n << ": ";
    for (int i = 2; i <= n; i++) {
        if (prime[i]) cout << i << " ";
    }
}
int main() {
    int n;
    cin >> n;
    sieveOfEratosthenes(n);
}


/*

⏱ Time Complexity: O(N log log N)
💾 Space Complexity: O(N)

✅ Interview Strategy

Start with √n optimized approach.

If they ask about multiple queries, explain Sieve.








✅ Interview Strategy

👉 If they ask "check if a single number is prime" → Explain √n method.
👉 If they ask "many queries like prime up to 10⁶" → Explain Sieve of Eratosthenes.
👉 Bonus: Mention Segmented Sieve for very large N (like 10¹² with queries).

*/