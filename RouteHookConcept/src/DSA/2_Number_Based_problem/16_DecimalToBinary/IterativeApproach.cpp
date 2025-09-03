/*


✅ Part A: Decimal → Binary


🔹 Approach 1: Using Division by 2 (Iterative)
------------------------------------------------



*/




#include <iostream>
#include <vector>
using namespace std;

void decimalToBinary(int n) {
    vector<int> binary;

    while (n > 0) {
        binary.push_back(n % 2); // store remainder
        n /= 2;
    }

    cout << "Binary: ";
    for (int i = binary.size() - 1; i >= 0; i--)
        cout << binary[i];
    cout << endl;
}

int main() {
    int n;
    cout << "Enter decimal number: ";
    cin >> n;
    decimalToBinary(n);
    return 0;
}



/*

👉 Example: 10 → 1010
👉 Time Complexity: O(log n) (because we divide by 2)
👉 Space Complexity: O(log n) (to store binary digits)

*/