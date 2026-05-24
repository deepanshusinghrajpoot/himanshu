



'''



/*
====================================================
 MySQL SET Operators – Correct Notes
====================================================
*/

-- lll🔹 Basic Concept
--        JOIN Operator  → Combine Columns
--        SET Operator  → Combine Rows (Result Sets)


/* ------------------------------------------------
    lll 🔹 Types of SET Operators in MySQL
------------------------------------------------ */
--         1. UNION
--         2. UNION ALL

-- ❌ NOT supported in MySQL:
-- EXCEPT (use NOT EXISTS / LEFT JOIN)
-- INTERSECT (use INNER JOIN)


/* ------------------------------------------------
🔹 SYNTAX
------------------------------------------------ */

SELECT col1, col2 FROM table1
UNION / UNION ALL
SELECT col1, col2 FROM table2;


/* ------------------------------------------------
 🔹 RULES (Very Important)
------------------------------------------------ */

lll First,  :-  both queries must have the same structure — meaning same number of columns, 
                same data types, and same order.

Second, :-  the final output is controlled by the first query — so column names come from the first query, 
            and ORDER BY is applied only once at the end.”


/* ------------------------------------------------
    lll🔹 UNION set operator
---------------------------------------------- */
-     Returns all district rows from both queries.
      and
-     Removes duplicate rows from the result.

SELECT name FROM employees
UNION
SELECT name FROM customers;



/* ------------------------------------------------
   lll🔹 UNION ALL set operator
------------------------------------------------ */
-         Returns all rows from both queries, including duplicates.


SELECT name FROM employees
UNION ALL
SELECT name FROM customers;


/* ------------------------------------------------
🔹 UNION vs UNION ALL
------------------------------------------------ */
- UNION ALL is generally faster than UNION
- If we are confident there are no duplicate, use UNION ALL



/* ------------------------------------------------
🔹 EXCEPT (MySQL Alternative)
------------------------------------------------ */

-- Goal: Rows in first table NOT in second

SELECT e.name
FROM employees e
LEFT JOIN customers c 
ON e.name = c.name
WHERE c.name IS NULL;

-- OR

SELECT name 
FROM employees e
WHERE NOT EXISTS (
    SELECT 1 
    FROM customers c 
    WHERE c.name = e.name
);


/* ------------------------------------------------
🔹 INTERSECT (MySQL Alternative)
------------------------------------------------ */

-- Goal: Common rows in both tables

SELECT e.name
FROM employees e
INNER JOIN customers c 
ON e.name = c.name;


/* ------------------------------------------------
🔹 One-Line Summary
------------------------------------------------ */

-- MySQL supports UNION & UNION ALL directly,
-- EXCEPT & INTERSECT are achieved using JOINs.
*/






'''
