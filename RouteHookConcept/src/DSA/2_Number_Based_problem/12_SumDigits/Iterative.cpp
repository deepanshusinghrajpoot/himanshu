/*

12. Sum of Digits of a Number



✅ Approach 1: Iterative (Modulo + Division)
---------------------------------------------

Extract each digit using % 10, add to sum, then divide by 10.

*/




#include <iostream>
using namespace std;

int sumOfDigits(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n % 10;  // get last digit
        n /= 10;        // remove last digit
    }
    return sum;
}

int main() {
    int n;
    cout << "Enter number: ";
    cin >> n;
    cout << "Sum of digits = " << sumOfDigits(n) << endl;
}


/*


👉 Time Complexity: O(d) (where d = number of digits)
👉 Space Complexity: O(1)



*/







