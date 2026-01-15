
/*


================ BINARY SEARCH – REQUIRED CONCEPTS =================

🟢 What is Binary Search?
Binary Search is a searching technique that finds an element
by repeatedly dividing the search space into two halves.

🟢 Mandatory Condition (MOST IMPORTANT):
The array / search space MUST be:
- Sorted (ascending or descending)
OR
- Monotonic (answer space moves only in one direction)

🟢 Why Binary Search is Fast:
Each step removes HALF of the remaining elements.

🟢 When to Think About Binary Search:
- Sorted array
- Find first / last occurrence
- Minimum / maximum satisfying a condition
- Answer lies in a range (search space)
- “Optimize”, “minimum”, “maximum”, “smallest”, “largest” keywords

🟢 Types of Binary Search:
1️⃣ Classic Binary Search
   - Find exact element

2️⃣ Lower Bound
   - First index where value ≥ target

3️⃣ Upper Bound
   - First index where value > target

4️⃣ Binary Search on Answer
   - Search on result, not array
   - Used in optimization problems

🟢 Core Variables:
- low  → start of search space
- high → end of search space
- mid  → middle index/value

🟢 Mid Calculation (Safe Formula):
mid = low + (high - low) / 2

🟢 Movement Rules:
If condition is TRUE:
→ Move left (high = mid - 1) OR store answer

If condition is FALSE:
→ Move right (low = mid + 1)

🟢 Loop Condition:
while(low <= high)

🟢 Common Edge Cases:
- Empty array
- Single element
- Target not present
- Duplicate elements
- Overflow in mid calculation

🟢 Time Complexity:
O(log N)

🟢 Space Complexity:
O(1)

🟢 Interview Golden Rule:
If answer space is sorted or monotonic → APPLY BINARY SEARCH.

🟢 One-Line Takeaway:
Binary Search is about eliminating half, not checking every element.

===============================================================










*/