/*






=========== REMOVE OUTERMOST PARENTHESES (COUNTER METHOD) ===========

Problem:
--------------------------------------------------
Given a valid parentheses string,
remove the OUTERMOST parentheses
from every primitive group.

--------------------------------------------------
Example:
--------------------------------------------------

Input:
s = "(()())(())"

Primitive Groups:
(()())   (())

After removing outermost:
()()     ()

Output:
"()()()"

--------------------------------------------------
Core Idea:
--------------------------------------------------

• Use an INTEGER COUNTER instead of stack  
• Counter tracks current DEPTH of parentheses  
• Keep characters ONLY when depth > 0  

--------------------------------------------------
Key Observation:
--------------------------------------------------

• cnt == 0 → OUTERMOST level  
• cnt > 0  → INNER parentheses  

--------------------------------------------------
How Counter Works:
--------------------------------------------------

• '('  → depth increases (cnt++)  
• ')'  → depth decreases (cnt--)  

--------------------------------------------------
Rules to Add Character:
--------------------------------------------------

Opening '(' :
• Add ONLY if cnt > 0
• Then increment cnt

Closing ')' :
• Decrement cnt first
• Add ONLY if cnt > 0

--------------------------------------------------
Dry Run (Key Steps):
--------------------------------------------------

String: "(()())"

Char '(' :
cnt = 0 → OUTERMOST '(' ❌ skip
cnt = 1

Char '(' :
cnt > 0 → INNER '(' ✅ keep
cnt = 2

Char ')' :
cnt = 1
cnt > 0 → INNER ')' ✅ keep

Char '(' :
cnt > 0 → INNER '(' ✅ keep
cnt = 2

Char ')' :
cnt = 1
cnt > 0 → INNER ')' ✅ keep

Char ')' :
cnt = 0 → OUTERMOST ')' ❌ skip

Result: "()()"

--------------------------------------------------
Why This Works:
--------------------------------------------------

• Outermost parentheses are exactly
  the points where cnt moves
  from 0 → 1 (opening)
  and 1 → 0 (closing)

• Everything between them is INNER content

--------------------------------------------------
Time Complexity:
--------------------------------------------------
O(N)

--------------------------------------------------
Where does O(N) come from?
--------------------------------------------------

• Single pass through string
• Each character processed ONCE

--------------------------------------------------
Space Complexity:
--------------------------------------------------
O(1)

--------------------------------------------------
Why O(1)?
--------------------------------------------------

• Only an integer counter used
• No stack or extra data structures

--------------------------------------------------
Edge Cases:
--------------------------------------------------

• "()()" → returns empty string
• "((()))" → returns "(())"
• Empty string → returns empty

--------------------------------------------------
One-Line Interview Answer:
--------------------------------------------------
"Track depth using a counter and ignore characters
when depth is zero to remove outer parentheses."

===================================================













*/





#include<bits/stdc++.h>
using namespace std;


string remove_outer_most_parenthesis(string s) {

    string ans = "";
    int cnt = 0;

    for (char ch : s) {

        // Opening bracket
        if (ch == '(') {
            if (cnt > 0) ans += ch;  // inner opening
            cnt++;
        }

        // Closing bracket
        else {
            cnt--;
            if (cnt > 0) ans += ch;  // inner closing
        }
    }

    return ans;
}


int main(){

    string s1 = "((())((())))(())(())(())";

    string s2 = "[({}){()}]([{}]({}))";

    cout<<"Remove Outer most paranthesis :- ";
    cout<<remove_outer_most_parenthesis(s1);

    return 0;
}
