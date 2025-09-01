import React from 'react'


/*

🔹 SQL Operators


1. Comparison Operators
-----------------------

| Operator     | Meaning               | Example                      | Result                   |
| ------------ | --------------------- | ---------------------------- | ------------------------ |
| `=`          | Equal to              | `WHERE age = 25`             | rows where age = 25      |
| `!=` or `<>` | Not equal to          | `WHERE age <> 25`            | rows where age is not 25 |
| `>`          | Greater than          | `WHERE salary > 50000`       | salary above 50k         |
| `<`          | Less than             | `WHERE age < 30`             | age below 30             |
| `>=`         | Greater than or equal | `WHERE marks >= 50`          | marks 50 and above       |
| `<=`         | Less than or equal    | `WHERE date <= '2023-01-01'` | date up to Jan 1, 2023   |




2. Logical Operators
--------------------

| Operator      | Meaning                     | Example                             |
| ------------- | --------------------------- | ----------------------------------- |
| `AND`         | All conditions must be true | `WHERE age > 20 AND city = 'Delhi'` |
| `OR`          | At least one condition true | `WHERE age < 18 OR city = 'Mumbai'` |
| `NOT`         | Negates a condition         | `WHERE NOT city = 'London'`         |
| `IS NULL`     | Checks for null             | `WHERE phone IS NULL`               |
| `IS NOT NULL` | Checks for not null         | `WHERE email IS NOT NULL`           |





3. Range & Set Operators
------------------------

| Operator              | Meaning               | Example                                    |
| --------------------- | --------------------- | ------------------------------------------ |
| `IN`                  | Matches any in a list | `WHERE dept IN ('HR','IT','Sales')`        |
| `NOT IN`              | Excludes values       | `WHERE dept NOT IN ('HR','IT')`            |
| `BETWEEN … AND …`     | Range inclusive       | `WHERE salary BETWEEN 30000 AND 60000`     |
| `NOT BETWEEN … AND …` | Outside range         | `WHERE salary NOT BETWEEN 10000 AND 20000` |





4. Pattern Matching

| Operator       | Meaning          | Example                          |
| -------------- | ---------------- | -------------------------------- |
| `LIKE 'A%'`    | Starts with A    | `WHERE name LIKE 'A%'` → `Amit`  |
| `LIKE '%A'`    | Ends with A      | `WHERE name LIKE '%a'` → `Megha` |
| `LIKE '%abc%'` | Contains abc     | `WHERE email LIKE '%gmail%'`     |
| `LIKE '_A%'`   | 2nd letter A     | `WHERE code LIKE '_A%'`          |
| `NOT LIKE`     | Excludes pattern | `WHERE name NOT LIKE 'J%'`       |





5. Arithmetic Operators

| Operator       | Example            | Result          |
| -------------- | ------------------ | --------------- |
| `+` (Add)      | `salary + 5000`    | increase salary |
| `-` (Subtract) | `price - discount` | net price       |
| `*` (Multiply) | `marks * 2`        | doubled marks   |
| `/` (Divide)   | `salary / 12`      | monthly salary  |
| `%` (Modulo)   | `id % 2 = 0`       | even numbers    |







6. String Operators (depends on DB)

| Operator                   | Example                            | Result                      |           |   |            |               |
| -------------------------- | ---------------------------------- | --------------------------- | --------- | - | ---------- | ------------- |
| \`                         |                                    | \` (concat in Oracle/PGSQL) | \`'Hello' |   | ' World'\` | `Hello World` |
| `+` (concat in SQL Server) | `'Hi' + ' John'`                   | `Hi John`                   |           |   |            |               |
| `CONCAT()` (MySQL)         | `CONCAT(first_name,' ',last_name)` | `Deepanshu Singh`           |           |   |            |               |






8. Joins (special operators between tables)


| Operator          | Meaning                                   |
| ----------------- | ----------------------------------------- |
| `INNER JOIN`      | Matches records in both tables            |
| `LEFT JOIN`       | All rows from left + matched from right   |
| `RIGHT JOIN`      | All rows from right + matched from left   |
| `FULL OUTER JOIN` | All rows from both (UNION in MySQL)       |
| `CROSS JOIN`      | Cartesian product (every row × every row) |
| `SELF JOIN`       | Join a table to itself                    |














































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








------------------
------ IN --------
------------------


📌 Sample admissions Table (before query)

| patient\_id | attending\_doctor\_id | diagnosis    |
| ----------- | --------------------- | ------------ |
| 101         | 1                     | Fever        |
| 102         | 12                    | Diabetes     |
| 103         | 5                     | Headache     |
| 104         | 19                    | Flu          |
| 105         | 22                    | Asthma       |
| 23          | 7                     | Allergy      |
| 115         | 25                    | Hypertension |


SELECT patient_id, attending_doctor_id, diagnosis 
FROM admissions 
WHERE 
   (
      patient_id % 2 != 0 
      AND attending_doctor_id IN (1, 5, 19)
   )
   OR 
   (
      attending_doctor_id LIKE '%2%' 
      AND LENGTH(patient_id) = 3
   );


📌 Execution Order in SQL

FROM admissions → load table.
WHERE → apply filters:
       Condition 1: Odd patient_id AND doctor_id in (1,5,19).
       Condition 2: doctor_id contains 2 AND patient_id has 3 characters.
SELECT → pick columns patient_id, attending_doctor_id, diagnosis.




📌 Final Output (after query)

| patient\_id | attending\_doctor\_id | diagnosis    |
| ----------- | --------------------- | ------------ |
| 101         | 1                     | Fever        |
| 102         | 12                    | Diabetes     |
| 103         | 5                     | Headache     |
| 115         | 25                    | Hypertension |










--------------------
------ BETWEEN -----
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





















*/









const Operator = () => {
  return (
    <div>Operator</div>
  )
}

export default Operator