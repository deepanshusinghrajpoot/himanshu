
// Using STL



#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    string s;
    cout << "Enter a string: ";
    getline(cin, s);

    reverse(s.begin(), s.end());  // STL function
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