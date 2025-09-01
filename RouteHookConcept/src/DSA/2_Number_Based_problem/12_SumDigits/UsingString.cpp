/*


✅ Approach 3: Using Strings

Convert to string and sum characters.


*/



#include <iostream>
#include <string>
using namespace std;

int sumOfDigits(int n) {
    string s = to_string(n);
    int sum = 0;
    for (char c : s) sum += c - '0';
    return sum;
}

int main() {
    int n;
    cout << "Enter number: ";
    cin >> n;
    cout << "Sum of digits = " << sumOfDigits(n) << endl;
}


/*


👉 Time Complexity: O(d)
👉 Space Complexity: O(d)


*/


