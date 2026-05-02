
/*







=========== MAJORITY ELEMENT (BRUTE FORCE APPROACH) ===========

Definition:
-----------------------------------------------------------
Majority Element = element that appears MORE than ⌊N/2⌋ times
in the array.


-----------------------------------------------------------
Better Optimized Approaches:
-----------------------------------------------------------

✔ Hash Map → O(N log N)
✔ Moore’s Voting Algorithm → O(N), O(1)


-----------------------------------------------------------
Given Code Idea:
-----------------------------------------------------------

• Pick each element one by one
• Count its occurrences in the entire array
• If count > N/2 → return that element

-----------------------------------------------------------
Algorithm Flow:
-----------------------------------------------------------

1️⃣ Let n = size of array

2️⃣ For each index i (0 → n-1):
    • count = 0

3️⃣ For each index j (0 → n-1):
    • If arr[i] == arr[j]
        → increment count

4️⃣ After inner loop:
    • If count > n/2
        → arr[i] is MAJORITY ELEMENT
        → return arr[i]

5️⃣ If no such element exists:
    → return -1

-----------------------------------------------------------
Example:
-----------------------------------------------------------

Array: [2, 2, 1, 2, 3, 2, 2]
n = 7, n/2 = 3

Element = 2
Count = 5  (> 3)

Answer:
Majority Element = 2

-----------------------------------------------------------
Why It Works:
-----------------------------------------------------------

• Majority element must appear more than half the time
• Brute force checks frequency of every element

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------

O(N²)

-----------------------------------------------------------
Where does O(N²) come from?
-----------------------------------------------------------

• Outer loop runs N times
• Inner loop runs N times
• Total operations = N × N

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------

O(1)

-----------------------------------------------------------
Why O(1)?
-----------------------------------------------------------

• No extra data structure used
• Only a counter variable

-----------------------------------------------------------
Limitations:
-----------------------------------------------------------

❌ Very slow for large N
❌ Not suitable for interviews as final solution


-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------

"This brute-force solution checks frequency of every element,
leading to O(N²) time complexity."

===========================================================




*/




#include<bits/stdc++.h>
using namespace std;


int majority_element(vector<int>&arr){

    int n = arr.size();

    for(int i=0; i<n; i++){
        int count =0;
        for(int j=0; j<n; j++){
            if(arr[i] == arr[j]) count++;
        }
        if(count > n/2) return arr[i];
    }

    return -1;
}



int main(){

    vector<int>arr{2, 3, 2, 3, 3, 3, 3, 3, 4, 4};

    cout<<"Majority element in the array :- ";
    cout<<majority_element(arr);

    return 0;
}