
/*



🔹 Infix to Postfix Conversion (Using Stack)
------------------------------------------------

📌 Expression
a + b * ( c ^ d - e )



🔹 Operator Priority (Precedence)

| Operator | Priority    |
| -------- | ----------- |
| `^`      | 3 (Highest) |
| `* /`    | 2           |
| `+ -`    | 1           |
| `(`      | 0 (Special) |



🔹 Rules (Very Important for Interview)
------------------------------------------

Operand → directly add to output.
( → push into stack.
) → pop from stack until ( is found.
Operator
    Stack empty → push operator.
    Incoming operator has higher priority → push.
    Incoming operator has lower or equal priority → pop from stack until lower priority is found, then push.



🔹 Given Interview Notes (Clean Version)
----------------------------------------------
✔ If stack has lower priority operator and higher priority comes → PUSH
✔ If stack has higher priority operator and lower priority comes → POP then PUSH



🔹 Step-by-Step Dry Run (Interview Gold ⭐)

Expression:

a + b * ( c ^ d - e )


| i (char) | Stack   | Answer (Postfix) |
| -------- | ------- | ---------------- |
| a        | —       | a                |
| +        | +       | a                |
| b        | +       | ab               |
| *        | + *     | ab               |
| (        | + * (   | ab               |
| c        | + * (   | abc              |
| ^        | + * ( ^ | abc              |
| d        | + * ( ^ | abcd             |
| -        | + * ( - | abcd^            |
| e        | + * ( - | abcd^e           |
| )        | + *     | abcd^e-          |
| END      | —       | abcd^e-*+        |


✅ Final Postfix Expression

abcd^e-*+

*/










/*




Example (one frame):

Approach Used:
Stack-based Infix → Postfix Conversion


Base Case
=========
• If operand (A–Z / a–z / 0–9)  
  → Directly add to answer  
• Stack is used only for operators and brackets  


Input:
------
Infix Expression:
(A+B)*(C-D)

Output:
-------
Postfix Expression:
AB+CD-*


Operator Priority
=================
^  → 3   (Highest)  
* / → 2  
+ - → 1   (Lowest)  


How the Code Works
=================

Rule 1: Operand
---------------
If character is:
A–Z, a–z, 0–9  
→ Append directly to postfix string  


Rule 2: Opening Bracket '('
---------------------------
• Push into stack  
• Marks start of a sub-expression  


Rule 3: Closing Bracket ')'
---------------------------
• Pop from stack and add to postfix  
• Stop when '(' is found  
• Pop '(' but DO NOT add it to answer  


Rule 4: Operator (+, -, *, /, ^)
--------------------------------
• While stack is NOT empty  
• AND priority(current) ≤ priority(stack top)  
  → Pop stack top and add to postfix  

• Push current operator into stack  


Final Step
==========
After traversal:
• Pop all remaining operators from stack  
• Append to postfix string  


Why Stack Is Needed
===================
✔ Maintains operator precedence  
✔ Handles nested expressions  
✔ Ensures correct evaluation order  


Bracket Handling (Key Concept)
==============================
• '(' delays operators  
• ')' flushes operators till '('  
• Brackets never appear in postfix  


Time Complexity (T.C):
O(N)


Space Complexity (S.C):
O(N)


Final Takeaway
==============
Use stack because:
✔ Operators must wait based on priority  
✔ Brackets control evaluation order  
✔ Clean, standard, interview-ready solution 💯







*/



#include<bits/stdc++.h>
using namespace std;


int priority(char ch){

    if(ch == '^') return 3;
    else if (ch == '*' || ch == '/') return 2;
    else if (ch == '+' || ch == '-') return 1;
    else return -1;

}



string InfixToPostfix(string s){

    int i=0;
    string ans = "";
    stack<char>st;

    while(i < s.length()){

        if((s[i] >= 'A' &&  s[i] <= 'Z') || (s[i] >= 'a' &&  s[i] <= 'z') || (s[i] >= '0' && s[i] <= '9')){
             ans += s[i];
        }
        else{

            if(s[i] == '('){
                st.push(s[i]);
            }
            else if(s[i] == ')'){

                while(!st.empty() && st.top() != '('){
                    ans += st.top();
                    st.pop();
                }
                st.pop();
            }
            else{

                while(!st.empty() && priority(s[i]) <= priority(st.top())){
                    ans += st.top();
                    st.pop();
                }
                st.push(s[i]);

            }
        }

        i++;
    }

    while(!st.empty()){
        ans += st.top();
        st.pop();
    }

    return ans;
}






int main(){


    string s = "a+b*(c^d-e)";

    cout<<"Convert Infix expression Into Postfix Expresstion:- ";
    cout<<InfixToPostfix(s);

    return 0;
}