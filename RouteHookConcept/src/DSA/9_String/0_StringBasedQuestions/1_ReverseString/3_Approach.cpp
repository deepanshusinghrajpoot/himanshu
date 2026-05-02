
// Recursive approach


#include <iostream>
using namespace std;

void reverseRec(string &s, int left, int right) {
    if(left >= right) return;
    swap(s[left], s[right]);
    reverseRec(s, left+1, right-1);
}

int main() {
    string s;
    cout << "Enter a string: ";
    getline(cin, s);

    reverseRec(s, 0, s.size()-1);
    cout << "Reversed String: " << s << endl;
    return 0;
}



/*


⏱ Time & Space Complexity

Time Complexity: O(N) (all approaches)

Space Complexity:

Two-pointers & STL → O(1) (in-place)
Recursion → O(N) (stack space)


*/