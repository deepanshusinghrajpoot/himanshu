/*


🔹 Problem: Palindrome Check
-----------------------------

A palindrome is a string that reads the same forward and backward.

Example:

Input → "madam" ✅ Palindrome
Input → "hello" ❌ Not a palindrome







✅ Approach 1: Two Pointers
----------------------------


*/


#include <iostream>
using namespace std;

bool isPalindrome(string s) {
    int left = 0, right = s.size() - 1;

    while(left < right) {
        if(s[left] != s[right]) return false;  // mismatch
        left++;
        right--;
    }
    return true;
}

int main() {
    string s;
    cout << "Enter a string: ";
    cin >> s;

    if(isPalindrome(s))
        cout << "Palindrome ✅" << endl;
    else
        cout << "Not Palindrome ❌" << endl;

    return 0;
}

/*


⏱ Time & Space Complexity


Time Complexity: O(N)


Space Complexity:

Two-pointer → O(1)
Reverse-string → O(N) (extra copy)



*/