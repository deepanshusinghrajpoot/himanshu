/*


Infix to Prefix
----------------

(A+B)*C-D+F


step
-------

step 1 :-  Peverse The Infix (handle opening and closing bracket)
step 2 :-  Infix To Postfix
stem 3 :-  Reverse that answer




Infix to Prefix (One Frame)
================================

Expression:

(A+B)*C-D+F


Step 1 – Reverse Infix (swap brackets):
-----------------------------------------

(A+B)*C-D+F
→ F+D-C*)B+A(
→ F+D-C*(B+A)


Step 2 – Infix → Postfix:
---------------------------

F+D-C*(B+A)
→ FD+CB+A*-


Step 3 – Reverse Postfix → Prefix:
------------------------------------

FD+CB+A*-
→ -*A+BC+DF


Final Answer:
----------------
Prefix Expression = -*A+BC+DF


Time Complexity (T.C): O(N)
Space Complexity (S.C): O(N)

Formula:
Infix → Prefix = Reverse + Postfix + Reverse ✅







*/



#include<bits/stdc++.h>
using namespace std;


string reverseInfixHandleOpenAndCloseBracket(string s){

    int low = 0;
    int high = s.length() - 1;

    while(low < high){
        char ch = s[low];
        s[low] = s[high];
        s[high] = ch;

        low++;
        high--;
    }

    int i=0;
    while(i < s.length()){

        if(s[i] == ')') s[i] = '(';
        else if(s[i] == '(') s[i] = ')';

        i++;
    }


   return s;
}


int priority(char ch){

    if(ch == '^') return 3;
    else if(ch == '*' || ch == '/') return 2;
    else if(ch == '+' || ch == '-') return 1;
    else return -1;

}



string InfixToPrefix(string s){

    int i=0;  stack<char>st;  string ans = "";

    s = reverseInfixHandleOpenAndCloseBracket(s);

    while(i < s.length()){

        if(( 'a' <= s[i] && s[i] <= 'z') || ( 'A' <= s[i] && s[i] <= 'Z') || ( '0' <= s[i] && s[i] <= '9')){
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
              
               if(s[i] == '^'){
                   while(!st.empty() &&  priority(s[i]) < priority(st.top())){
                        ans += st.top();
                        st.pop();
                   }
               }
               else{
                  while(!st.empty() && priority(s[i]) <= priority(st.top())){
                        ans += st.top();
                        st.pop();
                  }
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

    ans = reverseInfixHandleOpenAndCloseBracket(ans);

    return ans;
}


int main(){


    string s = "(A+B)*C-D+F";

    string prefixExpression = InfixToPrefix(s);

    cout<<prefixExpression;

    return 0;
}