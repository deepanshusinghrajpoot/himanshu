/*



✅ Approach 2: Without Reversing Entire Number (Efficient)

Instead of reversing whole number (risk of overflow), reverse only half.

Example: 1221
→ First half = 12
→ Reverse second half = 12
→ Compare → Palindrome ✅



*/


#include<bits/stdc++.h>
#include<iostream>
using namespace std;




bool isPalindromeEfficient(int n) {
    if (n < 0 || (n % 10 == 0 && n != 0)) return false;     // Negative numbers are not palindrome 

    int rev = 0;

    while (n > rev) {
        int digit = n % 10;
        rev = rev * 10 + digit;
        n /= 10;
    }

    return (n == rev || n == rev / 10);  // number contain odd digit
}



int main() {
    int n;
    cout << "Enter number: ";
    cin >> n;

    if (isPalindromeEfficient(n))
        cout << n << " is a Palindrome Number" << endl;
    else
        cout << n << " is NOT a Palindrome" << endl;

    return 0;
}









/*



if (n < 0 || (n % 10 == 0 && n != 0)) return false;

        Explanation:
                  n < 0  :-  Negative numbers are never palindromes, because of the - sign.
                  Example: -121 → reversed would be 121- (not equal).


        (n % 10 == 0 && n != 0)
                  If the number ends with 0 but is not 0 itself, it cannot be a palindrome.
                  Example: 10 → reversed is 01 → becomes 1, not equal.

✅ Only 0 itself is valid (since 0 == 0).





*/