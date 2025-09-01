

/*



🔹 Definition

A number is called an Armstrong number if the sum of its digits raised to the power of the number of digits equals the number itself.

Examples:
      153 → 1³ + 5³ + 3³ = 153 ✅ (Armstrong)
      9474 → 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474 
      123 → 1³ + 2³ + 3³ = 36 ❌






*/




#include <iostream>
#include <cmath> // for pow()
using namespace std;



int power(int digit, int digits){
   int p = 1;
   for(int i=1; i<=digits; i++){
      p *= digit;
   }
   return p;
}


bool isArmstrong(int n) {
    int original = n;
    int digits = 0;
    int temp = n;

    // Count digits
    while (temp > 0) {
        digits++;
        temp /= 10;
    }

    int sum = 0;
    temp = n;

    // Sum of digits^digits
    while (temp > 0) {
        int digit = temp % 10;
        sum += power(digit, digits);
        temp /= 10;
    }

    return sum == original;
}

int main() {
    int n;
    cout << "Enter number: ";
    cin >> n;

    if (isArmstrong(n))
        cout << n << " is an Armstrong number" << endl;
    else
        cout << n << " is NOT an Armstrong number" << endl;

    return 0;
}


/*


Time Complexity = O(d^2)
Space Complexity = O(1)



*/