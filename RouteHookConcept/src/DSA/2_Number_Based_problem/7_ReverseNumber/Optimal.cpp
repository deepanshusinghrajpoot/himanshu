/*


✅ Approach 1: Iterative (Loop)
--------------------------------



🔹 Edge Case Handling

Negative Number

Input : -123
Output: -321


Ending with Zero

Input : 1200
Output: 21   (leading zeros ignored)


Overflow Case (Beyond 32-bit signed int range: -2,147,483,648 → 2,147,483,647)

Input : 1534236469
Output: Overflow! Cannot reverse within int range.





int overflow condition
----------------------

   -2^31 to 2^31 - 1(base)

-2,147,483,648 → 2,147,483,647


📌 Why this works?
-------------------

Rearrange the equation:
We want to ensure: 
                   
                    rev * 10 + digit <= INT_MAX

                    rev <= (INT_MAX - digit)/10;





*/



#include<bits/stdc++.h> // for INT_MAX and INT_MIN
#include <iostream>
using namespace std;

int reverseNumber(int n) {
    int rev = 0;
    bool isNegative = false;

    // Case 1: Handle Negative Numbers
    if (n < 0) {
        isNegative = true;
        n = -n;  // make positive
    }

    while (n > 0) {
        int digit = n % 10;

        // Case 2: Handle Overflow (like 1534236469 → reverse overflows int)
        if (rev > (INT_MAX - digit) / 10) {
            cout << "Overflow! Cannot reverse within int range." << endl;
            return 0;
        }

        rev = rev * 10 + digit;
        n /= 10;
    }

    return isNegative ? -rev : rev;
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;

    cout << "Reversed Number: " << reverseNumber(n) << endl;
    return 0;
}





/*



🔹 Complexity
---------------

Time Complexity: O(d) (where d = number of digits)
Space Complexity: O(1)




*/