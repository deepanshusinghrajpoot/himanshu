/*



Ques:- Balanced Paranthesis
---------------------------


s = ()[{}()]   => this is balance paranthesis
s = ()[{}(])   => this is not balance paranthesis





Example (one frame):

Approach Used:
Stack-based Parenthesis Matching


Base Case
=========
• If a closing bracket appears when stack is empty  
  → Invalid  
• After full traversal, stack must be empty  
  → Otherwise invalid  


Input 1 (Balanced):
-------------------
s = "{[()]}"

Output:
Balanced → true


Input 2 (Not Balanced):
----------------------
s = "{[(])}"

Output:
Not Balanced → false


How the Code Works
=================

Rule
----
• Opening brackets → PUSH into stack  
• Closing brackets →  
  – Stack must NOT be empty  
  – Top of stack must match the closing bracket  


Step-by-Step Logic
==================

Traversal:
----------
Loop through each character in string


Case 1: Opening bracket
-----------------------
'(' , '{' , '['  
→ Push into stack  


Case 2: Closing bracket
-----------------------
')' , '}' , ']'  

1️⃣ If stack is empty  
   → No matching opening  
   → return false  

2️⃣ Pop top element from stack  

3️⃣ Check matching pairs  
   '(' ↔ ')'  
   '{' ↔ '}'  
   '[' ↔ ']'  

4️⃣ If mismatch  
   → return false  


Final Check
===========
After loop ends:
• If stack is empty → Balanced  
• Else → Unmatched openings → Not balanced  


Why `st.empty()` at the End?
============================
✔ Handles extra opening brackets  
✔ Example: "(((" → stack not empty → false  


Edge Cases Covered
==================
• Starts with closing bracket → false  
• Extra opening bracket → false  
• Nested brackets → handled  
• Mixed types → handled  


Time Complexity (T.C):
O(N)


Space Complexity (S.C):
O(N)


Final Takeaway
==============
Use stack because:
✔ Last opening must close first  
✔ Perfect for nested structures  

Classic and interview-favorite problem 👍





*/




#include<bits/stdc++.h>
using namespace std;


bool checkBalancedParanthesis(string s){

    stack<char>st;

    for(int i=0; i<s.length(); i++){

        if(s[i] == '(' || s[i] == '{' || s[i] == '['){
            st.push(s[i]);
        }
        else{

            if(st.empty()) return false;

            char ch = st.top(); st.pop();

            if((ch == '(' && s[i] == ')') || (ch == '{' && s[i] == '}') || (ch == '[' && s[i] == ']') ){

            }
            else{
                return false;
            }
        }
    }


    return st.empty();
}



int main(){


    string s = "[{}()]({}[)]";

    cout<<"Check Balanced Paranthesis:- ";
    cout<<checkBalancedParanthesis(s);


    return 0;
}