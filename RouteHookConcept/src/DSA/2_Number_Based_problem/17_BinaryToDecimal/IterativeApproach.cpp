/*




✅ Part B: Binary → Decimal



🔹 Approach 1: Using Place Values
-----------------------------------



*/



#include <iostream>
#include <cmath>
using namespace std;

int binaryToDecimal(long long n) {
    int decimal = 0, base = 1;

    while (n > 0) {
        int lastDigit = n % 10;
        decimal += lastDigit * base;
        base *= 2;
        n /= 10;
    }
    return decimal;
}

int main() {
    long long n;
    cout << "Enter binary number: ";
    cin >> n;

    cout << "Decimal: " << binaryToDecimal(n) << endl;
    return 0;
}



/*


👉 Example: 1010 → 10
👉 Time Complexity: O(log n) (number of binary digits)
👉 Space Complexity: O(1)


*/