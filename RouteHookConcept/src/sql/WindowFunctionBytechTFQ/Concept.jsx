import React from 'react'

/*


🧠 Core SQL Concept Behind This Problem
SQL Logical Query Execution Order

SQL is declarative, not procedural.
So SQL does NOT run top-to-bottom as written.

🔢 Logical Execution Order (Important)

FROM – identify source tables
JOIN / ON – combine tables
WHERE – filter rows
GROUP BY – group rows
HAVING – filter groups
WINDOW FUNCTIONS – ROW_NUMBER(), RANK()
SELECT – choose output columns
ORDER BY – final sorting

❌ Why WHERE rn <= 2 FAILS
............................
Your query
SELECT e.*,
       ROW_NUMBER() OVER (PARTITION BY dept_name ORDER BY emp_id) AS rn
FROM employee e
WHERE rn <= 2;

What SQL tries to do internally

1️⃣ FROM employee
2️⃣ WHERE rn <= 2 ❌
3️⃣ ROW_NUMBER() is calculated later

🚫 Problem:
At step 2, rn does not exist yet
because window functions are executed after WHERE.

👉 This is the core reason it fails.


🧠 Core Rule (Very Important)
..................................
WHERE filters rows BEFORE window functions are calculated

So:

WHERE ❌ cannot use window function results

HAVING ❌ cannot use window functions either

✅ Why Subquery / CTE Works
Step-by-step flow (Correct Query)


SELECT *
FROM (
    SELECT e.*,
           ROW_NUMBER() OVER (PARTITION BY dept_name ORDER BY emp_id) AS rn
    FROM employee e
) x
WHERE rn <= 2;

Execution Breakdown

Inner Query

Calculates ROW_NUMBER()

Creates a temporary result set with column rn

Outer Query

Now rn exists

WHERE rn <= 2 works perfectly

✅ This follows SQL execution order correctly.




 */






const Concept = () => {
  return (
    <div>Concept</div>
  )
}

export default Concept