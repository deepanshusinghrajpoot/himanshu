/*

📌 Parent Table: orders_data

| order_id | order_date | ship_date  | customer_name | region | city    | category   | product_id | sales | quantity | profit |
| -------- | ---------- | ---------  | ------------- | ------ | ------- | ---------- | ---------- | ----- | -------- | ------ |
| 101      | 2025-01-05 | 2025-01-08 | Rahul Sharma  | North  | Delhi   | Furniture  | P001       | 1200  | 2        | 200    |
| 102      | 2025-01-07 | 2025-01-10 | Priya Singh   | South  | Chennai | Technology | P002       | 2500  | 1        | 500    |
| 103      | 2025-01-08 | 2025-01-12 | Aman Verma    | North  | Lucknow | OfficeSup  | P003       | 800   | 5        | 100    |
| 104      | 2025-01-10 | 2025-01-15 | Neha Gupta    | West   | Mumbai  | Furniture  | P004       | 1500  | 3        | 250    |
| 105      | 2025-01-11 | 2025-01-16 | Suresh Kumar  | East   | Kolkata | Technology | P005       | 3000  | 2        | 600    |



Scalar function
===============


(1). ABS()
-----------

Ques : Find difference from average sales of Technology category
...............................................................

SELECT
ABS(
    sales - (SELECT AVG(sales)
             FROM orders_data
             WHERE category = 'Technology')
) AS diff_between_sales_avgTechnologySales
FROM orders_data
WHERE category = 'Technology';


give result table
.................

| diff_between_sales_avgTechnologySales |
|-------------------------------------  |
| 250                                   |
| 250                                   |




(2). ROUND()
------------

Ques : Round average sales with one decimal place
.................................................

SELECT ROUND(AVG(sales), 1) AS round_avg_sales
FROM orders_data;


give result table
.................

| round_avg_sales |
|-----------------|
| 1800.0          |




(3). FLOOR()
------------

Ques : Find floor value of average sales
........................................

SELECT FLOOR(AVG(sales)) AS floor_avg_sales
FROM orders_data;


give result table
.................

| floor_avg_sales |
|-----------------|
| 1800            |




(4). CEIL()
-----------

Ques : Find ceil value of average sales
......................................

SELECT CEIL(AVG(sales)) AS ceil_avg_sales
FROM orders_data;


give result table
.................

| ceil_avg_sales |
|--------------- |
| 1800           |




*/
