import React from 'react'


/*




***********************
-----------------------
## 1. Select Statements
-----------------------
***********************


📌 Parent Table: orders_data

| order\_id | order\_date | ship\_date | customer\_name | region | city    | category   | product\_id | sales | quantity | profit |
| --------- | ----------- | ---------- | -------------- | ------ | ------- | ---------- | ----------- | ----- | -------- | ------ |
| 101       | 2025-01-05  | 2025-01-08 | Rahul Sharma   | North  | Delhi   | Furniture  | P001        | 1200  | 2        | 200    |
| 102       | 2025-01-07  | 2025-01-10 | Priya Singh    | South  | Chennai | Technology | P002        | 2500  | 1        | 500    |
| 103       | 2025-01-08  | 2025-01-12 | Aman Verma     | North  | Lucknow | OfficeSup  | P003        | 800   | 5        | 100    |
| 104       | 2025-01-10  | 2025-01-15 | Neha Gupta     | West   | Mumbai  | Furniture  | P004        | 1500  | 3        | 250    |
| 105       | 2025-01-11  | 2025-01-16 | Suresh Kumar   | East   | Kolkata | Technology | P005        | 3000  | 2        | 600    |


SELECT * 
FROM orders_data;


📌 Result Table
👉 This will return all the columns and all the rows from the table:


| order\_id | order\_date | ship\_date | customer\_name | region | city    | category   | product\_id | sales | quantity | profit |
| --------- | ----------- | ---------- | -------------- | ------ | ------- | ---------- | ----------- | ----- | -------- | ------ |
| 101       | 2025-01-05  | 2025-01-08 | Rahul Sharma   | North  | Delhi   | Furniture  | P001        | 1200  | 2        | 200    |
| 102       | 2025-01-07  | 2025-01-10 | Priya Singh    | South  | Chennai | Technology | P002        | 2500  | 1        | 500    |
| 103       | 2025-01-08  | 2025-01-12 | Aman Verma     | North  | Lucknow | OfficeSup  | P003        | 800   | 5        | 100    |
| 104       | 2025-01-10  | 2025-01-15 | Neha Gupta     | West   | Mumbai  | Furniture  | P004        | 1500  | 3        | 250    |
| 105       | 2025-01-11  | 2025-01-16 | Suresh Kumar   | East   | Kolkata | Technology | P005        | 3000  | 2        | 600    |



📌 Functionality of SQL Keywords

SELECT → Chooses which columns to display. * means all columns.
FROM → Tells SQL which table to fetch data from (orders_data).



📌 Execution Order

FROM → Load table orders_data.
SELECT → Return all columns (*).


✅ So this query simply retrieves the entire table without any filtering.








* Select specific columns:
--------------------------



📌 Parent Table: orders_data

| order\_id | order\_date | ship\_date | customer\_name | region | city    | category   | product\_id | sales | quantity | profit |
| --------- | ----------- | ---------- | -------------- | ------ | ------- | ---------- | ----------- | ----- | -------- | ------ |
| 101       | 2025-01-05  | 2025-01-08 | Rahul Sharma   | North  | Delhi   | Furniture  | P001        | 1200  | 2        | 200    |
| 102       | 2025-01-07  | 2025-01-10 | Priya Singh    | South  | Chennai | Technology | P002        | 2500  | 1        | 500    |
| 103       | 2025-01-08  | 2025-01-12 | Aman Verma     | North  | Lucknow | OfficeSup  | P003        | 800   | 5        | 100    |
| 104       | 2025-01-10  | 2025-01-15 | Neha Gupta     | West   | Mumbai  | Furniture  | P004        | 1500  | 3        | 250    |
| 105       | 2025-01-11  | 2025-01-16 | Suresh Kumar   | East   | Kolkata | Technology | P005        | 3000  | 2        | 600    |


SELECT order_id, order_date, sales, profit 
FROM orders_data;


📌 Result Table

👉 Only the selected columns are shown:

| order\_id | order\_date | sales | profit |
| --------- | ----------- | ----- | ------ |
| 101       | 2025-01-05  | 1200  | 200    |
| 102       | 2025-01-07  | 2500  | 500    |
| 103       | 2025-01-08  | 800   | 100    |
| 104       | 2025-01-10  | 1500  | 250    |
| 105       | 2025-01-11  | 3000  | 600    |


📌 Functionality of SQL Keywords

SELECT order_id, order_date, sales, profit → Only these columns are displayed in the result.
FROM orders_data → Data is fetched from table orders_data.



📌 Execution Order

FROM → Load the table orders_data.
SELECT → Pick only required columns: order_id, order_date, sales, profit.



✅ This query is useful when you don’t need all columns — just the required ones for analysis.








* Select top rows:
------------------


📌 Parent Table: orders_data

| order\_id | order\_date | ship\_date | customer\_name | region | city    | category   | product\_id | sales | quantity | profit |
| --------- | ----------- | ---------- | -------------- | ------ | ------- | ---------- | ----------- | ----- | -------- | ------ |
| 101       | 2025-01-05  | 2025-01-08 | Rahul Sharma   | North  | Delhi   | Furniture  | P001        | 1200  | 2        | 200    |
| 102       | 2025-01-07  | 2025-01-10 | Priya Singh    | South  | Chennai | Technology | P002        | 2500  | 1        | 500    |
| 103       | 2025-01-08  | 2025-01-12 | Aman Verma     | North  | Lucknow | OfficeSup  | P003        | 800   | 5        | 100    |
| 104       | 2025-01-10  | 2025-01-15 | Neha Gupta     | West   | Mumbai  | Furniture  | P004        | 1500  | 3        | 250    |
| 105       | 2025-01-11  | 2025-01-16 | Suresh Kumar   | East   | Kolkata | Technology | P005        | 3000  | 2        | 600    |


SELECT TOP 10 order_id, order_date, sales, profit 
FROM orders_data;


SELECT order_id, order_date, sales, profit 
FROM orders_data 
LIMIT 10;



📌 Result Table (since we only have 5 rows, it will show all 5)

| order\_id | order\_date | sales | profit |
| --------- | ----------- | ----- | ------ |
| 101       | 2025-01-05  | 1200  | 200    |
| 102       | 2025-01-07  | 2500  | 500    |
| 103       | 2025-01-08  | 800   | 100    |
| 104       | 2025-01-10  | 1500  | 250    |
| 105       | 2025-01-11  | 3000  | 600    |


📌 Functionality of SQL Keywords

SELECT order_id, order_date, sales, profit → Pick specific columns.
FROM orders_data → Source table.
TOP 10 (SQL Server) → Return only the first 10 rows.
LIMIT 10 (MySQL/PostgreSQL) → Same functionality, returns first 10 rows.


📌 Execution Order

FROM → Load table.
SELECT → Pick columns.
ORDER BY (if used).
TOP / LIMIT → Return only first n rows.

✅ This query is useful when you don’t want the full dataset, just a sample (like top 10 orders).

---













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

















const Select = () => {
  return (
    <div>Select</div>
  )
}

export default Select