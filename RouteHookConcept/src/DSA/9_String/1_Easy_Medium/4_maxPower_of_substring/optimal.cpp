
/*


=========== MAX POWER OF STRING (ONE UNIQUE CHAR SUBSTRING) ===========

Definition:
--------------------------------------------------
Power of a string =
Length of the LONGEST contiguous substring
containing ONLY ONE UNIQUE CHARACTER.

--------------------------------------------------
Example:
--------------------------------------------------

Input:  s = "leetcode"
Substrings:
"l" , "ee" , "t" , "c" , "o" , "d" , "e"

✔ Maximum Power = 2  ("ee")

--------------------------------------------------

Input: s = "abbcccddddeeeeedcba"
✔ Maximum Power = 5  ("eeeee")

--------------------------------------------------
Core Idea:
--------------------------------------------------

• Traverse string once
• Count consecutive SAME characters
• Reset count when character changes
• Track maximum length seen

--------------------------------------------------
Algorithm Flow:
--------------------------------------------------

1️⃣ Initialize:
   count = 1
   maxLen = 0

2️⃣ Start from index 1:
   Compare s[i] with s[i-1]

3️⃣ If SAME:
   → count++

4️⃣ If DIFFERENT:
   → update maxLen
   → reset count = 1

5️⃣ After loop:
   → update maxLen one last time

--------------------------------------------------
Why Last Update Needed?
--------------------------------------------------

• Longest group may appear at the END
• Loop update only happens on character change

--------------------------------------------------
Dry Run Example:
--------------------------------------------------

s = "aaabbc"

a a a → count = 3 → maxLen = 3  
b b   → count = 2  
c     → count = 1  

Final Answer = 3

--------------------------------------------------
Time Complexity:
--------------------------------------------------
O(N)

--------------------------------------------------
Where does O(N) come from?
--------------------------------------------------

• Single pass through the string
• Each character processed ONCE

--------------------------------------------------
Space Complexity:
--------------------------------------------------
O(1)

--------------------------------------------------
Why O(1)?
--------------------------------------------------

• Only fixed variables used
• No extra data structures

--------------------------------------------------
Edge Cases:
--------------------------------------------------

• Empty string → 0
• Single character → 1
• All characters same → length of string

--------------------------------------------------
One-Line Interview Answer:
--------------------------------------------------

"Track consecutive equal characters and keep
the maximum length seen in one traversal."

===================================================




| Input                   | Output | Correct |
| ----------------------- | ------ | ------- |
| `"leetcode"`            | `2`    | ✅       |
| `"abbcccddddeeeeedcba"` | `5`    | ✅       |
| `"a"`                   | `1`    | ✅       |
| `""`                    | `0`    | ✅       |
| `"aaabbaa"`             | `3`    | ✅       |




*/







#include<bits/stdc++.h>
using namespace std;

int max_power_of_substring_one_unique_char(string s){

    if(s.empty()) return 0;

    int maxLen = 0;

    int count = 1;
    for(int i=1; i<s.length(); i++){
         
        if(s[i] == s[i-1]){
            count++;
        }
        else{
            maxLen = max(maxLen, count);
            count = 1;
        }

    }
    maxLen = max(maxLen, count);

    return maxLen;
}


int main(){

    vector<string> testCases = {
        "leetcode",
        "abbcccddddeeeeedcba",
        "triplepillooooow",
        "hooraaaaaaaaaaay",
        "tourist",
        "a",
        "",
        "aaabbaa"
    };

    for(int i = 0; i < testCases.size(); i++){
        cout << "Test Case " << i + 1 << ": \"" << testCases[i] << "\"\n";
        cout << "Max Power = " << max_power_of_substring_one_unique_char(testCases[i]) << "\n\n";
    }

    return 0;
}