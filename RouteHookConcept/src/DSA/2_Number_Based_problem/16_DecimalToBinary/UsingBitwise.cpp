/*



🔹 Approach 2: Using Bitwise Operators
---------------------------------------




*/




#include <iostream>
#include <vector>
using namespace std;

void decimalToBinaryBitwise(int n) {
    cout << "Binary: ";
    for (int i = 31; i >= 0; i--) {
        int bit = (n >> i) & 1;
        if (bit) cout << 1;
        else cout << 0;
    }
    cout << endl;
}


int main() {
    int n;
    cout << "Enter decimal number: ";
    cin >> n;
    decimalToBinaryBitwise(n);
    return 0;
}



/*


T.C = O(32)
S.C = O(1)





🔹 Step 1: (n >> i)
--------------------

This is the right shift operator.
It shifts the bits of n right by i places.

Example:

n = 10 → binary: 0000...1010
n >> 3 → 0000...0001


So (n >> i) brings the ith bit to the last position (LSB).




🔹 Step 2: & 1
----------------

After shifting, we do & 1 (bitwise AND with 0001).
This extracts the last bit.

Example:

n = 10 (1010)
i = 3 → n >> 3 = 0001 → (0001 & 0001) = 1
i = 2 → n >> 2 = 0010 → (0010 & 0001) = 0


So bit = (n >> i) & 1 gives either 0 or 1.





🔹 Step 3: Printing loop
-------------------------

The loop goes from i = 31 down to i = 0.
This checks all 32 bits (for a standard int in C++).
So it prints the full 32-bit binary representation.

Example:

n = 5

Binary: 00000000000000000000000000000101






🔹 Example Walkthrough for n = 10
-----------------------------------

n = 10 → binary: 0000...00001010



Loop:

i = 31 → (10 >> 31) = 0 → &1 = 0 → print 0
...
i = 3  → (10 >> 3)  = 0001 → &1 = 1 → print 1
i = 2  → (10 >> 2)  = 0010 → &1 = 0 → print 0
i = 1  → (10 >> 1)  = 0101 → &1 = 1 → print 1
i = 0  → (10 >> 0)  = 1010 → &1 = 0 → print 0


Output:

Binary: 00000000000000000000000000001010


✅ In short:

(n >> i) shifts the number so that the ith bit moves to the last position.
& 1 extracts that last bit.
Loop prints all bits → gives full binary representation.




*/