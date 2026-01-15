/*



=========== LOWER BOUND – DIFFERENT CASE TYPES ===========

CASE 1️⃣: Target present multiple times
Array:
Index:   0   1   2   3   4   5
Array:  [1   2   4   4   4   7]
Target = 4

Result:
[1  2 | 4  4  4  7]
       ↑
Lower Bound = index 2






CASE 2️⃣: Target present once
Array:
Index:   0   1   2   3   4
Array:  [1   3   5   7   9]
Target = 5

Result:
[1  3 | 5 | 7  9]
       ↑
Lower Bound = index 2








CASE 3️⃣: Target not present (in between)
Array:
Index:   0   1   2   3   4
Array:  [1   3   5   7   9]
Target = 6

Result:
[1  3  5 | 7  9]
           ↑
Lower Bound = index 3 (insert position)









CASE 4️⃣: Target smaller than all elements
Array:
Index:   0   1   2   3
Array:  [5   6   7   8]
Target = 2

Result:
[| 5  6  7  8]
 ↑
Lower Bound = index 0









CASE 5️⃣: Target greater than all elements
Array:
Index:   0   1   2   3
Array:  [2   4   6   8]
Target = 10

Result:
[2  4  6  8 |]
              ↑
Lower Bound = index 4 (n)







lll lower_bound = first index where value ≥ target in sorted array

========================================================















*/