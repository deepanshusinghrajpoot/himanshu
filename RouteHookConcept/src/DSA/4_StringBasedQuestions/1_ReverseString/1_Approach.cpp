/*


🔹 Problem: Reverse a String

Input: "hello"
Output: "olleh"



✅ Approach 1: Using Two Pointers (In-place Swap)
--------------------------------------------------




*/

#include <iostream>
#include <string>
using namespace std;

string reverseString(string s) {
    int left = 0, right = s.size() - 1;
    while(left < right) {
        swap(s[left], s[right]);
        left++;
        right--;
    }
    return s;
}

int main() {
    string s;
    cout << "Enter a string: ";
    getline(cin, s);

    cout << "Reversed String: " << reverseString(s) << endl;
    return 0;
}


/*

⏱ Time & Space Complexity

Time Complexity: O(N) (all approaches)



Space Complexity:

Two-pointers & STL → O(1) (in-place)
Recursion → O(N) (stack space)



*/