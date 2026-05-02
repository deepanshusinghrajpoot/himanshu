

/*

=========== WORD PATTERN (HASH MAP – INDEX MAPPING) ===========

Problem:
Check whether string `s` follows the SAME pattern as string `pattern`.

-----------------------------------------------------------
Example:
-----------------------------------------------------------
pattern = "abba"
s       = "dog cat cat dog"

✔ Valid (same structure)

-----------------------------------------------------------
Core Idea:
-----------------------------------------------------------

• Each pattern character must map to ONE unique word  
• Each word must map back to ONE unique pattern character  
• Mapping must be CONSISTENT in order and position

-----------------------------------------------------------
Key Technique Used:
-----------------------------------------------------------

Index-based mapping using TWO maps:

1️⃣ charMap   → maps pattern character → last seen index  
2️⃣ wordMap   → maps word → last seen index  

👉 Instead of storing values directly, we store **positions (i+1)**

-----------------------------------------------------------
Why Index Mapping Works:
-----------------------------------------------------------

If:
charMap[pattern[j]] == wordMap[word]

✔ They appeared together last time  
❌ If not equal → pattern breaks

-----------------------------------------------------------
Step-by-Step Flow:
-----------------------------------------------------------

• Traverse string `s` character by character
• Build each word until space is found
• For each word:
   - Compare last index of pattern char and word
   - If mismatch → return false
   - Update both maps with current position (j+1)
• Move to next pattern character

-----------------------------------------------------------
Final Validation:
-----------------------------------------------------------

• Count total words in `s`
• If count != pattern length → return false

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
O(N log N)

Where:
• N = number of characters / words
• log N comes from map operations (insert / find)

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
O(N)

• Maps store pattern characters and words

-----------------------------------------------------------
Why This Solution Is Robust:
-----------------------------------------------------------

✔ Prevents:
• One character mapping to multiple words
• Multiple characters mapping to same word

✔ Order-sensitive
✔ Works for all valid inputs

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------
"By mapping pattern characters and words to their last
seen indices, we ensure a one-to-one and ordered relationship."

===========================================================








| Test Case | Pattern | String           | Expected                 |
| --------- | ------- | ---------------- | ------------------------ |
| 1         | abba    | dog cat cat dog  | true                     |
| 2         | abba    | dog cat cat fish | false                    |
| 3         | aaaa    | dog cat cat dog  | false                    |
| 4         | jquery  | jquery           | false                    |
| 5         | ab      | dog cat          | true                     |
| 6         | ab      | dog cat fish     | ❌ **undefined behavior** |




*/


/*



| j | pattern[j] | word | charMap | wordMap |
| - | ---------- | ---- | ------- | ------- |
| 0 | a          | dog  | a→1     | dog→1   |
| 1 | b          | cat  | b→2     | cat→2   |
| 2 | b          | cat  | b→2     | cat→2   |
| 3 | a          | dog  | a→4     | dog→4   |






*/


#include<bits/stdc++.h>
using namespace std;



 bool wordPattern(string pattern, string s) {


        map<string, int>wordMap;
        map<char, int>charMap;

        int count = 0;
        string word = "";

        int j=0;
        for(int i=0; i<s.length(); i++){

            char ch = s[i];

            if(ch == ' '){
                if(!word.empty()){

                   if(charMap[pattern[j]] != wordMap[word]) return false;

                   charMap[pattern[j]] = j+1;
                   wordMap[word] = j+1;

                   j++;
                   
                   count++;
                   word = "";
                }

            }else{
                word += ch;
            }
        }
        if(!word.empty()){
              if(charMap[pattern[j]] != wordMap[word]) return false;

              charMap[pattern[j]] = j+1;
              wordMap[word] = j+1;
              
              count++;
        }

        if(count != pattern.length()) return false;
        
        return true;
}



int main(){

    vector<pair<string,string>> testCases = {
        {"abba", "dog cat cat dog"},     // true
        {"abba", "dog cat cat fish"},   // false
        {"aaaa", "dog cat cat dog"},    // false
        {"jquery", "jquery"},           // false (important case)
        {"ab", "dog cat"},              // true
        {"ab", "dog cat fish"}           // ❌ risky case
    };

    for(int i = 0; i < testCases.size(); i++){
        cout << "Test Case " << i + 1 << "\n";
        cout << "Pattern: " << testCases[i].first << "\n";
        cout << "String : " << testCases[i].second << "\n";
        cout << "Output : "
             << (wordPattern(testCases[i].first, testCases[i].second) ? "true" : "false")
             << "\n\n";
    }

    return 0;
}
