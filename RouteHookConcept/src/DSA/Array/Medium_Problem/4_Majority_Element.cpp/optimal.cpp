
/*





=========== MAJORITY ELEMENT (MOORE’S VOTING ALGORITHM) ===========

Definition:
-----------------------------------------------------------
Majority Element = element that appears MORE than ⌊N/2⌋ times
in the array.

-----------------------------------------------------------
Core Idea:
-----------------------------------------------------------

• Majority element (if exists) survives pair cancellation
• Different elements cancel each other out
• Final candidate MAY be majority → needs verification

-----------------------------------------------------------
Algorithm – 2 PHASES:
-----------------------------------------------------------

PHASE 1️⃣: Find Candidate
PHASE 2️⃣: Verify Candidate

-----------------------------------------------------------
PHASE 1️⃣: FIND CANDIDATE
-----------------------------------------------------------

Rules:
• If count == 0 → pick current element as candidate
• If current element == candidate → count++
• Else → count--

-----------------------------------------------------------
Visual Example:
-----------------------------------------------------------

Array: [2, 2, 1, 1, 2, 2, 2]

Step-by-step:
-----------------------------------------------------------
Element   Candidate   Count
-----------------------------------------------------------
2           2          1
2           2          2
1           2          1
1           2          0   (cancelled)
2           2          1
2           2          2
2           2          3

Candidate after Phase 1 = 2

-----------------------------------------------------------
Why Cancellation Works:
-----------------------------------------------------------

• Majority element appears more than N/2 times
• It cannot be fully cancelled by other elements

-----------------------------------------------------------
PHASE 2️⃣: VERIFY CANDIDATE
-----------------------------------------------------------

• Count occurrences of candidate in array
• If count > N/2 → candidate is MAJORITY
• Else → no majority element

-----------------------------------------------------------
Final Answer:
-----------------------------------------------------------

Majority Element = element (if verified)
Else return -1

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------

O(N)

-----------------------------------------------------------
Where does O(N) come from?
-----------------------------------------------------------

• Phase 1: single traversal → O(N)
• Phase 2: single traversal → O(N)
• Total = O(N) + O(N) = O(N)

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------

O(1)

-----------------------------------------------------------
Why O(1)?
-----------------------------------------------------------

• Only two variables used (count, element)
• No extra data structures

-----------------------------------------------------------
Valid For:
-----------------------------------------------------------

✔ Positive numbers
✔ Negative numbers
✔ Zero values
✔ Unsorted array

-----------------------------------------------------------
Comparison Summary:
-----------------------------------------------------------

Brute Force → O(N²), O(1)
Hash Map    → O(N log N), O(N)
Moore Vote  → O(N), O(1) ✅ BEST

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------

"Moore’s Voting Algorithm finds the majority element
in linear time using constant space via cancellation."

===========================================================










*/






#include<bits/stdc++.h>
using namespace std;


int majority_element(vector<int>&arr){

     
    int element;

    int count = 0;

    for(int i=0; i<arr.size(); i++){

        if(count == 0){
            count = 1;
            element = arr[i];
        }
        else if(arr[i] == element) count++;
        else count--;

    }

    count = 0;

    for(int i=0; i<arr.size(); i++){
        if(arr[i] == element) count++;
    }

    if(count > arr.size() / 2) return element;

    return -1;
}



int main(){

    vector<int>arr{2, 3, 2, 3, 3, 3, 3, 3, 4, 4};

    cout<<"Majority element in the array :- ";
    cout<<majority_element(arr);

    return 0;
}