/*



=========== GROUP ANAGRAMS ===========

Problem:
Group strings that are ANAGRAMS of each other.

Two strings are anagrams if:
• They contain the SAME characters
• Frequency of characters is SAME
• Order does NOT matter

-----------------------------------------------------------
Example:
-----------------------------------------------------------

Input:
["eat", "tea", "tan", "ate", "nat", "bat"]

Output:
[
  ["eat", "tea", "ate"],
  ["tan", "nat"],
  ["bat"]
]

-----------------------------------------------------------
Core Idea:
-----------------------------------------------------------

• Anagrams become IDENTICAL after sorting
• Use sorted string as a KEY
• Group original strings using a map

-----------------------------------------------------------
Approach Used:
-----------------------------------------------------------

Sorting + Hash Map

map< sorted_string , list_of_original_strings >

-----------------------------------------------------------
Step-by-Step Logic:
-----------------------------------------------------------

1️⃣ For each word in the list:
   • Store original word
   • Sort the word characters

-----------------------------------------------------------

2️⃣ Use sorted word as KEY:
   mp[sorted_word].push_back(original_word)

-----------------------------------------------------------

3️⃣ All anagrams map to the SAME key
   because sorting normalizes them

-----------------------------------------------------------

4️⃣ Traverse the map:
   • Push all grouped values into answer

-----------------------------------------------------------
Why This Works:
-----------------------------------------------------------

• Sorting removes character order
• Anagrams → same sorted form
• Map automatically groups them together

-----------------------------------------------------------
Visualization:
-----------------------------------------------------------

"eat" → "aet"
"tea" → "aet"
"ate" → "aet"
→ Grouped together

"tan" → "ant"
"nat" → "ant"
→ Grouped together

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------

O(N × K log K)

-----------------------------------------------------------
Where does it come from?
-----------------------------------------------------------

• N = number of strings
• K = average length of each string
• Sorting each string takes O(K log K)
• Done for N strings

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------

O(N × K)

-----------------------------------------------------------
Why O(N × K)?
-----------------------------------------------------------

• Map stores all strings
• Each string of length K is stored once

-----------------------------------------------------------
Valid For:
-----------------------------------------------------------

✔ Uppercase letters
✔ Lowercase letters
✔ Mixed characters
✔ Any order of input

-----------------------------------------------------------
One-Line Interview Answer:
-----------------------------------------------------------

"By sorting each string and using it as a key,
we can group all anagrams efficiently."

===========================================================










*/



#include<bits/stdc++.h>
using namespace std;



vector<vector<string>>group_anagram(vector<string>s){

    vector<vector<string>>ans;

    map<string, vector<string>>mp;

    for(auto word : s){

        string original = word;

        sort(word.begin(), word.end());

        mp[word].push_back(original);
    }

    for(auto p : mp){
        ans.push_back(p.second);
    }

    return ans;
}


int main(){

    vector<vector<string>> testCases = {
        {"eat", "tea", "tan", "ate", "nat", "bat"},
        {"", ""},
        {"a"},
        {"abc", "bca", "cab", "xyz", "zyx"},
        {"listen", "silent", "enlist", "google", "gooegl"}
    };

    for(int i = 0; i < testCases.size(); i++){

        cout << "Test Case " << i + 1 << "\n";
        vector<vector<string>> result = group_anagram(testCases[i]);

        for(auto group : result){
            cout << "[ ";
            for(auto word : group){
                cout << word << " ";
            }
            cout << "]\n";
        }
        cout << "\n";
    }

    return 0;
}