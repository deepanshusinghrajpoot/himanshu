import React from 'react'



/*


************************
------------------------
## 2. Sorting (ORDER BY)
------------------------
************************


* Sort by multiple columns:


📌 Parent Table: orders_data

| order\_id | order\_date | ship\_date | customer\_name | region | city    | category   | product\_id | sales | quantity | profit |
| --------- | ----------- | ---------- | -------------- | ------ | ------- | ---------- | ----------- | ----- | -------- | ------ |
| 101       | 2025-01-05  | 2025-01-08 | Rahul Sharma   | North  | Delhi   | Furniture  | P001        | 1200  | 2        | 200    |
| 102       | 2025-01-07  | 2025-01-10 | Priya Singh    | South  | Chennai | Technology | P002        | 2500  | 1        | 500    |
| 103       | 2025-01-08  | 2025-01-12 | Aman Verma     | North  | Lucknow | OfficeSup  | P003        | 800   | 5        | 100    |
| 104       | 2025-01-10  | 2025-01-15 | Neha Gupta     | West   | Mumbai  | Furniture  | P004        | 1500  | 3        | 250    |
| 105       | 2025-01-11  | 2025-01-16 | Suresh Kumar   | East   | Kolkata | Technology | P005        | 3000  | 2        | 600    |



SELECT * 
FROM orders_data 
ORDER BY order_date, profit;


📌 Result Table
👉 The result is sorted first by order_date (ascending by default), and if two rows have the same date, then it sorts by profit.

| order\_id | order\_date | ship\_date | customer\_name | region | city    | category   | product\_id | sales | quantity | profit |
| --------- | ----------- | ---------- | -------------- | ------ | ------- | ---------- | ----------- | ----- | -------- | ------ |
| 101       | 2025-01-05  | 2025-01-08 | Rahul Sharma   | North  | Delhi   | Furniture  | P001        | 1200  | 2        | 200    |
| 102       | 2025-01-07  | 2025-01-10 | Priya Singh    | South  | Chennai | Technology | P002        | 2500  | 1        | 500    |
| 103       | 2025-01-08  | 2025-01-12 | Aman Verma     | North  | Lucknow | OfficeSup  | P003        | 800   | 5        | 100    |
| 104       | 2025-01-10  | 2025-01-15 | Neha Gupta     | West   | Mumbai  | Furniture  | P004        | 1500  | 3        | 250    |
| 105       | 2025-01-11  | 2025-01-16 | Suresh Kumar   | East   | Kolkata | Technology | P005        | 3000  | 2        | 600    |

👉 Here, since all order_date values are unique, sorting by profit didn’t come into play — but if two orders had the same date, then the one with lower profit would appear first.



📌 Functionality of SQL Keywords

SELECT * → Selects all columns.
FROM orders_data → Data is taken from orders_data table.
ORDER BY order_date, profit → Sort rows by order_date first, then by profit within same dates.


📌 Execution Order

FROM → Load table.
SELECT → Pick all columns (*).
ORDER BY → Sort the rows by order_date, then profit.


✅ So this query gives you the entire dataset, but sorted by date and profit.





* Descending & ascending order:
-------------------------------

📌 Parent Table: orders_data

| order\_id | order\_date | ship\_date | customer\_name | region | city    | category   | product\_id | sales | quantity | profit |
| --------- | ----------- | ---------- | -------------- | ------ | ------- | ---------- | ----------- | ----- | -------- | ------ |
| 101       | 2025-01-05  | 2025-01-08 | Rahul Sharma   | North  | Delhi   | Furniture  | P001        | 1200  | 2        | 200    |
| 102       | 2025-01-07  | 2025-01-10 | Priya Singh    | South  | Chennai | Technology | P002        | 2500  | 1        | 500    |
| 103       | 2025-01-08  | 2025-01-12 | Aman Verma     | North  | Lucknow | OfficeSup  | P003        | 800   | 5        | 100    |
| 104       | 2025-01-10  | 2025-01-15 | Neha Gupta     | West   | Mumbai  | Furniture  | P004        | 1500  | 3        | 250    |
| 105       | 2025-01-11  | 2025-01-16 | Suresh Kumar   | East   | Kolkata | Technology | P005        | 3000  | 2        | 600    |


SELECT * 
FROM orders_data 
ORDER BY order_date DESC, profit ASC;


📌 Result Table

👉 First, rows are sorted by order_date descending (latest orders first).
👉 If two rows have the same order_date, then they are sorted by profit ascending.


📌 Functionality of SQL Keywords

SELECT * → Selects all columns.
FROM orders_data → Retrieves data from the table.
ORDER BY order_date DESC, profit ASC
order_date DESC → Sorts rows by latest date first.
profit ASC → If multiple rows share the same order_date, sort them by profit (smallest first).



📌 Execution Order

FROM → Load table.
SELECT → Retrieve all columns.
ORDER BY → Sort rows by order_date DESC, then profit ASC.


✅ This query is super useful when you want to see most recent orders first, and in case of ties, the lowest profit orders appear first.











🔹 SQL Sorting (ORDER BY) – Short Notes

Default Order → Ascending (ASC)
If we just write ORDER BY column, it sorts in ascending order.

Example:

SELECT * FROM Students ORDER BY marks;


→ Lowest marks first.




Multiple Columns Sorting
-------------------------

If we give ORDER BY x, y:

First sorted by x.
If some rows have the same value of x, then sorting is applied on y.

Example:

SELECT * FROM Students ORDER BY class, marks DESC;


→ First sort by class, then within each class sort by marks (highest first).


👉 Super short way to remember:
ORDER BY = first column priority, tie-breaker by next column.














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




const Sorting = () => {
  return (
    <div>Sorting</div>
  )
}

export default Sorting