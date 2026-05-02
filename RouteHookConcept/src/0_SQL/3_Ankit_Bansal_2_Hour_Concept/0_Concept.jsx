import React from 'react'


/*



🔹 SQL Syntax Order (Query Writing Order)
============================================

Correct Order:

SELECT – choose columns or expressions from source table
DISTINCT – remove duplicate rows from source 
FROM – specify source table(s)
JOIN / ON – combine tables using conditions
WHERE – filter rows before gouping
GROUP BY – group rows of the source table
HAVING – filter row after gouping
ORDER BY – sort the final result.
LIMIT / TOP / OFFSET – restrict number of rows


lll ==================================== VVV.Imp =======================================================

SELECT  column...,
        WINDOW_FUNCTION_NAME OVER w AS xyz
FROM    ................
JOIN    ................
        ON ..................
WHERE   .................
GROUP BY ................
HAVING ..................
WINDOW  w AS (
                  PARTITION BY ....  
                  ORDER BY ....  
                  full-frame-use 
              )
ORDER BY ..............
LIMIT / TOP / OFFSET 

==============================================================================================






=================================== VVV.Imp ==================================================

🔹 SQL Logical Execution Order(How DB Executes)

Correct Order:

FROM – specify the source table(s).
JOIN / ON – apply joins between tables.
lll WHERE – filter rows (before grouping).
GROUP BY – group the filtered rows.
lll HAVING – filter groups (after grouping).
WINDOW FUNCTION
SELECT – choose the columns/expressions.
DISTINCT – remove duplicates from result set.
Aggregate Functions – SUM(), COUNT(), MIN(), MAX(), AVG(), GROUP_CONCAT() are applied here (inside SELECT).
ORDER BY – sort the final result.
LIMIT / TOP / OFFSET – return only required rows.


============================================================================================================



*/



/*




***********************
-----------------------
## 1. Select keyword 
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




*/




/*



****************************
----------------------------
## 4. Filtering Data (WHERE)
----------------------------
****************************




* Filter by region:
-------------------

📌 Parent Table: orders_data

| order\_id | order\_date | ship\_date | customer\_name | region  | city    | category   | product\_id | sales | quantity | profit |
| --------- | ----------- | ---------- | -------------- | ------- | ------- | ---------- | ----------- | ----- | -------- | ------ |
| 101       | 2025-01-05  | 2025-01-08 | Rahul Sharma   | North   | Delhi   | Furniture  | P001        | 1200  | 2        | 200    |
| 102       | 2025-01-07  | 2025-01-10 | Priya Singh    | South   | Chennai | Technology | P002        | 2500  | 1        | 500    |
| 103       | 2025-01-08  | 2025-01-12 | Aman Verma     | North   | Lucknow | OfficeSup  | P003        | 800   | 5        | 100    |
| 104       | 2025-01-10  | 2025-01-15 | Neha Gupta     | West    | Mumbai  | Furniture  | P004        | 1500  | 3        | 250    |
| 105       | 2025-01-11  | 2025-01-16 | Suresh Kumar   | East    | Kolkata | Technology | P005        | 3000  | 2        | 600    |
| 106       | 2025-01-12  | 2025-01-17 | Ankit Mehra    | Central | Bhopal  | Furniture  | P006        | 2000  | 4        | 300    |
| 107       | 2025-01-13  | 2025-01-18 | Riya Patel     | Central | Indore  | Technology | P007        | 1800  | 2        | 150    |


SELECT * 
FROM orders_data 
WHERE region = 'Central';


📌 Result Table

| order\_id | order\_date | ship\_date | customer\_name | region  | city   | category   | product\_id | sales | quantity | profit |
| --------- | ----------- | ---------- | -------------- | ------- | ------ | ---------- | ----------- | ----- | -------- | ------ |
| 106       | 2025-01-12  | 2025-01-17 | Ankit Mehra    | Central | Bhopal | Furniture  | P006        | 2000  | 4        | 300    |
| 107       | 2025-01-13  | 2025-01-18 | Riya Patel     | Central | Indore | Technology | P007        | 1800  | 2        | 150    |


📌 Functionality of SQL Keywords

WHERE region = 'Central' → Filters only rows where region is Central.
SELECT * → Returns all columns for those rows.
FROM orders_data → Data is taken from orders_data table.



📌 Execution Order

FROM → Load orders_data.
WHERE → Keep only rows where region = 'Central'.
SELECT → Return all columns.


✅ Now it works with real results.





* Filter by date:
-----------------

📌 Parent Table (orders_data – sample)

| order\_id | order\_date | ship\_date | customer\_name | region  | city    | category   | product\_id | sales | quantity | profit |
| --------- | ----------- | ---------- | -------------- | ------- | ------- | ---------- | ----------- | ----- | -------- | ------ |
| 101       | 2025-01-05  | 2025-01-08 | Rahul Sharma   | North   | Delhi   | Furniture  | P001        | 1200  | 2        | 200    |
| 102       | 2025-01-07  | 2025-01-10 | Priya Singh    | South   | Chennai | Technology | P002        | 2500  | 1        | 500    |
| 103       | 2025-01-08  | 2025-01-12 | Aman Verma     | North   | Lucknow | OfficeSup  | P003        | 800   | 5        | 100    |
| 104       | 2025-01-10  | 2025-01-15 | Neha Gupta     | West    | Mumbai  | Furniture  | P004        | 1500  | 3        | 250    |
| 105       | 2025-01-11  | 2025-01-16 | Suresh Kumar   | East    | Kolkata | Technology | P005        | 3000  | 2        | 600    |
| 106       | 2025-01-12  | 2025-01-17 | Ankit Mehra    | Central | Bhopal  | Furniture  | P006        | 2000  | 4        | 300    |
| 107       | 2025-01-13  | 2025-01-18 | Riya Patel     | Central | Indore  | Technology | P007        | 1800  | 2        | 150    |


SELECT * 
FROM orders_data 
WHERE order_date > '2025-01-10'
ORDER BY order_date;


📌 Result Table (after applying WHERE and ORDER BY)

👉 Since all order_date values are after 2019-09-17, the condition includes all rows.
Then rows are sorted ascending by order_date:

| order\_id | order\_date | ship\_date | customer\_name | region  | city    | category   | product\_id | sales | quantity | profit |
| --------- | ----------- | ---------- | -------------- | ------- | ------- | ---------- | ----------- | ----- | -------- | ------ |
| 105       | 2025-01-11  | 2025-01-16 | Suresh Kumar   | East    | Kolkata | Technology | P005        | 3000  | 2        | 600    |
| 106       | 2025-01-12  | 2025-01-17 | Ankit Mehra    | Central | Bhopal  | Furniture  | P006        | 2000  | 4        | 300    |
| 107       | 2025-01-13  | 2025-01-18 | Riya Patel     | Central | Indore  | Technology | P007        | 1800  | 2        | 150    |



📌 Functionality of SQL Keywords

WHERE order_date > '2019-09-17' → Filters rows where order_date is greater than 2019-09-17.
ORDER BY order_date → Sorts the result set in ascending order by order_date.
SELECT * → Returns all columns.
FROM orders_data → Data source table.



📌 Execution Order

FROM → Take data from orders_data.
WHERE → Keep rows with order_date > '2019-09-17'.
SELECT → Pick all columns.
ORDER BY → Sort rows by order_date.




**********************************************************************
* Operators: `AND`, `OR`, `NOT` or `IS NOT`, `IN`, `BETWEEN`, `LIKE`
**********************************************************************

📌 Updated Parent Table (orders_data)

| order\_id | order\_date | customer\_name | region  | city    | category   | sales | quantity | profit |
| --------- | ----------- | -------------- | ------- | ------- | ---------- | ----- | -------- | ------ |
| 201       | 2025-02-01  | Rahul Sharma   | North   | Delhi   | Furniture  | 1200  | 2        | 200    |
| 202       | 2025-02-02  | Priya Singh    | South   | Chennai | Technology | 2500  | 4        | 500    |
| 203       | 2025-02-03  | Aman Verma     | North   | Lucknow | OfficeSup  | 800   | 5        | 100    |
| 204       | 2025-02-04  | Neha Gupta     | West    | Mumbai  | Furniture  | 1500  | 3        | 250    |
| 205       | 2025-02-05  | Suresh Kumar   | East    | Kolkata | Technology | 3000  | 6        | 600    |
| 206       | 2025-02-06  | Ankit Mehra    | Central | Bhopal  | Furniture  | 2000  | 2        | 300    |
| 207       | 2025-02-07  | Riya Patel     | Central | Indore  | Technology | 1800  | 5        | 150    |
| 208       | 2025-02-08  | Karan Yadav    | Central | Gwalior | Technology | 2200  | 7        | 350    |


-----------
--- AND ---
-----------

SELECT * 
FROM orders_data 
WHERE quantity > 3 AND category = 'Technology' AND region = 'Central';



🔎 Step-by-Step Execution

FROM orders_data → take all rows.
WHERE → apply filters:
          quantity > 3
          category = 'Technology'
          region = 'Central'
          👉 All 3 conditions must be true (AND).

SELECT* → return matching rows.


🎯 Result Table

| order\_id | order\_date | customer\_name | region  | city    | category   | sales | quantity | profit |
| --------- | ----------- | -------------- | ------- | ------- | ---------- | ----- | -------- | ------ |
| 207       | 2025-02-07  | Riya Patel     | Central | Indore  | Technology | 1800  | 5        | 150    |
| 208       | 2025-02-08  | Karan Yadav    | Central | Gwalior | Technology | 2200  | 7        | 350    |





----------
--- OR ---
----------


📌 Parent Table (Reminder)

| order\_id | order\_date | customer\_name | region  | city    | category   | sales | quantity | profit |
| --------- | ----------- | -------------- | ------- | ------- | ---------- | ----- | -------- | ------ |
| 201       | 2025-02-01  | Rahul Sharma   | North   | Delhi   | Furniture  | 1200  | 2        | 200    |
| 202       | 2025-02-02  | Priya Singh    | South   | Chennai | Technology | 2500  | 4        | 500    |
| 203       | 2025-02-03  | Aman Verma     | North   | Lucknow | OfficeSup  | 800   | 5        | 100    |
| 204       | 2025-02-04  | Neha Gupta     | West    | Mumbai  | Furniture  | 1500  | 3        | 250    |
| 205       | 2025-02-05  | Suresh Kumar   | East    | Kolkata | Technology | 3000  | 6        | 600    |
| 206       | 2025-02-06  | Ankit Mehra    | Central | Bhopal  | Furniture  | 2000  | 2        | 300    |
| 207       | 2025-02-07  | Riya Patel     | Central | Indore  | Technology | 1800  | 5        | 150    |
| 208       | 2025-02-08  | Karan Yadav    | Central | Gwalior | Technology | 2200  | 7        | 350    |


SELECT * 
FROM orders_data 
WHERE quantity > 3 OR category = 'Technology' OR region = 'Central';


🔎 Step-by-Step Execution

FROM orders_data → start with all rows.
WHERE → apply conditions:
        quantity > 3
        OR category = 'Technology'
        OR region = 'Central'
        👉 At least one condition must be true.

SELECT* → return matching rows.


🎯 Result Table

| order\_id | order\_date | customer\_name | region  | city    | category   | sales | quantity | profit |
| --------- | ----------- | -------------- | ------- | ------- | ---------- | ----- | -------- | ------ |
| 202       | 2025-02-02  | Priya Singh    | South   | Chennai | Technology | 2500  | 4        | 500    |
| 203       | 2025-02-03  | Aman Verma     | North   | Lucknow | OfficeSup  | 800   | 5        | 100    |
| 205       | 2025-02-05  | Suresh Kumar   | East    | Kolkata | Technology | 3000  | 6        | 600    |
| 206       | 2025-02-06  | Ankit Mehra    | Central | Bhopal  | Furniture  | 2000  | 2        | 300    |
| 207       | 2025-02-07  | Riya Patel     | Central | Indore  | Technology | 1800  | 5        | 150    |
| 208       | 2025-02-08  | Karan Yadav    | Central | Gwalior | Technology | 2200  | 7        | 350    |




--------------------
--- IN / BETWEEN ---
--------------------

📌 Parent Table (Reminder)

| order\_id | order\_date | customer\_name | region  | city    | category   | sales | quantity | profit |
| --------- | ----------- | -------------- | ------- | ------- | ---------- | ----- | -------- | ------ |
| 201       | 2025-02-01  | Rahul Sharma   | North   | Delhi   | Furniture  | 1200  | 2        | 200    |
| 202       | 2025-02-02  | Priya Singh    | South   | Chennai | Technology | 2500  | 4        | 500    |
| 203       | 2025-02-03  | Aman Verma     | North   | Lucknow | OfficeSup  | 800   | 5        | 100    |
| 204       | 2025-02-04  | Neha Gupta     | West    | Mumbai  | Furniture  | 1500  | 3        | 250    |
| 205       | 2025-02-05  | Suresh Kumar   | East    | Kolkata | Technology | 3000  | 6        | 600    |
| 206       | 2025-02-06  | Ankit Mehra    | Central | Bhopal  | Furniture  | 2000  | 2        | 300    |
| 207       | 2025-02-07  | Riya Patel     | Central | Indore  | Technology | 1800  | 5        | 150    |
| 208       | 2025-02-08  | Karan Yadav    | Central | Gwalior | Technology | 2200  | 7        | 350    |


SELECT * 
FROM orders_data 
WHERE quantity BETWEEN 3 AND 5;

🔎 Step-by-Step

BETWEEN 3 AND 5 includes both ends (3, 4, and 5).
Filter rows where quantity = 3, 4, or 5.


🎯 Result Table

| order\_id | order\_date | customer\_name | region  | city    | category   | sales | quantity | profit |
| --------- | ----------- | -------------- | ------- | ------- | ---------- | ----- | -------- | ------ |
| 202       | 2025-02-02  | Priya Singh    | South   | Chennai | Technology | 2500  | 4        | 500    |
| 203       | 2025-02-03  | Aman Verma     | North   | Lucknow | OfficeSup  | 800   | 5        | 100    |
| 204       | 2025-02-04  | Neha Gupta     | West    | Mumbai  | Furniture  | 1500  | 3        | 250    |
| 207       | 2025-02-07  | Riya Patel     | Central | Indore  | Technology | 1800  | 5        | 150    |




----------------------------
* Pattern Matching (`LIKE`):
----------------------------

-- '%A' → ends with A
-- '%A%' → contains A
-- '_A%' → 2nd character is A
-- '_[ae]%' → 2nd character is a or e



📌 Parent Table (Reminder)

| order\_id | order\_date | customer\_name | region  | city    | category   | sales | quantity | profit |
| --------- | ----------- | -------------- | ------- | ------- | ---------- | ----- | -------- | ------ |
| 201       | 2025-02-01  | Rahul Sharma   | North   | Delhi   | Furniture  | 1200  | 2        | 200    |
| 202       | 2025-02-02  | Priya Singh    | South   | Chennai | Technology | 2500  | 4        | 500    |
| 203       | 2025-02-03  | Aman Verma     | North   | Lucknow | OfficeSup  | 800   | 5        | 100    |
| 204       | 2025-02-04  | Neha Gupta     | West    | Mumbai  | Furniture  | 1500  | 3        | 250    |
| 205       | 2025-02-05  | Suresh Kumar   | East    | Kolkata | Technology | 3000  | 6        | 600    |
| 206       | 2025-02-06  | Ankit Mehra    | Central | Bhopal  | Furniture  | 2000  | 2        | 300    |
| 207       | 2025-02-07  | Riya Patel     | Central | Indore  | Technology | 1800  | 5        | 150    |
| 208       | 2025-02-08  | Karan Yadav    | Central | Gwalior | Technology | 2200  | 7        | 350    |

SELECT * 
FROM orders_data
WHERE customer_name LIKE 'A%';


🔎 Step-by-Step
LIKE 'A%' → find names starting with A.
% means “any characters after A.”


🎯 Result Table
| order\_id | order\_date | customer\_name | region  | city    | category  | sales | quantity | profit |
| --------- | ----------- | -------------- | ------- | ------- | --------- | ----- | -------- | ------ |
| 203       | 2025-02-03  | Aman Verma     | North   | Lucknow | OfficeSup | 800   | 5        | 100    |
| 206       | 2025-02-06  | Ankit Mehra    | Central | Bhopal  | Furniture | 2000  | 2        | 300    |








⚡ Execution Order:

Engine executes in logical order (FROM → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT).

We write in SQL syntax order (SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT).











*/








const Concept = () => {
  return (
    <div>Concept</div>
  )
}

export default Concept