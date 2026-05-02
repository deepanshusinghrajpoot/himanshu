
/*


=========== RIGHT ROTATE ARRAY BY D PLACES (TEMP ARRAY METHOD) ===========

Problem:
-----------------------------------------------------------
Rotate the array to the RIGHT by k positions.

-----------------------------------------------------------
Key Conversion:
-----------------------------------------------------------

Right rotation by k  ≡  Left rotation by (n - k)

So,
d = n - k

-----------------------------------------------------------
Why k = k % n ?
-----------------------------------------------------------

• Rotating by n or multiples of n gives same array
• Avoids extra rotations

-----------------------------------------------------------
Visual Example:
-----------------------------------------------------------

Array:  [1  2  3  4  5  6  7]
Index:   0  1  2  3  4  5  6
k = 2

n = 7
d = n - k = 5

-----------------------------------------------------------
Step 1️⃣: Store first d elements in temp
-----------------------------------------------------------

temp = [1  2  3  4  5]

-----------------------------------------------------------
Step 2️⃣: Shift remaining elements to front
-----------------------------------------------------------

Move elements from index d → n-1 to front

[6  7  3  4  5  6  7]
↓
[6  7  _  _  _  _  _]

-----------------------------------------------------------
Step 3️⃣: Copy temp elements at the end
-----------------------------------------------------------

Final Array:

[6  7  1  2  3  4  5]

-----------------------------------------------------------
Final Output:
-----------------------------------------------------------

[6  7  1  2  3  4  5]

-----------------------------------------------------------
Why This Works:
-----------------------------------------------------------

• Right rotation converted to left rotation
• Preserves order using temporary storage

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------

O(N)

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------

O(D)  ≈  O(N)

-----------------------------------------------------------
Where Space is Used:
-----------------------------------------------------------

• temp array stores first (n - k) elements

-----------------------------------------------------------
Comparison:
-----------------------------------------------------------

Temp Array Method   → O(N), O(N)
Reversal Algorithm  → O(N), O(1) ✅ Better

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------

"Right rotation is achieved by converting it into
left rotation using a temporary array in O(N) time."

===========================================================







*/




#include<bits/stdc++.h>
using namespace std;


void right_rotate_by_d_place(vector<int>&arr, int k){

    int n = arr.size();

    k = k%n;
    int d = n-k;

    vector<int>temp;

    for(int i=0; i<d; i++){
        temp.push_back(arr[i]);
    }
    for(int i=d; i<n; i++){
        arr[i-d] = arr[i];
    }

    int j = 0;
    for(int i=n-d; i<n; i++){
       arr[i] = temp[j];
       j++;
    }

}




int main(){

    vector<int>arr{2, 3, 4, 5, 6, 1, 7, 8, 9, 0};

    cout<<"Rotate D place right of the array :- ";
    right_rotate_by_d_place(arr, 4);
    for(int i=0; i<arr.size(); i++){
         cout<<arr[i]<<" ";
    }

    return 0;
}