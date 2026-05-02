

/*


=========== CHECK ANAGRAM (USING FREQUENCY ARRAY) ===========

Definition:
--------------------------------------------------
Two strings are ANAGRAMS if:
• They contain the SAME characters
• With the SAME frequency
• Order does NOT matter

--------------------------------------------------
Example:
--------------------------------------------------

s1 = "listen"
s2 = "silent"

✔ Anagram (same characters & counts)

--------------------------------------------------
Key Observation:
--------------------------------------------------

• If lengths differ → NOT anagram
• If character counts match → anagram

--------------------------------------------------
Core Idea:
--------------------------------------------------

• Use a frequency array of size 256 (ASCII)
• Count characters of first string
• Subtract characters of second string
• Final frequencies must be ZERO

--------------------------------------------------
Algorithm Flow:
--------------------------------------------------

1️⃣ If length(s1) ≠ length(s2)
   → return false

2️⃣ Initialize freq[256] = {0}

3️⃣ Traverse s1:
   → freq[ch]++

4️⃣ Traverse s2:
   → freq[ch]--

5️⃣ Check freq array:
   → if any value ≠ 0 → NOT anagram

6️⃣ Else → strings are anagrams

--------------------------------------------------
Why This Works:
--------------------------------------------------

• Matching increments & decrements cancel out
• Any mismatch leaves non-zero frequency

--------------------------------------------------
Time Complexity:
--------------------------------------------------
O(N)

--------------------------------------------------
Where does O(N) come from?
--------------------------------------------------

• One pass over s1 → O(N)
• One pass over s2 → O(N)
• Fixed 256 check → O(1)

--------------------------------------------------
Space Complexity:
--------------------------------------------------
O(1)

--------------------------------------------------
Why O(1)?
--------------------------------------------------

• Frequency array size is CONSTANT (256)
• Independent of input size

--------------------------------------------------
Edge Cases:
--------------------------------------------------

• Different lengths → false
• Empty strings → true
• Case-sensitive (A ≠ a)

--------------------------------------------------
One-Line Interview Answer:
--------------------------------------------------

"Count characters using a frequency array and
verify all counts cancel to zero."

===================================================








| Test Case | s1        | s2        | Output | Correct            |
| --------- | --------- | --------- | ------ | ------------------ |
| 1         | listen    | silent    | True   | ✅                  |
| 2         | triangle  | integral  | True   | ✅                  |
| 3         | rat       | car       | False  | ✅                  |
| 4         | aab       | aba       | True   | ✅                  |
| 5         | abcd      | abc       | False  | ✅                  |
| 6         | ""        | ""        | True   | ✅                  |
| 7         | a         | a         | True   | ✅                  |
| 8         | a         | b         | False  | ✅                  |
| 9         | Dormitory | Dirtyroom | False  | ✅ (case-sensitive) |






*/




#include<iostream>
#include<bits/stdc++.h>
using namespace std;



bool isAnagram(string s1, string s2){

    if(s1.length() != s2.length()) return false;

    int freq[256] = {0};

    for(char ch : s1) freq[ch]++;
    for(char ch : s2) freq[ch]--;

    for(int i=0; i<256; i++){
        if(freq[i] != 0) return false;
    }

    return true;
}



int main(){

    vector<pair<string,string>> testCases = {
        {"listen", "silent"},
        {"triangle", "integral"},
        {"rat", "car"},
        {"aab", "aba"},
        {"abcd", "abc"},
        {"", ""},
        {"a", "a"},
        {"a", "b"},
        {"Dormitory", "Dirtyroom"}   // case-sensitive check
    };

    for(int i = 0; i < testCases.size(); i++){
        cout << "Test Case " << i + 1 << ": "
             << testCases[i].first << " , "
             << testCases[i].second << "\nResult = "
             << (isAnagram(testCases[i].first, testCases[i].second) ? "True" : "False")
             << "\n\n";
    }

    return 0;
}





/*

T.C = O(n)
S.C = O(1)

*/