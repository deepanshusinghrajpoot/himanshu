import React from 'react'



/*




----------------------------------------------------------------------------------------------------------------------------------------
                                                         6. Joins
----------------------------------------------------------------------------------------------------------------------------------------

-----------------------
1️⃣ Concept: INNER JOIN
-----------------------


lll INNER JOIN returns only rows where the join condition matches in both tables.
lll    | `INNER JOIN`      | Matches records in both tables            |


Syntax:

      SELECT columns
      FROM table1
      INNER JOIN table2
      ON table1.column = table2.column;


SELECT columns
FROM table1
INNER JOIN table2
ON table1.column = table2.column;


👉  Your Query
-------------

SELECT *
FROM orders_data o
INNER JOIN returns_data r 
ON o.order_id = r.order_id
WHERE r.return_reason = 'Wrong Item' 
AND city = 'Los Angeles';



🔎 Step-by-Step Execution

FROM orders_data o → take all rows from orders_data as o.
INNER JOIN returns_data r ON o.order_id = r.order_id → join rows where order_id exists in both tables.
WHERE r.return_reason = 'Wrong Item' AND city = 'Los Angeles' → filter only rows with the reason 'Wrong Item' and city = 'Los Angeles'.
SELECT* → return all columns from both tables.


 Example Data


orders_data

| order\_id | order\_date | customer\_name | city        | category   | sales |
| --------- | ----------- | -------------- | ----------- | ---------- | ----- |
| 101       | 2025-01-05  | Rahul Sharma   | Delhi       | Furniture  | 1200  |
| 102       | 2025-01-07  | Priya Singh    | Los Angeles | Technology | 2500  |
| 103       | 2025-01-08  | Aman Verma     | Lucknow     | OfficeSup  | 800   |


👉 returns_data

| return\_id | order\_id | return\_reason |
| ---------- | --------- | -------------- |
| 1          | 102       | Wrong Item     |
| 2          | 103       | Damaged        |
| 3          | 101       | Wrong Item     |


👉  Result of Query

| order\_id | order\_date | customer\_name | city        | category   | sales | return\_id | return\_reason |
| --------- | ----------- | -------------- | ----------- | ---------- | ----- | ---------- | -------------- |
| 102       | 2025-01-07  | Priya Singh    | Los Angeles | Technology | 2500  | 1          | Wrong Item     |






------------------------------------
2️⃣ Concept: LEFT JOIN (Definition)
------------------------------------


lll 👉 LEFT JOIN (or LEFT OUTER JOIN) returns:

All rows from the left table
Matching rows from the right table (if available)
If no match is found in the right table, it will return NULL values for the right table’s columns.

| `LEFT JOIN`       | All rows from left + matched from right   |


Syntax:

SELECT columns
FROM left_table
LEFT JOIN right_table
ON left_table.column = right_table.column;


👉  Your Query

SELECT o.*
FROM orders_data o
LEFT JOIN returns_data r 
ON o.order_id = r.order_id
WHERE r.return_reason IS NULL;



🔎 Step-by-Step Execution

FROM orders_data o → take all rows from orders_data as o.
LEFT JOIN returns_data r ON o.order_id = r.order_id → attach matching rows from returns_data, or NULL if no match.
WHERE r.return_reason IS NULL → keep only rows without a match in returns_data (i.e., non-returned orders).
SELECT o.* → return only columns from orders_data.


👉  Example Data

orders_data

| order\_id | customer\_name | city        | category   | sales |
| --------- | -------------- | ----------- | ---------- | ----- |
| 101       | Rahul Sharma   | Delhi       | Furniture  | 1200  |
| 102       | Priya Singh    | Los Angeles | Technology | 2500  |
| 103       | Aman Verma     | Lucknow     | OfficeSup  | 800   |


👉 returns_data

| order\_id | customer\_name | city  | category  | sales |
| --------- | -------------- | ----- | --------- | ----- |
| 101       | Rahul Sharma   | Delhi | Furniture | 1200  |




✅ Explanation:

order_id = 101 → no matching row in returns_data → included
order_id = 102 and 103 → returned → excluded







------------------------------------
2️⃣ Concept: RIGHT JOIN (Definition)
------------------------------------
👉 RIGHT JOIN (or RIGHT OUTER JOIN) returns:

All rows from the right table
Matching rows from the left table (if available)
If no match is found in the left table, it will return NULL values for the left table’s columns.

| `RIGHT JOIN`      | All rows from right + matched from left   |


✅ Syntax:

SELECT columns
FROM left_table
RIGHT JOIN right_table
ON left_table.column = right_table.column;


✅ Example

orders_data

| order\_id | customer\_name | city   |
| --------- | -------------- | ------ |
| 101       | Rahul          | Delhi  |
| 102       | Priya          | Mumbai |


returns_data

| return\_id | order\_id | reason     |
| ---------- | --------- | ---------- |
| 1          | 102       | Wrong Item |
| 2          | 103       | Damaged    |


RIGHT JOIN Query:

SELECT o.order_id, o.customer_name, r.reason
FROM orders_data o
RIGHT JOIN returns_data r
ON o.order_id = r.order_id;

🔎 Result:

| order\_id | customer\_name | reason     |
| --------- | -------------- | ---------- |
| 102       | Priya          | Wrong Item |
| NULL      | NULL           | Damaged    |


📌 Key Point:

All rows from returns_data (right table) are shown.
If matching order_id exists in orders_data, values are shown.
Otherwise, left table columns are NULL.





--------------------------------
🔹 FULL OUTER JOIN (Definition)
--------------------------------

👉 FULL OUTER JOIN returns all records from both tables,

lll It’s basically the combination of LEFT JOIN + RIGHT JOIN.


✅ Syntax:

SELECT columns
FROM table1
FULL OUTER JOIN table2
ON table1.column = table2.column;



✅ Example

orders_data

| order\_id | customer\_name | city    |
| --------- | -------------- | ------- |
| 101       | Rahul          | Delhi   |
| 102       | Priya          | Mumbai  |
| 103       | Aman           | Chennai |


returns_data

| return\_id | order\_id | reason     |
| ---------- | --------- | ---------- |
| 1          | 102       | Wrong Item |
| 2          | 104       | Damaged    |



SELECT o.order_id, o.customer_name, r.reason
FROM orders_data o
FULL OUTER JOIN returns_data r
ON o.order_id = r.order_id;



🔎 Result:

| order\_id | customer\_name | reason     |
| --------- | -------------- | ---------- |
| 101       | Rahul          | NULL       |
| 102       | Priya          | Wrong Item |
| 103       | Aman           | NULL       |
| 104       | NULL           | Damaged    |


📌 Key Points:

101 and 103 appear with NULL in returns_data (no return).
104 appears with NULL in orders_data (return exists but no order in parent table).
102 appears with full match.



⚠️ Note:

VVV.Imp :-  MySQL does NOT support FULL OUTER JOIN directly.
            You have to simulate it using UNION of LEFT JOIN and RIGHT JOIN.




----------------------------
🔹 FULL OUTER JOIN in MySQL
----------------------------

👉 MySQL does not support FULL OUTER JOIN directly.
But we can simulate it using LEFT JOIN + RIGHT JOIN + UNION.


✅ Syntax:

SELECT o.order_id, o.customer_name, r.return_reason
FROM orders_data o
LEFT JOIN returns_data r ON o.order_id = r.order_id

UNION

SELECT o.order_id, o.customer_name, r.return_reason
FROM orders_data o
RIGHT JOIN returns_data r ON o.order_id = r.order_id;



🔹 How it works:

LEFT JOIN → returns all orders + matching returns.
RIGHT JOIN → returns all returns + matching orders.
UNION → combines them to give FULL OUTER JOIN effect.



✅ Example

orders_data

| order\_id | customer\_name | city    |
| --------- | -------------- | ------- |
| 101       | Rahul          | Delhi   |
| 102       | Priya          | Mumbai  |
| 103       | Aman           | Chennai |


returns_data

| return\_id | order\_id | reason     |
| ---------- | --------- | ---------- |
| 1          | 102       | Wrong Item |
| 2          | 104       | Damaged    |




🔹 Example Result:

| order\_id | customer\_name | return\_reason |
| --------- | -------------- | -------------- |
| 101       | Rahul          | NULL           |
| 102       | Priya          | Wrong Item     |
| 103       | Aman           | NULL           |
| 106       | NULL           | Damaged        |




👉 Here:

Orders not returned show NULL in return_reason.
Returns without matching orders show NULL in customer_name.







⚡ Execution Order:

Engine executes in logical order (FROM → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT).

We write in SQL syntax order (SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT).








🔹 SQL Logical Execution Order

Correct Order:

FROM – pick the source table(s).
JOIN / ON – apply joins between tables.
WHERE – filter rows (before grouping).
GROUP BY – group the filtered rows.
HAVING – filter groups (after grouping).
SELECT – choose the columns/expressions.
DISTINCT – remove duplicates from result set.
Aggregate Functions – SUM(), COUNT(), MIN(), MAX(), AVG(), GROUP_CONCAT() are applied here (inside SELECT).
ORDER BY – sort the final result.
LIMIT / TOP / OFFSET – return only required rows.









*/






const Join = () => {
  return (
    <div>Join</div>
  )
}

export default Join