

/*


=========== FLOOR & CEIL – VISUAL ARRAY FLOW ===========

Sorted Array:
Index:   0   1   2   3   4   5
Array:  [1   3   5   7   9  11]
Target = 6

-----------------------------------------------------
🟢 FLOOR VALUE (largest element ≤ target)

Result:
[1  3  5 | 7  9  11]
        ↑
Floor = 5 (index 2)

-----------------------------------------------------
🟢 CEIL VALUE (smallest element ≥ target)

Result:
[1  3  5 | 7  9  11]
            ↑
Ceil = 7 (index 3)

-----------------------------------------------------
🟢 DIFFERENT CASES
-----------------------------------------------------

CASE 1️⃣: Target present
Target = 7

[1  3  5 | 7 | 9  11]
           ↑
Floor = 7,  Ceil = 7

-----------------------------------------------------

CASE 2️⃣: Target smaller than all elements
Target = 0

[| 1  3  5  7  9  11]
 ↑
Floor = NOT EXIST
Ceil  = 1

-----------------------------------------------------

CASE 3️⃣: Target greater than all elements
Target = 15

[1  3  5  7  9  11 |]
                   ↑
Floor = 11
Ceil  = NOT EXIST

-----------------------------------------------------

CASE 4️⃣: Target not present (in between)
Target = 8

[1  3  5  7 | 9  11]
            ↑
Floor = 7
Ceil  = 9

-----------------------------------------------------
🟢 Time Complexity:
O(log N)

🟢 Space Complexity:
O(1)

🟢 Takeaway:
Floor → max ≤ target  
Ceil  → min ≥ target

=====================================================




=========== FLOOR & CEIL (INDEX-BASED) – EQUAL ELEMENT ===========

Sorted Array:
Index:   0   1   2   3   4   5   6
Array:  [1   3   5   7   7   7   9]
Target = 7

-----------------------------------------------------
🟢 CEIL (first index where value ≥ target)
→ LEFTMOST occurrence of target

Result:
[1  3  5 | 7  7  7 | 9]
           ↑
Ceil index = 3

-----------------------------------------------------
🟢 FLOOR (last index where value ≤ target)
→ RIGHTMOST occurrence of target

Result:
[1  3  5 | 7  7  7 | 9]
                 ↑
Floor index = 5

-----------------------------------------------------
🟢 Key Interpretation:
Ceil  = lower_bound(target)
Floor = upper_bound(target) - 1

-----------------------------------------------------
🟢 Values:
Ceil value  = 7
Floor value = 7

-----------------------------------------------------
🟢 Time Complexity:
O(log N)

🟢 Space Complexity:
O(1)

🟢 Takeaway:
Duplicates →  
Ceil = first target  
Floor = last target  

=====================================================


*/


#include <bits/stdc++.h>
using namespace std;

int ceil(vector<int> &arr, int target)
{ // floor <= target

    int low = 0;
    int high = arr.size() - 1;

    while (low <= high)
    {

        int mid = low + (high - low) / 2;

        if (arr[mid] <= target)
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }

    return high;
}

int main()
{

    vector<int> arr{4, 5, 7, 9, 12, 34, 35, 35, 35, 35, 35, 78, 90, 123, 456, 789, 12345};

    int cl = ceil(arr, 35);
    int fl = lower_bound(arr.begin(), arr.end(),35) - arr.begin();

    cout<<"floor index:- "<<fl<<endl;
    cout<<"ciel index:- "<<cl<<endl;

                                                         

    return 0;
}