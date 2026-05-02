/*


🔹 C++ String & ASCII Concepts
--------------------------------

1. Character Basics & ASCII
---------------------------

A char in C++ stores 1 byte (8 bits).
It actually stores an integer value (0–255) → which maps to ASCII.
ASCII (American Standard Code for Information Interchange):


'A' → 65, 'Z' → 90
'a' → 97, 'z' → 122
'0' → 48, '9' → 57







IMPORTANT string STL functions
==============================


s.substr(pos, len)     // extract substring



s.push_back(ch)        // add character at end
s.pop_back()           // remove last character

s.size()               // return length of string
s.length()             // same as size()

s.empty()              // check if string is empty

s.clear()              // remove all characters







s.front()              // first character
s.back()               // last character







s.append(str)          // add string at end
s += str               // append string

s.insert(pos, str)     // insert string at position
s.erase(pos, len)      // erase characters

s.find(str)            // return first index or npos
s.substr(pos, len)     // extract substring

s.compare(str)         // return 0 if equal

s.c_str()              // convert to C-style string

*/









/*





🔑 Important String Conversion Concepts (DSA Ready)




1️⃣ Convert character digit → integer
int digit = s[i] - '0';




2️⃣ Convert lowercase → uppercase
s[i] = s[i] - 'a' + 'A';




3️⃣ Convert uppercase → lowercase
s[i] = s[i] - 'A' + 'a';




4️⃣ Convert numeric string → integer number
int num = 0;
for(char ch : s){
    num = num * 10 + (ch - '0');
}





5️⃣ Convert integer → string
string s = to_string(num);






6️⃣ Check character is digit or not
if(s[i] >= '0' && s[i] <= '9')





7️⃣ Check character is lowercase
if(s[i] >= 'a' && s[i] <= 'z')





8️⃣ Check character is uppercase
if(s[i] >= 'A' && s[i] <= 'Z')





9️⃣ Convert entire string to uppercase
for(int i=0; i<s.size(); i++){
    if(s[i] >= 'a' && s[i] <= 'z')
        s[i] = s[i] - 'a' + 'A';
}




🔟 Convert entire string to lowercase
for(int i=0; i<s.size(); i++){
    if(s[i] >= 'A' && s[i] <= 'Z')
        s[i] = s[i] - 'A' + 'a';
}











1️⃣1️⃣ Convert character → ASCII value
int ascii = s[i];

1️⃣2️⃣ Convert ASCII value → character
char ch = (char)ascii;

1️⃣3️⃣ Compare characters (lexicographically)
if(s1[i] > s2[i])

1️⃣4️⃣ Reverse character digit → digit value
int digit = s[i] & 15;   // Fast trick

1️⃣5️⃣ Check alphabet or not
if((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z'))

1️⃣6️⃣ Toggle case (upper ↔ lower)
if(s[i] >= 'a' && s[i] <= 'z')
    s[i] = s[i] - 'a' + 'A';
else if(s[i] >= 'A' && s[i] <= 'Z')
    s[i] = s[i] - 'A' + 'a';







*/
