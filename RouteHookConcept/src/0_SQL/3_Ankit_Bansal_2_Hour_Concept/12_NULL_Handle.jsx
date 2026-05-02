/*




-- ===============================
-- IFNULL() Function (MySQL)
-- ===============================

-- 🔹 Role:
-- Replaces NULL with a specified value

-- 🔹 Syntax:
-- IFNULL(expression, replacement_value)


-- --------------------------------
-- Basic Examples
-- --------------------------------

SELECT IFNULL(NULL, 0) AS result;
-- Output: 0

SELECT IFNULL(100, 0) AS result;
-- Output: 100


-- --------------------------------
-- Replace NULL Values in Table
-- --------------------------------

SELECT IFNULL(prd_cost, 0) AS prd_cost
FROM products;
-- If prd_cost is NULL → returns 0


-- --------------------------------
-- Real Use Case (Calculations)
-- --------------------------------

SELECT 
    product_name,
    price,
    IFNULL(discount, 0) AS discount,
    price - IFNULL(discount, 0) AS final_price
FROM products;


-- --------------------------------
-- With String Data
-- --------------------------------

SELECT IFNULL(customer_name, 'Unknown') AS customer_name
FROM customers;





-- ===============================
-- COALESCE() Function
-- ===============================

-- 🔹 Role:
-- Returns the FIRST non-NULL value from a list

-- 🔹 Syntax:
-- COALESCE(value1, value2, value3, ...)


-- --------------------------------
-- Basic Examples
-- --------------------------------

SELECT COALESCE(NULL, NULL, 10, 20) AS result;
-- Output: 10

SELECT COALESCE(NULL, 'Hello', 'World') AS result;
-- Output: 'Hello'


-- --------------------------------
-- Replace NULL Values
-- --------------------------------

SELECT COALESCE(prd_cost, 0) AS prd_cost
FROM products;
-- If prd_cost is NULL → returns 0


-- --------------------------------
-- Real Use Case (ETL / Reporting)
-- --------------------------------

SELECT 
    product_name,
    COALESCE(discount, 0) AS discount,
    price - COALESCE(discount, 0) AS final_price
FROM products;


-- --------------------------------
-- Multiple Column Fallback
-- --------------------------------

SELECT 
    COALESCE(email, phone, 'No Contact') AS contact_info
FROM customers;
-- Picks first available contact


-- --------------------------------
-- With NULLIF (Power Combo)
-- --------------------------------

SELECT 
    COALESCE(NULLIF(prd_cost, 0), 100) AS prd_cost
FROM products;
-- If prd_cost = 0 → NULL → replaced by 100





-- ===============================
-- CAST() Function
-- ===============================

-- 🔹 Role:
-- Converts a value from one data type to another

-- 🔹 Syntax:
-- CAST(expression AS datatype)

-- 🔹 Example:
SELECT CAST('123' AS INT) AS result;
-- Output: 123 (string → integer)

SELECT CAST(123.45 AS INT) AS result;
-- Output: 123 (decimal → integer)


-- 🔹 Real Use Case (ETL / Data Cleaning):
SELECT 
    CAST(order_date AS DATE) AS clean_date
FROM orders;







-- ===============================
-- NULLIF() Function
-- ===============================

-- 🔹 Role:
-- Compares two expressions.
-- If they are equal → returns NULL
-- If not equal → returns first value

-- 🔹 Syntax:
-- NULLIF(value1, value2)


-- --------------------------------
-- Basic Examples
-- --------------------------------

SELECT NULLIF(100, 100) AS result;
-- Output: NULL

SELECT NULLIF(100, 0) AS result;
-- Output: 100


-- --------------------------------
-- Real Use Case (Avoid Division Error)
-- --------------------------------

SELECT 100 / NULLIF(0, 0) AS result;
-- Output: NULL (instead of divide by zero error)


-- --------------------------------
-- Data Cleaning Example
-- --------------------------------
-- Convert unwanted values (like 0 or empty) into NULL

SELECT NULLIF(prd_cost, 0) AS prd_cost
FROM products;


-- --------------------------------
-- With TRIM (ETL Scenario)
-- --------------------------------
-- Convert empty string to NULL

SELECT NULLIF(TRIM(cst_name), '') AS clean_name
FROM customers;






-- --------------------------------
-- How REPLACE() Works in SQL
-- --------------------------------

REPLACE(column, 'old_value', 'new_value')

It finds old_value and replaces it with new_value






*/