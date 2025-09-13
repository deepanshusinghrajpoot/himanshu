

// ✅ Approach 2: Using Reversed String


#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    string s;
    cout << "Enter a string: ";
    cin >> s;

    string rev = s;
    reverse(rev.begin(), rev.end());

    if(s == rev)
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