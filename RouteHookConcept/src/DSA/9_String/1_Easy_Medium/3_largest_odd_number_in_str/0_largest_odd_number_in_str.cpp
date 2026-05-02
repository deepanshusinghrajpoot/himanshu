

/*


=========== LARGEST ODD NUMBER IN A STRING ===========

Problem:
--------------------------------------------------
Given a numeric string s,
return the LARGEST ODD number (as a string)
that can be formed by removing some suffix.
If no odd number exists, return "".

--------------------------------------------------
Key Observation:
--------------------------------------------------

• An ODD number always ends with an ODD digit
• Odd digits → 1, 3, 5, 7, 9
• To get the LARGEST odd number:
  → keep the string as LONG as possible
  → cut from the RIGHT side only

--------------------------------------------------
Core Idea:
--------------------------------------------------

• Traverse the string from RIGHT to LEFT
• Find the FIRST odd digit
• Return substring from index 0 to that position

--------------------------------------------------
Algorithm Flow:
--------------------------------------------------

For i = last index → 0:
• Convert s[i] to digit
• Check if digit is ODD
• If YES:
  → return s[0 … i]

If no odd digit found:
→ return empty string ""

--------------------------------------------------
Example:
--------------------------------------------------

Input:
s = "35420"

Scan from right:
0 → even ❌
2 → even ❌
4 → even ❌
5 → odd ✅

Return:
"354"

--------------------------------------------------
Another Example:
--------------------------------------------------

Input:
s = "4206"

No odd digit found
Output = ""

--------------------------------------------------
Why This Works:
--------------------------------------------------

• Cutting from the right keeps number maximum
• First odd digit from right gives longest valid odd prefix

--------------------------------------------------
Time Complexity:
--------------------------------------------------
O(N)

--------------------------------------------------
Where does O(N) come from?
--------------------------------------------------

• Single reverse traversal of the string

--------------------------------------------------
Space Complexity:
--------------------------------------------------
O(1)

--------------------------------------------------
Why O(1)?
--------------------------------------------------

• No extra data structures used
• Substring is part of output, not auxiliary space

--------------------------------------------------
Edge Cases:
--------------------------------------------------

• String has no odd digit → ""
• Single digit odd → return full string
• Leading zeros are preserved if present

--------------------------------------------------
One-Line Interview Answer:
--------------------------------------------------

"Scan from right to find the last odd digit and
return the prefix up to that index."

===================================================






| Test Case | Input     | Output    | Correct |
| --------- | --------- | --------- | ------- |
| 1         | `"52"`    | `"5"`     | ✅       |
| 2         | `"4206"`  | `""`      | ✅       |
| 3         | `"35427"` | `"35427"` | ✅       |
| 4         | `"13579"` | `"13579"` | ✅       |
| 5         | `"2468"`  | `""`      | ✅       |
| 6         | `"1"`     | `"1"`     | ✅       |
| 7         | `"0"`     | `""`      | ✅       |
| 8         | `"1010"`  | `"101"`   | ✅       |
| 9         | `"9087"`  | `"9087"`  | ✅       |






*/






#include<bits/stdc++.h>
using namespace std;


string largest_odd_number_in_str(string s){

    for(int i=s.size() - 1;  i>=0;  i--){
        if((s[i] - '0')%2 != 0){
            return s.substr(0, i+1);
        }
    }

    return "";
}



int main(){

    vector<string> testCases = {
        "52",
        "4206",
        "35427",
        "13579",
        "2468",
        "1",
        "0",
        "1010",
        "9087"
    };

    for(int i = 0; i < testCases.size(); i++){
        cout << "Test Case " << i + 1 << ": " << testCases[i]
             << "\nLargest Odd Number = "
             << largest_odd_number_in_str(testCases[i]) << "\n\n";
    }

    return 0;
}