/*



=========== LONGEST PALINDROMIC SUBSTRING (BRUTE FORCE) ===========

Definition:
A Palindromic Substring is a contiguous part of a string
that reads the SAME forward and backward.

-----------------------------------------------------------
Example:
-----------------------------------------------------------
Input  : "babad"
Output : "bab" or "aba"

-----------------------------------------------------------
Core Idea:
-----------------------------------------------------------

• Generate ALL possible substrings
• Check each substring if it is a PALINDROME
• Keep track of the LONGEST palindromic substring found

-----------------------------------------------------------
Palindrome Check Logic:
-----------------------------------------------------------

Using TWO POINTERS:

• left  → start of substring
• right → end of substring

While left < right:
→ if s[left] != s[right] → NOT palindrome
→ else move inward

-----------------------------------------------------------
Algorithm Steps:
-----------------------------------------------------------

1️⃣ Loop i from 0 to n-1 (start index)
2️⃣ Loop j from i to n-1 (end index)
3️⃣ Extract substring s[i…j]
4️⃣ Check if substring is palindrome
5️⃣ If palindrome AND length > maxLen:
    → update maxLen
    → update answer string

-----------------------------------------------------------
Why It Works:
-----------------------------------------------------------

• Every possible substring is checked
• Palindrome condition guarantees correctness
• Maximum length tracking ensures longest result

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N³)

-----------------------------------------------------------
Where does O(N³) come from?
-----------------------------------------------------------

• O(N²) → generating all substrings
• O(N)  → palindrome check for each substring

Total:
→ O(N² × N) = O(N³)

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(1) auxiliary space  
(ignoring substring creation cost)

-----------------------------------------------------------
Limitations:
-----------------------------------------------------------

❌ Very slow for large strings  
❌ Repeated palindrome checks

-----------------------------------------------------------
Key Interview Takeaway:
-----------------------------------------------------------

"This brute-force solution is correct but inefficient.
Optimized approaches like Expand Around Center or DP
reduce time to O(N²)."

===========================================================









*/




#include<bits/stdc++.h>
using namespace std;

    bool isPalindromic(string s){
        
        int left = 0;
        int right = s.length()-1;

        while(left < right){

            if(s[left] != s[right]) return false;

            left++;
            right--;
        }

        return true;
    }


    string longest_palindromic_substr(string s) {


        int maxLen = INT_MIN;
        string max_str = "";

        for(int i=0; i<s.length(); i++){
            for(int j=i; j<s.length(); j++){
                if(isPalindromic(s.substr(i, j-i+1))){
                    if(j-i+1 > maxLen){
                        maxLen = j-i+1;
                        max_str = s.substr(i, j-i+1);
                    }
                }
            }
        }

        return max_str;
    }

int main(){

    vector<string> testCases = {
        "babad",              // bab / aba
        "cbbd",               // bb
        "a",                  // a
        "ac",                 // a / c
        "racecar",            // racecar
        "forgeeksskeegfor",   // geeksskeeg
        "",                   // ""
        "aaaa"                // aaaa
    };

    for(int i = 0; i < testCases.size(); i++){
        cout << "Test Case " << i + 1 << "\n";
        cout << "Input  : " << testCases[i] << "\n";
        cout << "Output : "
             << longest_palindromic_substr(testCases[i]) << "\n\n";
    }

    return 0;
}