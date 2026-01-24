
/*


=========== LEFT ROTATE ARRAY BY D PLACES (REVERSAL ALGORITHM) ===========

Problem:
-----------------------------------------------------------
Rotate the array to the LEFT by D positions
using IN-PLACE method.

-----------------------------------------------------------
Core Idea:
-----------------------------------------------------------

Left Rotation by D =
Reverse first D elements
Reverse remaining N-D elements
Reverse the whole array

-----------------------------------------------------------
Why d = d % n ?
-----------------------------------------------------------

• Rotating by n or multiples of n gives same array
• Prevents unnecessary operations

-----------------------------------------------------------
Visual Explanation:
-----------------------------------------------------------

Array:  [1  2  3  4  5  6  7]
Index:   0  1  2  3  4  5  6
d = 2

-----------------------------------------------------------
Step 1️⃣: Reverse first D elements (0 → d-1)
-----------------------------------------------------------

Reverse [1  2]

[2  1  3  4  5  6  7]

-----------------------------------------------------------
Step 2️⃣: Reverse remaining elements (d → n-1)
-----------------------------------------------------------

Reverse [3  4  5  6  7]

[2  1  7  6  5  4  3]

-----------------------------------------------------------
Step 3️⃣: Reverse whole array (0 → n-1)
-----------------------------------------------------------

Reverse entire array

[3  4  5  6  7  1  2]

-----------------------------------------------------------
Final Output:
-----------------------------------------------------------

[3  4  5  6  7  1  2]

-----------------------------------------------------------
Why This Works:
-----------------------------------------------------------

• First reversal puts rotated elements in reverse order
• Second reversal arranges remaining elements
• Final reversal restores correct relative order

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------

O(N)

-----------------------------------------------------------
Where does O(N) come from?
-----------------------------------------------------------

• Reverse first part → O(D)
• Reverse second part → O(N-D)
• Reverse full array → O(N)
• Total ≈ O(N)

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------

O(1)

-----------------------------------------------------------
Why O(1)?
-----------------------------------------------------------

• No extra array used
• Only swaps performed in-place

-------------------------------------------






*/



#include <bits/stdc++.h>
using namespace std;

void reverse(vector<int>& arr, int left, int right) {
    while (left < right) {
        swap(arr[left], arr[right]);
        left++;
        right--;
    }
}

void left_rotate_by_d_place(vector<int>& arr, int d) {

    int n = arr.size();
    d = d % n;

    reverse(arr, 0, d - 1);
    reverse(arr, d, n - 1);
    reverse(arr, 0, n - 1);
}


int main(){

    vector<int>arr{2, 3, 4, 5, 6, 1, 7, 8, 9, 0};

    cout<<"Rotate D place left of the array :- ";
    left_rotate_by_d_place(arr, 15);
    for(int i=0; i<arr.size(); i++){
         cout<<arr[i]<<" ";
    }

    return 0;
}