/*

✅ Approach 2: Recursive (Simple but Inefficient)

*/


#include <iostream>
using namespace std;

int fibonacci(int n) {
    if (n <= 1) return n;   // base case
    return fibonacci(n-1) + fibonacci(n-2);
}

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;
    cout << n << "th Fibonacci Number = " << fibonacci(n);
    return 0;
}



/*

⏱ Time Complexity:

O(2^N) (each call branches into 2 calls)

💾 Space Complexity:

O(N) (recursion stack depth)

*/