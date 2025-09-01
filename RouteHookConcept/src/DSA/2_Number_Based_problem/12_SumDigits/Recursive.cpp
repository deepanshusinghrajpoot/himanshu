/*


✅ Approach 2: Recursive

Same logic but using recursion.



*/



#include <iostream>
using namespace std;

int sumOfDigits(int n) {
    if (n == 0) return 0;
    return (n % 10) + sumOfDigits(n / 10);
}

int main() {
    int n;
    cout << "Enter number: ";
    cin >> n;
    cout << "Sum of digits = " << sumOfDigits(n) << endl;
}

/*

👉 Time Complexity: O(d)
👉 Space Complexity: O(d) (due to recursion stack)

*/