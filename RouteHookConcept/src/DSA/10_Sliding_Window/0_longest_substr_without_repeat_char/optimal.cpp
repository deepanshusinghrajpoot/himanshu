
/*


=========== LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS ===========

Problem:
Find the length of the LONGEST substring
with ALL UNIQUE characters.

-----------------------------------------------------------
Approach Used:
-----------------------------------------------------------

Sliding Window + Hashing (Last Seen Index)

• Use two pointers: LEFT and RIGHT
• Maintain a window [LEFT … RIGHT] with unique characters
• Hash array stores LAST INDEX of each character

-----------------------------------------------------------
Core Idea:
-----------------------------------------------------------

When a repeating character appears:
→ Move LEFT just after the previous occurrence
→ This keeps the substring UNIQUE

-----------------------------------------------------------
How Window Moves:
-----------------------------------------------------------

• RIGHT expands the window (adds new characters)
• LEFT shrinks the window ONLY when duplication occurs
• Window always represents a VALID substring

-----------------------------------------------------------
Step-by-Step Logic:
-----------------------------------------------------------

1️⃣ Initialize:
   LEFT = 0
   RIGHT = 0
   maxLen = 0
   hash[256] = -1 (stores last index of characters)

-----------------------------------------------------------

2️⃣ While RIGHT < length of string:

   • If current character was seen BEFORE
     AND its last index ≥ LEFT
       → Move LEFT = lastIndex + 1

   • Update maxLen using:
       maxLen = max(maxLen, RIGHT - LEFT + 1)

   • Update last seen index of current character

   • Move RIGHT forward

-----------------------------------------------------------
Why This Works:
-----------------------------------------------------------

• LEFT never moves backward
• Each character is processed at most TWICE
  → once by RIGHT, once by LEFT
• Window always contains UNIQUE characters

-----------------------------------------------------------
Example:
-----------------------------------------------------------

Input:  "abcabcbb"

Window moves as:
"abc" → maxLen = 3
Repeat 'a' → LEFT jumps forward
Continue maintaining unique window

Final Answer = 3

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------

O(N)

-----------------------------------------------------------
Where does O(N) come from?
-----------------------------------------------------------

• RIGHT pointer moves N times
• LEFT pointer also moves at most N times
• No nested loops

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------

O(1)

-----------------------------------------------------------
Why O(1)?
-----------------------------------------------------------

• Hash array size is fixed (256 characters)
• Does NOT grow with input size

-----------------------------------------------------------
Valid For:
-----------------------------------------------------------

✔ Uppercase letters
✔ Lowercase letters
✔ Digits
✔ Special characters

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------

"Using sliding window with last seen indices,
we maintain a unique substring in O(N) time."

===========================================================







*/





#include<bits/stdc++.h>
using namespace std;



int longest_substr_without_repeating_char(string s){

    int left = 0;
    int right = 0;

    int maxLen = 0;

    vector<int>hash(256, -1);

    while(right < s.length()){
         
       if(hash[s[right]] != -1){
           if(hash[s[right]] >= left){
               left = hash[s[right]] + 1;
           }
       } 

       maxLen = max(maxLen, right - left + 1);

       hash[s[right]] = right;

       right++;
    }
    
    return maxLen;
}




int main(){

    vector<string> testCases = {
        "abcabcbb",   // 3 -> "abc"
        "bbbbb",      // 1 -> "b"
        "pwwkew",     // 3 -> "wke"
        "",           // 0
        "a",          // 1
        "au",         // 2
        "dvdf",       // 3 -> "vdf"
        "abba"        // 2 -> "ab" / "ba"
    };

    for(int i = 0; i < testCases.size(); i++){
        cout << "Test Case " << i + 1 << "\n";
        cout << "Input  : " << testCases[i] << "\n";
        cout << "Output : "
             << longest_substr_without_repeating_char(testCases[i]) << "\n\n";
    }

    return 0;
}