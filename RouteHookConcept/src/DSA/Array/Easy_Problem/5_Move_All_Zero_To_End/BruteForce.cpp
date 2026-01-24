
/*


=========== MOVE ALL ZEROS TO END (USING EXTRA ARRAY) ===========

Problem:
-----------------------------------------------------------
Move all 0s to the END of the array
while maintaining the RELATIVE ORDER
of non-zero elements.

-----------------------------------------------------------
Approach Used:
-----------------------------------------------------------

• Extra temporary array
• Two-pass method

-----------------------------------------------------------
Algorithm Steps:
-----------------------------------------------------------

1️⃣ Traverse array
   → Store all NON-ZERO elements in temp[]

2️⃣ Copy temp[] back to original array from index 0

3️⃣ Fill remaining positions with 0

-----------------------------------------------------------
Diagrammatic Example:
-----------------------------------------------------------

Input:
[1, 0, 2, 0, 3, 0, 4]

Step 1: temp array
temp = [1, 2, 3, 4]
count = 4

Step 2: copy temp back
[1, 2, 3, 4, ?, ?, ?]

Step 3: fill zeros
[1, 2, 3, 4, 0, 0, 0]

-----------------------------------------------------------
Final Output:
-----------------------------------------------------------

[1  2  3  4  0  0  0]

-----------------------------------------------------------
Why This Works:
-----------------------------------------------------------

• Preserves order of non-zero elements
• Zeros are pushed after all valid elements
• Simple and readable approach

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------

O(N)

-----------------------------------------------------------
Where does O(N) come from?
-----------------------------------------------------------

• First loop → scans array once (N)
• Second + third loop → total N writes
• Overall linear work

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------

O(N)

-----------------------------------------------------------
Why O(N)?
-----------------------------------------------------------

• Uses an extra array temp[] of size ≤ N

-----------------------------------------------------------
Edge Cases:
-----------------------------------------------------------

• All zeros → array unchanged
• No zeros → array unchanged
• Single element array

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------

"Store non-zero elements first, then overwrite remaining
positions with zeros using an extra array."

===========================================================



*/





#include<bits/stdc++.h>
using namespace std;


void move_all_zero_to_end(vector<int>&arr){

    vector<int>temp;
    int count = 0;

    for(int i=0; i<arr.size(); i++){
        if(arr[i] != 0){
           temp.push_back(arr[i]);
           count++;
        }
    }

    for(int i=0; i<count; i++){
        arr[i] = temp[i];
    }

    for(int i=count; i<arr.size(); i++){
        arr[i] = 0;
    }
}


int main(){

    vector<int>arr{2, 0, 4, 0, 4, 0, 2, 5, 6, 0, 0, 0, 1, 9};
    cout<<"Move all zero to the end :- ";
    move_all_zero_to_end(arr);
    for(int i=0; i<arr.size(); i++){
        cout<<arr[i]<<" ";
    }

    return 0;
}