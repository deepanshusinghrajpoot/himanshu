
/*



=========== REMOVE OUTERMOST PARENTHESES ===========

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

• Use a STACK to track nesting depth  
• Only keep characters that are INSIDE outer parentheses  
• Ignore the FIRST opening and LAST closing of each primitive  

--------------------------------------------------
Key Observation:
--------------------------------------------------

• When stack is EMPTY → we are at OUTERMOST level  
• Characters added ONLY when stack is NOT empty  

--------------------------------------------------
Step-by-Step Logic (Dry Run):
--------------------------------------------------

String: "(()())"

Char '(' :
Stack empty → OUTERMOST '(' ❌ skip
Push '('

Char '(' :
Stack NOT empty → INNER '(' ✅ keep
Push '('

Char ')' :
Pop
Stack NOT empty → INNER ')' ✅ keep

Char '(' :
Stack NOT empty → INNER '(' ✅ keep
Push '('

Char ')' :
Pop
Stack NOT empty → INNER ')' ✅ keep

Char ')' :
Pop
Stack becomes empty → OUTERMOST ')' ❌ skip

Result from this group: "()()"

--------------------------------------------------
Why Stack Works:
--------------------------------------------------

• Stack size tells DEPTH of parentheses  
• Depth > 0 → inner content  
• Depth = 0 → outer boundary  

--------------------------------------------------
Valid Brackets Covered:
--------------------------------------------------

• ( )
• { }
• [ ]

Same logic applies to all.

--------------------------------------------------
Time Complexity:
--------------------------------------------------
O(N)

--------------------------------------------------
Where does O(N) come from?
--------------------------------------------------

• Each character is processed ONCE  
• Each push/pop is O(1)

--------------------------------------------------
Space Complexity:
--------------------------------------------------
O(N)

--------------------------------------------------
Why O(N)?
--------------------------------------------------

• Stack may store all opening brackets
  in worst case (e.g. "(((((")

--------------------------------------------------
Edge Cases:
--------------------------------------------------

• Empty string → returns empty
• "()()" → returns empty string
• Single primitive only → inner part returned

--------------------------------------------------
One-Line Interview Answer:
--------------------------------------------------
"Use a stack to track depth and ignore characters
when depth is zero to remove outer parentheses."

===================================================








*/






#include<bits/stdc++.h>
using namespace std;



string remove_outer_most_parenthesis(string s) {

    string ans = "";
    stack<char> st;

    for (char ch : s) {

        // Opening bracket
        if (ch == '(' || ch == '{' || ch == '[') {
            if (!st.empty()) ans += ch;   // inner opening
            st.push(ch);
        }

        // Closing bracket
        else {
            st.pop();
            if (!st.empty()) ans += ch;   // inner closing
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