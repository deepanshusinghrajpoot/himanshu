
/*



=========== MAJORITY ELEMENT (HASH MAP APPROACH) ===========

Definition:
-----------------------------------------------------------
Majority Element = element that appears MORE than ⌊N/2⌋ times
in the array.

-----------------------------------------------------------
Core Idea:
-----------------------------------------------------------

• Count frequency of each element using Hash Map
• The element with count > N/2 is the majority element

-----------------------------------------------------------
Algorithm Flow:
-----------------------------------------------------------

1️⃣ Create an empty map mp

2️⃣ Traverse the array:
    • mp[arr[i]]++   (store frequency)

3️⃣ Traverse the map:
    • If frequency > N/2
        → return that element

4️⃣ If no such element exists:
    → return -1

-----------------------------------------------------------
Example:
-----------------------------------------------------------

Array: [3, 3, 4, 2, 3, 3, 3]
N = 7, N/2 = 3

Map:
3 → 5
4 → 1
2 → 1

Answer:
Majority Element = 3

-----------------------------------------------------------
Why This Works:
-----------------------------------------------------------

• Majority element must dominate the frequency count
• Hash map stores exact occurrences of each element

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------

O(N log N)

-----------------------------------------------------------
Where does O(N log N) come from?
-----------------------------------------------------------

• Inserting N elements into map → O(N log N)
• Traversing map → O(N)
• Dominant term → O(N log N)

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------

O(N)

-----------------------------------------------------------
Why O(N)?
-----------------------------------------------------------

• Hash map stores up to N unique elements

-----------------------------------------------------------
Valid For:
-----------------------------------------------------------

✔ Positive numbers
✔ Negative numbers
✔ Zero values
✔ Unsorted array

-----------------------------------------------------------
Comparison:
-----------------------------------------------------------

Brute Force → O(N²), O(1)
Hash Map    → O(N log N), O(N)
Moore Vote  → O(N), O(1) ✅ BEST

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------

"Using a hash map, we count frequencies and find the element
appearing more than N/2 times in O(N log N) time."

===========================================================






*/




#include<bits/stdc++.h>
using namespace std;


int majority_element(vector<int>&arr){

    map<int, int>mp;

    for(int i=0; i<arr.size(); i++){
        mp[arr[i]]++;
    }

    for(auto p : mp){
        if(p.second > arr.size()/2) return p.first;
    }

    return -1;
}



int main(){

    vector<int>arr{2, 3, 2, 3, 3, 3, 3, 3, 4, 4};

    cout<<"Majority element in the array :- ";
    cout<<majority_element(arr);

    return 0;
}