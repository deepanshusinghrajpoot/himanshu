/*

🔹 Problem: Find the Nth Fibonacci Number

👉 Fibonacci series: 0, 1, 1, 2, 3, 5, 8 …

F(0) = 0

F(1) = 1

F(n) = F(n-1) + F(n-2) for n ≥ 2

✅ Approach 1: Iterative (Efficient)


*/


#include <iostream>
using namespace std;

int nthFibonacci(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;

    int a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;
    cout << n << "th Fibonacci Number = " << nthFibonacci(n);
    return 0;
}


/*

⏱ Time Complexity:

O(N) (loop runs N times)

💾 Space Complexity:

O(1) (only a few variables)

*/