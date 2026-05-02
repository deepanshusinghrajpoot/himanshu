
/*


=========== LEFT ROTATE ARRAY BY D PLACES (USING TEMP ARRAY) ===========

Problem:
-----------------------------------------------------------
Rotate the array to the LEFT by D positions.

-----------------------------------------------------------
Key Idea:
-----------------------------------------------------------

• Store first D elements separately
• Shift remaining elements to the left
• Place stored elements at the end

-----------------------------------------------------------
Why d = d % n ?
-----------------------------------------------------------

• Rotating by n or multiples of n gives same array
• Avoids unnecessary rotations

-----------------------------------------------------------
Step-by-Step Flow:
-----------------------------------------------------------

Array:  [1  2  3  4  5  6  7]
Index:   0  1  2  3  4  5  6
d = 2

-----------------------------------------------------------
Step 1️⃣: Store first d elements
-----------------------------------------------------------

temp = [1, 2]

-----------------------------------------------------------
Step 2️⃣: Shift remaining elements left
-----------------------------------------------------------

Shift elements from index d → n-1 to front

[3  4  5  6  7  _  _]

-----------------------------------------------------------
Step 3️⃣: Copy temp elements at end
-----------------------------------------------------------

[3  4  5  6  7  1  2]

-----------------------------------------------------------
Final Output:
-----------------------------------------------------------

[3  4  5  6  7  1  2]

-----------------------------------------------------------
Why This Works:
-----------------------------------------------------------

• Left rotation = remove first D elements
• Append them at the end
• Order of remaining elements stays same

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------

O(N)

-----------------------------------------------------------
Where does O(N) come from?
-----------------------------------------------------------

• Copy first D elements → O(D)
• Shift remaining N-D elements → O(N)
• Copy back D elements → O(D)
• Total ≈ O(N)

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------

O(D)

-----------------------------------------------------------
Why O(D)?
-----------------------------------------------------------

• Extra temporary array of size D is used

-----------------------------------------------------------
Limitations:
-----------------------------------------------------------

❌ Uses extra space
❌ Not in-place

-----------------------------------------------------------
Optimized Alternatives:
-----------------------------------------------------------

✔ Reversal Algorithm → O(N), O(1)
✔ Juggling Algorithm → O(N), O(1)

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------

"This approach rotates the array by storing first D elements,
shifting the rest, and appending stored elements in O(N) time."

===========================================================





*/




#include<bits/stdc++.h>
using namespace std;


void left_rotate_by_d_place(vector<int>&arr, int d){

    int n = arr.size();

    d = d%n;

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

    cout<<"Rotate D place left of the array :- ";
    left_rotate_by_d_place(arr, 15);
    for(int i=0; i<arr.size(); i++){
         cout<<arr[i]<<" ";
    }

    return 0;
}