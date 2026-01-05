/*






Alternate way to write SQL query using Window Functions
=======================================================

SELECT *,
FIRST_VALUE(product_name) OVER w AS most_exp_product,
LAST_VALUE(product_name) OVER w AS least_exp_product
FROM product
WINDOW w AS (PARTITION BY product_category ORDER BY price DESC
             RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING);






⭐ 1️⃣ Syntax Order of the WINDOW Keyword
---------------------------------------------

✔ Correct SQL Syntax Order (Actual Order of Clauses)
SELECT ...
FROM ...
WHERE ...
GROUP BY ...
HAVING ...
WINDOW window_name AS (...)
ORDER BY ...

✔ Why?

Because the WINDOW clause sits between HAVING and ORDER BY.


⭐ 2️⃣ Logical Execution Order (How SQL Actually Executes Internally)
---------------------------------------------------------------------

SQL does not execute in the order written.

✔ Logical Execution Order

(Important for interviews)

FROM — load table
WHERE — filter rows
GROUP BY — make groups
HAVING — filter groups
WINDOW — create partitions + ordering + frame
SELECT — evaluate window functions
ORDER BY — final sorting

✔ Window Function Internal Flow

Inside SELECT:

Form partitions (PARTITION BY)
Order rows (ORDER BY)
Apply Frame (ROWS / RANGE)
Execute function (e.g., RANK, NTH_VALUE, CUME_DIST)





⭐ 3️⃣ NTH_VALUE()
======================

✔ Definition (Easy to Understand)

lll NTH_VALUE(col, n) → returns the nth value from the ordered window.

NTH_VALUE(col, 1) → first value
NTH_VALUE(col, 2) → second value
NTH_VALUE(col, 3) → third value

lll ⚠ Needs full frame: When we use NTH_VALUE and LAST_VALUE window function need full frame
    RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING

    Default frame : RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW


❓ Question

Write a query to display the second most expensive product under each category.

✔ Correct Query
SELECT *,
NTH_VALUE(product_name, 2) OVER w AS second_most_exp_product
FROM product
WINDOW w AS (
    PARTITION BY product_category
    ORDER BY price DESC
    RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
);


✔ Shows the 2nd highest product in each category.

⚠ Note: LAST_VALUE() & NTH_VALUE() always require a proper frame clause.





⭐ 4️⃣ NTILE()
================

✔ Definition (Easy)

lll NTILE(n) breaks the ordered rows into n equal buckets.

Example:
NTILE(3):

Bucket 1 → top items
Bucket 2 → middle items
Bucket 3 → lowest items


✔ PARTITION BY is optional
If omitted → entire table is considered one group.


❓ Question

Segregate phones into expensive, mid-range, and cheaper phones.

✔ Query
SELECT product_name,
CASE 
     WHEN x.buckets = 1 THEN 'Expensive Phones'
     WHEN x.buckets = 2 THEN 'Mid Range Phones'
     WHEN x.buckets = 3 THEN 'Cheaper Phones'
END AS phone_category
FROM (
     SELECT *,
     NTILE(3) OVER (ORDER BY price DESC) AS buckets
     FROM product
     WHERE product_category = 'phone'
) x;


✔ Bucket 1 = Expensive
✔ Bucket 2 = Mid-range
✔ Bucket 3 = Cheaper




⭐ 5️⃣ CUME_DIST()
=====================

✔ Definition (Easy)

lll CUME_DIST() tells what percentage of rows are less than or equal to the current row.

lll ✔ Value Range
    0 < CUME_DIST <= 1

lll ✔ Formula
    CUME_DIST = (Number of rows with value ≤ current row) / (Total rows)



| id | name   | marks |
| -- | ------ | ----- |
| 1  | Amit   | 95    |
| 2  | Priya  | 88    |
| 3  | Rohit  | 88    |
| 4  | Sneha  | 75    |
| 5  | Deepak | 60    |

We calculate CUME_DIST() in descending order of marks (highest first).

🧮 Step-by-Step Calculation
1️⃣ Order rows by marks DESC:

| Rank | name   | marks |
| ---- | ------ | ----- |
| 1    | Amit   | 95    |
| 2    | Priya  | 88    |
| 3    | Rohit  | 88    |
| 4    | Sneha  | 75    |
| 5    | Deepak | 60    |

2️⃣ Apply the formula for each row
⭐ Row 1 — Amit (95)

Rows ≤ 95 = 5 rows
Total rows = 5

CUME_DIST = 5/5 = 1.0

⭐ Row 2 — Priya (88)

Rows ≤ 88 = rows with marks 88, 75, 60 → 4 rows
Total = 5

CUME_DIST = 4/5 = 0.80

⭐ Row 3 — Rohit (88)

Rows ≤ 88 = still 4 rows
CUME_DIST = 4/5 = 0.80

⭐ Row 4 — Sneha (75)

Rows ≤ 75 = 75, 60 → 2 rows
Total = 5
CUME_DIST = 2/5 = 0.40

⭐ Row 5 — Deepak (60)

Rows ≤ 60 = 1 row
Total = 5
CUME_DIST = 1/5 = 0.20

📌 Final Output Table

| name   | marks | cume_dist |
| ------ | ----- | --------- |
| Amit   | 95    | 1.00      |
| Priya  | 88    | 0.80      |
| Rohit  | 88    | 0.80      |
| Sneha  | 75    | 0.40      |
| Deepak | 60    | 0.20      |






❓ Question
Fetch all products that make up the first 30% of data, based on highest prices.

✔ Query

SELECT product_name, (cume_dist_percentage || '%') AS cume_dist_percentage
FROM (
      SELECT *,
      CUME_DIST() OVER (ORDER BY price DESC) AS cume_distribution,
      ROUND(CUME_DIST() OVER (ORDER BY price DESC)::numeric * 100, 2) 
             AS cume_dist_percentage
      FROM product
     ) x
WHERE x.cume_dist_percentage <= 30;


✔ Returns top 30% of items (by price, descending).







⭐ 6️⃣ PERCENT_RANK()
======================

lll ✔ Definition (Easy)

Shows the relative rank of the current row as a percentage.

lll✔ Value Range
0 <= PERCENT_RANK <= 1

lll✔ Formula
PERCENT_RANK = (Rank of current row - 1) / (Total rows - 1)


lll Important:

PERCENT_RANK is based on RANK(), not ROW_NUMBER.
The first row always gets 0.
The last row always gets 1.


📌 Example Table — Students & Marks

| id | name   | marks |
| -- | ------ | ----- |
| 1  | Amit   | 95    |
| 2  | Priya  | 88    |
| 3  | Rohit  | 88    |
| 4  | Sneha  | 75    |
| 5  | Deepak | 60    |


(Notice: Priya and Rohit get same rank 2, Sneha becomes 4 — rank gap)


🧮 Step 2: Apply PERCENT_RANK formula
Total rows = 5 → denominator = 5 − 1 = 4

⭐ Row 1 – Amit (Rank = 1)
--------------------------

(1 − 1)/4 = 0

✔ PERCENT_RANK = 0

⭐ Row 2 – Priya (Rank = 2)
---------------------------

(2 − 1)/4 = 0.25

✔ PERCENT_RANK = 0.25


⭐ Row 3 – Rohit (Rank = 2)
----------------------------

Same rank → same result

✔ 0.25


⭐ Row 4 – Sneha (Rank = 4)
----------------------------

(4 − 1)/4 = 0.75

✔ 0.75


⭐ Row 5 – Deepak (Rank = 5)
-----------------------------

(5 − 1)/4 = 1

✔ 1.00



📌 Final Output Table

| name   | marks | rank | percent_rank |
| ------ | ----- | ---- | ------------ |
| Amit   | 95    | 1    | 0.00         |
| Priya  | 88    | 2    | 0.25         |
| Rohit  | 88    | 2    | 0.25         |
| Sneha  | 75    | 4    | 0.75         |
| Deepak | 60    | 5    | 1.00         |




❓ Question
Identify how much percentage more expensive “Jacket” is compared to all products.

✔ Correct Query
SELECT product_name, per_rank
FROM (
     SELECT *,
     PERCENT_RANK() OVER (ORDER BY price) AS percentage_rank,
     ROUND(PERCENT_RANK() OVER (ORDER BY price)::numeric * 100, 2) AS per_rank
     FROM product
) x
WHERE x.product_name = 'Jacket';


✔ Shows what percentage of products are cheaper than Jacket.


















*/