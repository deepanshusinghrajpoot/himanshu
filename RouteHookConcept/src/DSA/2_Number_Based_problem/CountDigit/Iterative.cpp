/*

13. Count Digits of a Number



✅ Approach 1: Iterative (Division by 10)
------------------------------------------

Keep dividing by 10 until number becomes 0.


*/





#include <iostream>
using namespace std;

int countDigits(int n) {
    if (n == 0) return 1; // special case
    int count = 0;
    while (n > 0) {
        n /= 10;
        count++;
    }
    return count;
}

int main() {
    int n;
    cout << "Enter number: ";
    cin >> n;
    cout << "Number of digits = " << countDigits(n) << endl;
}


/*


👉 Time Complexity: O(d) (where d = number of digits)
👉 Space Complexity: O(1)


*/