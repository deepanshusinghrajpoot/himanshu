/*

✅ Approach 1: Reverse Number & Compare

Store original number.
Reverse the number (like we did earlier).
Compare reversed with original.
       If same → Palindrome
       Else → Not Palindrome



*/




#include <iostream>
using namespace std;

bool isPalindrome(int n) {
    if (n < 0) return false;   // Negative numbers are not palindrome

    int original = n;
    long long rev = 0;

    while (n > 0) {
        int digit = n % 10;
        rev = rev * 10 + digit;
        n /= 10;
    }

    return (rev == original);
}

int main() {
    int n;
    cout << "Enter number: ";
    cin >> n;

    if (isPalindrome(n))
        cout << n << " is a Palindrome Number" << endl;
    else
        cout << n << " is NOT a Palindrome" << endl;

    return 0;
}


/*


Time Complexity: O(d) :- d is nuber od digits.

Space Complexity: O(1)



*/