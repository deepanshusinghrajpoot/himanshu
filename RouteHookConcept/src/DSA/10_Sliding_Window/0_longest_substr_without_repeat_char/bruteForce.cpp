
/*




=========== LONGEST SUBSTRING WITH UNIQUE CHARACTERS (BRUTE FORCE) ===========

Problem:
Find the LENGTH of the longest substring
that contains ALL UNIQUE characters.

-----------------------------------------------------------
Approach Used:
-----------------------------------------------------------

Brute Force + Frequency Array

• Fix a starting index i
• Try all substrings starting from i
• Stop when a duplicate character appears

-----------------------------------------------------------
Core Idea:
-----------------------------------------------------------

For every starting position:
→ Expand substring until characters remain UNIQUE
→ Use a hash/frequency array to detect duplicates

-----------------------------------------------------------
Step-by-Step Logic:
-----------------------------------------------------------

1️⃣ Outer loop (i):
   • Choose starting index of substring

-----------------------------------------------------------

2️⃣ Inner loop (j):
   • Keep extending substring from i to j
   • Use hash[256] to track visited characters

-----------------------------------------------------------

3️⃣ If a character repeats:
   • Break the inner loop
   • Move to next starting index

-----------------------------------------------------------

4️⃣ Update maximum length:
   maxLen = max(maxLen, j - i + 1)

-----------------------------------------------------------
Why This Works:
-----------------------------------------------------------

• All possible substrings are explored
• Hash array ensures substring contains UNIQUE characters
• Longest valid substring length is tracked

-----------------------------------------------------------
Example:
-----------------------------------------------------------

Input:  "abca"

i = 0 → "a" → "ab" → "abc" → stop at duplicate 'a'
Length = 3

i = 1 → "b" → "bc" → "bca"
Length = 3

Final Answer = 3

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------

O(N²)

-----------------------------------------------------------
Where does O(N²) come from?
-----------------------------------------------------------

• Outer loop runs N times
• Inner loop runs up to N times
• Duplicate check is O(1) using hash array

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------

O(1)

-----------------------------------------------------------
Why O(1)?
-----------------------------------------------------------

• Hash array size is fixed (256 characters)
• Independent of input size

-----------------------------------------------------------
Valid For:
-----------------------------------------------------------

✔ Uppercase characters
✔ Lowercase characters
✔ Digits
✔ Special characters

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------

"Brute force checks all substrings using a hash array,
leading to O(N²) time complexity."

===========================================================





*/







#include<bits/stdc++.h>
using namespace std;



int longest_substring_with_unique_character(string s){

     int maxLen = 0;

     for(int i=0; i<s.length(); i++){
        int hash[256] = {0};
        for(int j=i; j<s.length(); j++){
            
            if(hash[s[j]] == 1) break;

            maxLen = max(maxLen, j-i+1);
            hash[s[i]] = 1;
        }
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
             << longest_substring_with_unique_character(testCases[i]) << "\n\n";
    }

    return 0;
}