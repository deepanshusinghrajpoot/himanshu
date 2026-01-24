import React from 'react'


/*



*************************
-------------------------
## 5. Aggregate Functions
-------------------------
*************************


📌 Parent Table: orders_data

| order\_id | order\_date | ship\_date | customer\_name | region | city    | category   | product\_id | sales | quantity | profit |
| --------- | ----------- | ---------- | -------------- | ------ | ------- | ---------- | ----------- | ----- | -------- | ------ |
| 101       | 2025-01-05  | 2025-01-08 | Rahul Sharma   | North  | Delhi   | Furniture  | P001        | 1200  | 2        | 200    |
| 102       | 2025-01-07  | 2025-01-10 | Priya Singh    | South  | Chennai | Technology | P002        | 2500  | 1        | 500    |
| 103       | 2025-01-08  | 2025-01-12 | Aman Verma     | North  | Lucknow | OfficeSup  | P003        | 800   | 5        | 100    |
| 104       | 2025-01-10  | 2025-01-15 | Neha Gupta     | West   | Mumbai  | Furniture  | P004        | 1500  | 3        | 250    |
| 105       | 2025-01-11  | 2025-01-16 | Suresh Kumar   | East   | Kolkata | Technology | P005        | 3000  | 2        | 600    |


1️⃣ SUM(): Total Sales
---------------------

SELECT SUM(sales) AS total_sales 
FROM orders_data;


🔹 Execution

SUM(sales) → adds all sales values:
1200 + 2500 + 800 + 1500 + 3000 = 9000


✅ Result

| total\_sales |
| ------------ |
| 9000         |




2️⃣  COUNT(): Total Records
------------------------

SELECT COUNT(*) AS total_records 
FROM orders_data;


🔹 Execution

COUNT(*) → counts all rows in the table → 5


✅ Result

| total\_records |
| -------------- |
| 5              |





3️⃣ AVG(): Average Sales
-----------------------

SELECT SUM(sales)/COUNT(*) AS avg_sales 
FROM orders_data;


🔹 Execution

SUM(sales) = 9000
COUNT(*) = 5
9000 / 5 = 1800


✅ Result

| avg\_sales |
| ---------- |
| 1800       |


⚡ Concept Recap

SUM() → total of numeric column
COUNT(*) → number of rows
AVG() → shortcut for average (SUM/COUNT)



👉 Actually, SQL also has:

SELECT AVG(sales) AS avg_sales 
FROM orders_data;





 4️⃣ MIN() → Minimum value
 -------------------------

 SELECT MIN(profit) AS min_profit FROM orders_data;

 ✅ Result

| min\_profit    |
| -------------- |
| 100            |




 5️⃣ MAX() → Maximum value
 -------------------------

 SELECT MAX(sales) AS max_sales FROM orders_data;

 ✅ Result

| max\_sales     |
| -------------- |
| 3000           |



 6️⃣ GROUP_CONCAT() / STRING_AGG() → Combine string values (MySQL/PostgreSQL)
 ----------------------------------------------------------------------------

 -- MySQL
SELECT GROUP_CONCAT(customer_name) AS customers FROM orders_data;

-- PostgreSQL
SELECT STRING_AGG(customer_name, ', ') AS customers FROM orders_data;


 ✅ Result

| customers                                                                  |
| -------------------------------------------------------------------------- |
| 'Rahul Sharma, Priya Singh, Aman Verma, Neha Gupta, Suresh Kumar'          |




7️⃣ COUNT(DISTINCT column) → Count unique values
------------------------------------------------

SELECT COUNT(DISTINCT category) AS unique_categories FROM orders_data;

Result: 3 (Furniture, Technology, OfficeSup)

 ✅ Result

| unique_categories     |
| --------------------- |
| 3                     |


8. STD() → Use to find stander deviation
------------------------------------------------

SELECT STD(sales) AS stander_daviation_of_sales FROM orders_data;


 ✅ Result

| standard_deviation_of_sales |
| --------------------------- |
| 822.19                      |


9. VARIANCE() → Use to find variance
------------------------------------

SELECT VARIANCE(sales) AS variance_of_sales FROM orders_data;


 ✅ Result

| variance_of_sales |
| ----------------- |
| 676000            |



10. Aggregate with GROUP BY (important)
--------------------------------------

SELECT region, SUM(sales) AS total_sales_per_region
FROM orders_data
GROUP BY region;


Result:

| region | total\_sales\_per\_region |
| ------ | ------------------------- |
| North  | 2000                      |
| South  | 2500                      |
| West   | 1500                      |
| East   | 3000                      |





**************************************
Some more Important Aggregate function
**************************************
-----------
* Distinct:
-----------
***********


📌 Parent Table (orders_data)

| order\_id | order\_date | customer\_name | region | city    | category   | product\_id | sales | quantity | profit |
| --------- | ----------- | -------------- | ------ | ------- | ---------- | ----------- | ----- | -------- | ------ |
| 101       | 2025-01-05  | Rahul Sharma   | North  | Delhi   | Furniture  | P001        | 1200  | 2        | 200    |
| 102       | 2025-01-07  | Priya Singh    | South  | Chennai | Technology | P002        | 2500  | 1        | 500    |
| 103       | 2025-01-08  | Aman Verma     | North  | Lucknow | OfficeSup  | P003        | 800   | 5        | 100    |
| 104       | 2025-01-10  | Neha Gupta     | West   | Mumbai  | Furniture  | P004        | 1500  | 3        | 250    |
| 105       | 2025-01-11  | Suresh Kumar   | East   | Kolkata | Technology | P005        | 3000  | 2        | 600    |


SELECT DISTINCT category, region 
FROM orders_data;


🔎 Execution order

FROM orders_data → take all rows.
SELECT category, region → pick only these two columns.
DISTINCT → remove duplicate combinations of (category, region).


🎯 Result Table

| category   | region |
| ---------- | ------ |
| Furniture  | North  |
| Technology | South  |
| OfficeSup  | North  |
| Furniture  | West   |
| Technology | East   |


⚡ Explanation

DISTINCT applies to the combination of columns listed.
Only unique pairs of category and region are returned.
Duplicate pairs like (Furniture, North) appear only once.





-----------------------------------------------------------
* Group By: Most Important Aggregate Function (VVVVVVV.Imp)
-----------------------------------------------------------

📌 Parent Table (orders_data)

| order\_id | order\_date | customer\_name | region | city    | category   | product\_id | sales | quantity | profit |
| --------- | ----------- | -------------- | ------ | ------- | ---------- | ----------- | ----- | -------- | ------ |
| 101       | 2025-01-05  | Rahul Sharma   | North  | Delhi   | Furniture  | P001        | 1200  | 2        | 200    |
| 102       | 2025-01-07  | Priya Singh    | South  | Chennai | Technology | P002        | 2500  | 1        | 500    |
| 103       | 2025-01-08  | Aman Verma     | North  | Lucknow | OfficeSup  | P003        | 800   | 5        | 100    |
| 104       | 2025-01-10  | Neha Gupta     | West   | Mumbai  | Furniture  | P004        | 1500  | 3        | 250    |
| 105       | 2025-01-11  | Suresh Kumar   | East   | Kolkata | Technology | P005        | 3000  | 2        | 600    |


SELECT category, SUM(sales) AS category_sales, SUM(profit) AS category_profit
FROM orders_data
GROUP BY category;


🔎 Step-by-Step Execution

FROM orders_data → take all rows.
GROUP BY category → group rows by category.
SUM(sales) → total sales per category.
SUM(profit) → total profit per category.
SELECT category, SUM(sales), SUM(profit) → show results per category.


🎯 Result Table

| category   | category\_sales | category\_profit |
| ---------- | --------------- | ---------------- |
| Furniture  | 2700            | 450              |
| Technology | 5500            | 1100             |
| OfficeSup  | 800             | 100              |


⚡ Explanation

GROUP BY category → aggregates rows per category.
SUM(sales) and SUM(profit) are computed within each group.
Each category appears once in the result.






--------------------------
* Having (filter groups):
--------------------------

📌 Parent Table (orders_data)

| order\_id | order\_date | customer\_name | region | city    | category   | product\_id | sales | quantity | profit |
| --------- | ----------- | -------------- | ------ | ------- | ---------- | ----------- | ----- | -------- | ------ |
| 101       | 2025-01-05  | Rahul Sharma   | North  | Delhi   | Furniture  | P001        | 1200  | 2        | 200    |
| 102       | 2025-01-07  | Priya Singh    | South  | Chennai | Technology | P002        | 2500  | 1        | 500    |
| 103       | 2025-01-08  | Aman Verma     | North  | Lucknow | OfficeSup  | P003        | 800   | 5        | 100    |
| 104       | 2025-01-10  | Neha Gupta     | West   | Mumbai  | Furniture  | P004        | 1500  | 3        | 250    |
| 105       | 2025-01-11  | Suresh Kumar   | East   | Kolkata | Technology | P005        | 3000  | 2        | 600    |


SELECT city, SUM(sales) AS city_sales
FROM orders_data
GROUP BY city
HAVING SUM(sales) > 100;


🔎 Step-by-Step Execution

FROM orders_data → take all rows.
GROUP BY city → group rows by city.
SUM(sales) → calculate total sales per city.
HAVING SUM(sales) > 100 → keep only groups where total sales > 100.
SELECT city, SUM(sales) → show result.


     ⚠️ Note: HAVING works after aggregation, unlike WHERE which filters before aggregation.
     ----------------------------------------------------------------------------------------


🎯 Result Table

| city    | city\_sales |
| ------- | ----------- |
| Delhi   | 1200        |
| Chennai | 2500        |
| Lucknow | 800         |
| Mumbai  | 1500        |
| Kolkata | 3000        |


⚡ Explanation

Each city is treated as a group.
SUM(sales) calculates total sales per city.
HAVING filters groups with total sales > 100 → all cities pass in this case.















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








const Aggregation = () => {
  return (
    <div>Aggregation</div>
  )
}

export default Aggregation