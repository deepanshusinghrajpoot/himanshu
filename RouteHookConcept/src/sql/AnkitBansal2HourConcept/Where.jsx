import React from 'react'



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













const Where = () => {
  return (
    <div>Where</div>
  )
}

export default Where