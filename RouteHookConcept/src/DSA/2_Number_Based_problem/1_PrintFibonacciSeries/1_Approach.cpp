

/*

🔹 Problem: Print Fibonacci Series up to N terms

Example:
If N = 7 → Output: 0 1 1 2 3 5 8

✅ Approach 1: Iterative (Efficient & Preferred)

We calculate terms one by one using two variables.

C++ Code

*/


#include<bits/stdc++.h>
#include<iostream>
using namespace std;


void printFibonacci(int n) {
    int a = 0, b = 1;

    if (n >= 1) cout << a << " ";
    if (n >= 2) cout << b << " ";

    for (int i = 3; i <= n; i++) {
        int c = a + b;
        cout << c << " ";
        a = b;
        b = c;
    }
}



int main() {
    int n;
    cout << "Enter number of terms: ";
    cin >> n;
    printFibonacci(n);
    return 0;
}



/*
⏱ Time Complexity:

O(N) → loop runs N times

💾 Space Complexity:

O(1) → only 2-3 variables used

*/

