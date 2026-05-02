
/*



=========== ISOMORPHIC STRINGS (INDEX MAPPING METHOD) ===========

Definition: Two strings are isomorphic if characters map one-to-one, consistently, and in order.
--------------------------------------------------
Two strings s and t are ISOMORPHIC if:
• Characters in s can be replaced to get t
• Each character maps to ONLY ONE character
• Order must be preserved

--------------------------------------------------
Example:
--------------------------------------------------

s = "egg"
t = "add"
✔ Isomorphic

s = "foo"
t = "bar"
✘ Not Isomorphic

--------------------------------------------------
Core Idea:
--------------------------------------------------

• Track LAST SEEN POSITION of characters
• Mapping must be CONSISTENT for both strings
• Same pattern of repetition → valid

--------------------------------------------------
Data Structures Used:
--------------------------------------------------

• ms → map for string s
• mt → map for string t

(Key → character, Value → last index + 1)

--------------------------------------------------
Why store index + 1?
--------------------------------------------------

• Default map value is 0
• Index + 1 helps distinguish:
  - unseen (0)
  - seen before (>0)

--------------------------------------------------
Algorithm Flow:
--------------------------------------------------

For each index i from 0 to n-1:

1️⃣ Compare last seen positions:
   ms[s[i]] == mt[t[i]]

   ❌ If NOT equal → mapping mismatch → return false

2️⃣ Update both maps:
   ms[s[i]] = i + 1
   mt[t[i]] = i + 1

--------------------------------------------------
Why This Works:
--------------------------------------------------

• Ensures SAME pattern of repetition
• Prevents:
  - one-to-many mapping
  - many-to-one mapping

--------------------------------------------------
Pattern Check Example:
--------------------------------------------------

s = "paper"
t = "title"

Indexes:
p→0, a→1, p→2, e→3, r→4
t→0, i→1, t→2, l→3, e→4

✔ Same index pattern → Isomorphic

--------------------------------------------------
Time Complexity:
--------------------------------------------------
O(N)

--------------------------------------------------
Where does O(N) come from?
--------------------------------------------------

• Single traversal of strings
• Map operations are O(log N)

--------------------------------------------------
Space Complexity:
--------------------------------------------------
O(N)

--------------------------------------------------
Why O(N)?
--------------------------------------------------

• Maps store up to N unique characters

--------------------------------------------------
Edge Cases:
--------------------------------------------------

• Different lengths → false
• Single character strings → true
• Case-sensitive comparison

--------------------------------------------------
One-Line Interview Answer:
--------------------------------------------------

"Strings are isomorphic if their characters
repeat in the same index pattern."

===================================================





| s     | t     | Expected |
| ----- | ----- | -------- |
| egg   | add   | True     |
| foo   | bar   | False    |
| paper | title | True     |
| badc  | baba  | False    |
| a     | a     | True     |
| ab    | aa    | False    |






*/






#include<bits/stdc++.h>
using namespace std;


bool isIsomorphic(string s, string t){

    map<char, int>ms;
    map<char, int>mt;

    for(int i=0; i<s.length(); i++){

        if(ms[s[i]] != mt[mt[i]]) return false;

        ms[s[i]] = i+1;
        mt[t[i]] = i+1;
    }

    return true;
}




int main(){

    vector<pair<string,string>> testCases = {
        {"egg", "add"},
        {"foo", "bar"},
        {"paper", "title"},
        {"badc", "baba"},
        {"a", "a"},
        {"ab", "aa"}
    };

    for(int i = 0; i < testCases.size(); i++){
        cout << "Test Case " << i + 1 << ": "
             << testCases[i].first << " , "
             << testCases[i].second << "\nResult = "
             << (isIsomorphic(testCases[i].first, testCases[i].second) ? "True" : "False")
             << "\n\n";
    }

    return 0;
}