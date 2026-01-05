import React from 'react'


/*



1️⃣ Logical Execution Order (How SQL actually executes)
-------------------------------------------------------

SQL engine executes in this order:

FROM → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT/TOP




2️⃣ Writing Order (How we write queries)
----------------------------------------

When we write a query, we don’t write in that order.
We follow this syntax order:

SELECT column1, column2, aggregate_function
FROM table_name
WHERE condition
GROUP BY column
HAVING aggregate_condition
ORDER BY column ASC|DESC
LIMIT number;   -- (or TOP in SQL Server)



Example:
SELECT city, SUM(sales) AS total_sales
FROM orders_data
WHERE sales > 500
GROUP BY city
HAVING SUM(sales) > 2000
ORDER BY total_sales DESC
LIMIT 5;



👉 So Deepanshu, remember:

Engine executes in logical order (FROM → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT).

We write in SQL syntax order (SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT).



🔹 SQL Syntax Order (Query Writing Order)

Correct Order:

SELECT – choose columns or expressions
DISTINCT – remove duplicate rows
FROM – specify source table(s)
JOIN / ON – combine tables using conditions
WHERE – filter rows
GROUP BY – group rows
HAVING – filter grouped data
ORDER BY – sort the final result.
LIMIT / TOP / OFFSET – restrict number of rows


🔹 SQL Logical Execution Order(How DB Executes)

Correct Order:

FROM – pick the source table(s).
JOIN / ON – apply joins between tables.
lll WHERE – filter rows (before grouping).
GROUP BY – group the filtered rows.
lll HAVING – filter groups (after grouping).
SELECT – choose the columns/expressions.
DISTINCT – remove duplicates from result set.
Aggregate Functions – SUM(), COUNT(), MIN(), MAX(), AVG(), GROUP_CONCAT() are applied here (inside SELECT).
ORDER BY – sort the final result.
LIMIT / TOP / OFFSET – return only required rows.






🧠 What is the use of WITH in SQL?
=======================================
WITH is used to create a Common Table Expression (CTE).
A CTE is a temporary named result set that exists only for the duration of the query.


📌 Why do we use WITH?
--------------------------
1️⃣ Improves Readability & Structure

Breaks complex queries into logical, readable blocks
Makes SQL easier to understand and maintain

WITH dept_salary AS (
    SELECT dept, MAX(salary) AS max_salary
    FROM employees
    GROUP BY dept
)
SELECT *
FROM dept_salary;


*/





const Concept = () => {
  return (
    <div>Concept</div>
  )
}

export default Concept