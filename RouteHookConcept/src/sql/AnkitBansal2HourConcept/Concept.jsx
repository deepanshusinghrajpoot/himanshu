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





const Concept = () => {
  return (
    <div>Concept</div>
  )
}

export default Concept