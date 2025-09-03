/*


🔹 Approach 2: Using Bitwise Operators
----------------------------------------



*/




#include <iostream>
#include <cmath>
using namespace std;

int binaryToDecimalBitwise(string bin) {
    int decimal = 0;
    for (char bit : bin) {
        decimal = (decimal << 1) | (bit - '0'); 
    }
    return decimal;
}


int main() {
    string n;
    cout << "Enter binary number: ";
    cin >> n;

    cout << "Decimal: " << binaryToDecimalBitwise(n) << endl;
    return 0;
}







/*


Time Complexity = O(n)

Space Complexity = O(1)







What’s happening?
----------------

We start with decimal = 0.
We read each character ('0' or '1') in the binary string.

For each character:

decimal << 1 = multiply current decimal by 2 (shift bits left).
(bit - '0') = convert '0' → 0, '1' → 1.
| = add this new bit into the last place.






🔹 Example: "1011" (binary → decimal 11)

Start: decimal = 0

Step 1 → bit = '1'
decimal = (0 << 1) | 1
        = 0 | 1
        = 1



Step 2 → bit = '0'
decimal = (1 << 1) | 0
        = 2 | 0
        = 2



Step 3 → bit = '1'
decimal = (2 << 1) | 1
        = 4 | 1
        = 5



Step 4 → bit = '1'
decimal = (5 << 1) | 1
        = 10 | 1
        = 11



✅ Final Answer = 11



🔹 In easy words:

<< 1 = multiply by 2 (shift everything left).
| = put the new digit at the end.
Repeat for all digits → you get decimal number.




*/