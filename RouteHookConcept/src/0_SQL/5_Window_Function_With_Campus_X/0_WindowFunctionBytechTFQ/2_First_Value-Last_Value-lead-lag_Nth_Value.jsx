/*



✅ Parent Table (product)

Table: product

| product_category | brand      | product_name  | price |
| ---------------- | ---------- | ------------- | ----- |
| Electronics      | Sony       | TV 55 Inch    | 55000 |
| Electronics      | Samsung    | TV 50 Inch    | 45000 |
| Electronics      | LG         | TV 43 Inch    | 35000 |
| Clothing         | Adidas     | Hoodie        | 3500  |
| Clothing         | Nike       | Jacket        | 5000  |
| Clothing         | Puma       | T-Shirt       | 1500  |
| Groceries        | Aashirvaad | Atta 10kg     | 450   |
| Groceries        | Fortune    | Oil 5L        | 700   |
| Groceries        | Surf       | Detergent 4kg | 520   |



FIRST_VALUE()
==============

✔ Definition

lll FIRST_VALUE Window Function returns the first value in a window (partition) based on the ORDER BY clause.
    ORDER BY DESC → highest value
    ORDER BY ASC → lowest value


⭐ Query 1
Display the most expensive product under each category (show the name for every row)

SELECT *,
FIRST_VALUE(product_name) 
     OVER(PARTITION BY product_category ORDER BY price DESC) AS most_exp_product
FROM product;


🔍 Explanation

We partition by product_category → each category becomes a window
ORDER BY price DESC → highest price comes first
FIRST_VALUE takes that product name and prints it in all rows of that category


| product_cat | brand    | product_name  | price | most_exp_product |
| ----------- | -------- | ------------- | ----- | ---------------- |
| Electronics | Sony     | TV 55 Inch    | 55000 | TV 55 Inch       |
| Electronics | Samsung  | TV 50 Inch    | 45000 | TV 55 Inch       |
| Electronics | LG       | TV 43 Inch    | 35000 | TV 55 Inch       |
| Clothing    | Nike     | Jacket        | 5000  | Jacket           |
| Clothing    | Adidas   | Hoodie        | 3500  | Jacket           |
| Clothing    | Puma     | T-Shirt       | 1500  | Jacket           |
| Groceries   | Fortune  | Oil 5L        | 700   | Oil 5L           |
| Groceries   | Surf     | Detergent 4kg | 520   | Oil 5L           |
| Groceries   | Aashirv. | Atta 10kg     | 450   | Oil 5L           |


LAST_VALUE()
=============

✔ Definition

lll LAST_VALUE Window Function returns the last value in a window based on ORDER BY clause.
    But last value window function works only when full frame rows are visible.

    
⚠️ By default SQL uses FRAME:
RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW

This means:
✔ It can see all rows from the start of the partition
❌ But it cannot see rows after the current row

That is why LAST_VALUE often gives the current row value, not the real last value.

❌ Query with wrong result (default frame)


SELECT *,
LAST_VALUE(product_name)
     OVER(PARTITION BY product_category ORDER BY price DESC) AS least_exp_product
FROM product;


❌ Problem

ORDER BY price DESC → highest → lowest
But default frame stops at the current row, so LAST_VALUE becomes:

➡ "value of the current row" (not the lowest priced one!)

✔ Frame Explanation (Interview Level)
Default Frame

RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW

Meaning:

Start → first row of the partition
End → current row only
Future rows are NOT included
So LAST_VALUE cannot look ahead.


✔ Correct frame clause

To allow LAST_VALUE to see ALL rows in partition:

RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING

➡ Now the window can see from start → end
➡ LAST_VALUE correctly picks the lowest priced product


⭐ Correct Query

SELECT *,
LAST_VALUE(product_name) 
    OVER(
        PARTITION BY product_category 
        ORDER BY price DESC
        RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS least_exp_product
FROM product;


✔ Output Table (Correct Least Expensive)

| product_cat | product_name  | price | least_exp_product |
| ----------- | ------------- | ----- | ----------------- |
| Electronics | TV 55 Inch    | 55000 | TV 43 Inch        |
| Electronics | TV 50 Inch    | 45000 | TV 43 Inch        |
| Electronics | TV 43 Inch    | 35000 | TV 43 Inch        |
| Clothing    | Jacket        | 5000  | T-Shirt           |
| Clothing    | Hoodie        | 3500  | T-Shirt           |
| Clothing    | T-Shirt       | 1500  | T-Shirt           |
| Groceries   | Oil 5L        | 700   | Atta 10kg         |
| Groceries   | Detergent 4kg | 520   | Atta 10kg         |
| Groceries   | Atta 10kg     | 450   | Atta 10kg         |


⭐ Additional: RANGE BETWEEN 2 PRECEDING AND 2 FOLLOWING
Meaning (very easy):

Look at 2 rows before current row
Look at 2 rows after current row
Window size = 5 rows max

























🔹 LAG & LEAD Window Functions (SQL)
======================================


🔹 Definition of LAG
--------------------------
LAG() Window Function returns the value from a previous row within the same partition, based on order by clause.

👉 LAG window function Used when you/we want to compare the current row with the previous row.




LAG(column, offset, default) OVER (
    PARTITION BY partition_column
    ORDER BY order_column
)



🔹 LAG / LEAD Arguments (Easy Words)
------------------------------------------
  first_arg:- 👉 Which column’s value you/we want
              (example: salary)

  second_arg:- 👉 How many rows to move
               1 → just previous / next row (default)
               2 → two rows back / ahead

  third_arg :- 👉 What value to show if that row doesn’t exist
               (example: 0, NULL, -1)




🔹 Parent Table: employee

| emp_id | emp_name | dept_name | salary |
| -----: | -------- | --------- | -----: |
|      1 | Amit     | IT        |  50000 |
|      2 | Rohit    | IT        |  55000 |
|      3 | Neha     | IT        |  55000 |
|      4 | Ankit    | HR        |  40000 |
|      5 | Priya    | HR        |  45000 |




🔹 Example 1
Fetch previous employee salary (department-wise)
....................................................

SELECT e.*,
       LAG(salary) OVER (
           PARTITION BY dept_name
           ORDER BY emp_id
       ) AS prev_emp_salary
FROM employee e;


🔹 Output

| emp_id | emp_name | dept_name | salary | prev_emp_salary |
| -----: | -------- | --------- | -----: | --------------: |
|      1 | Amit     | IT        |  50000 |            NULL |
|      2 | Rohit    | IT        |  55000 |           50000 |
|      3 | Neha     | IT        |  55000 |           55000 |
|      4 | Ankit    | HR        |  40000 |            NULL |
|      5 | Priya    | HR        |  45000 |           40000 |





🔹 Example 2
LAG with offset and default value
..........................................

SELECT e.*,
       LAG(salary, 2, 0) OVER (
           PARTITION BY dept_name
           ORDER BY emp_id
       ) AS prev_emp_salary
FROM employee e;

🔹 Output

| emp_id | emp_name | dept_name | salary | prev_emp_salary |
| -----: | -------- | --------- | -----: | --------------: |
|      1 | Amit     | IT        |  50000 |               0 |
|      2 | Rohit    | IT        |  55000 |               0 |
|      3 | Neha     | IT        |  55000 |           50000 |
|      4 | Ankit    | HR        |  40000 |               0 |
|      5 | Priya    | HR        |  45000 |               0 |


🔹 Example 3
Compare salary with previous employee
.........................................

SELECT e.*,
       LAG(salary) OVER(PARTITION BY dept_name ORDER BY emp_id) AS prev_emp_salary,
       CASE
           WHEN salary > LAG(salary) OVER(PARTITION BY dept_name ORDER BY emp_id)
                THEN 'Higher than previous employee'
           WHEN salary = LAG(salary) OVER(PARTITION BY dept_name ORDER BY emp_id)
                THEN 'Same as previous employee salary'
           WHEN salary < LAG(salary) OVER(PARTITION BY dept_name ORDER BY emp_id)
                THEN 'Lower than previous employee salary'
           ELSE 'Previous employee not exist'
       END AS salary_comparison
FROM employee e;

🔹 Output

| emp_id | emp_name | dept_name | salary | prev_emp_salary | salary_comparison                |
| -----: | -------- | --------- | -----: | --------------: | -------------------------------- |
|      1 | Amit     | IT        |  50000 |            NULL | Previous employee not exist      |
|      2 | Rohit    | IT        |  55000 |           50000 | Higher than previous employee    |
|      3 | Neha     | IT        |  55000 |           55000 | Same as previous employee salary |
|      4 | Ankit    | HR        |  40000 |            NULL | Previous employee not exist      |
|      5 | Priya    | HR        |  45000 |           40000 | Higher than previous employee    |















🔹 Definition of LEAD
------------------------

lll LEAD() Window Function returns the value from the next row within the same partition based on oder by clause.

👉LEAD window function Used when you want to compare the current row with the next row.


LEAD(column, offset, default) OVER (
    PARTITION BY partition_column
    ORDER BY order_column
)







🔹 Parent Table: employee

| emp_id | emp_name | dept_name | salary |
| -----: | -------- | --------- | -----: |
|      1 | Amit     | IT        |  50000 |
|      2 | Rohit    | IT        |  55000 |
|      3 | Neha     | IT        |  55000 |
|      4 | Ankit    | HR        |  40000 |
|      5 | Priya    | HR        |  45000 |





🔹 Example 4
Fetch next employee salary (department-wise)
-----------------------------------------------

SELECT e.*,
       LEAD(salary) OVER (
           PARTITION BY dept_name
           ORDER BY emp_id
       ) AS next_emp_salary
FROM employee e;

output

| emp_id | emp_name | dept_name | salary | next_emp_salary |
| -----: | -------- | --------- | -----: | --------------: |
|      1 | Amit     | IT        |  50000 |           55000 |
|      2 | Rohit    | IT        |  55000 |           55000 |
|      3 | Neha     | IT        |  55000 |            NULL |
|      4 | Ankit    | HR        |  40000 |           45000 |
|      5 | Priya    | HR        |  45000 |            NULL |



🔹 Example 5
Compare salary with next employee
.....................................

SELECT e.*,
       LEAD(salary) OVER(PARTITION BY dept_name ORDER BY emp_id) AS next_emp_salary,
       CASE
           WHEN salary > LEAD(salary) OVER(PARTITION BY dept_name ORDER BY emp_id)
                THEN 'Higher than next employee'
           WHEN salary = LEAD(salary) OVER(PARTITION BY dept_name ORDER BY emp_id)
                THEN 'Same as next employee salary'
           WHEN salary < LEAD(salary) OVER(PARTITION BY dept_name ORDER BY emp_id)
                THEN 'Lower than next employee salary'
           ELSE 'Next employee not exist'
       END AS salary_comparison
FROM employee e;


output

| emp_id | emp_name | dept_name | salary | next_emp_salary | salary_comparison            |
| -----: | -------- | --------- | -----: | --------------: | ---------------------------- |
|      1 | Amit     | IT        |  50000 |           55000 | Lower than next employee     |
|      2 | Rohit    | IT        |  55000 |           55000 | Same as next employee salary |
|      3 | Neha     | IT        |  55000 |            NULL | Next employee not exist      |
|      4 | Ankit    | HR        |  40000 |           45000 | Lower than next employee     |
|      5 | Priya    | HR        |  45000 |            NULL | Next employee not exist      |









⭐ 3️⃣ NTH_VALUE()
======================

✔ Definition (Easy to Understand)

lll NTH_VALUE(col, n) Window Function → returns the nth value from the ordered window.
    But NTH_VALUE window function works only when full frame rows are visible.
 

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






------------------------------------------------------------------------------------------------------------

+------------+-------------------+----------+-------+
| product_id | product_name      | category | price |
+------------+-------------------+----------+-------+
| 1          | iPhone 15         | Mobile   | 80000 |
| 2          | Samsung S23       | Mobile   | 75000 |
| 3          | OnePlus 11        | Mobile   | 70000 |
| 4          | MacBook Air       | Laptop   | 120000|
| 5          | Dell XPS          | Laptop   | 110000|
| 6          | HP Pavilion       | Laptop   | 90000 |
+------------+-------------------+----------+-------+




SELECT 
    product_id,
    product_name,
    category,
    price,
    NTH_VALUE(product_name, 2) 
        OVER (
            PARTITION BY category
            ORDER BY price DESC
            RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
        ) AS second_most_exp_product
FROM product;




+------------+-------------------+----------+-------+--------------------------+
| product_id | product_name      | category | price | second_most_exp_product |
+------------+-------------------+----------+-------+--------------------------+
| 1          | iPhone 15         | Mobile   | 80000 | Samsung S23             |
| 2          | Samsung S23       | Mobile   | 75000 | Samsung S23             |
| 3          | OnePlus 11        | Mobile   | 70000 | Samsung S23             |
| 4          | MacBook Air       | Laptop   |120000 | Dell XPS                |
| 5          | Dell XPS          | Laptop   |110000 | Dell XPS                |
| 6          | HP Pavilion       | Laptop   | 90000 | Dell XPS                |
+------------+-------------------+----------+-------+--------------------------+




















*/
