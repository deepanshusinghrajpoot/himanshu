import React from 'react'


/*






🔹 SQL CASE Statement

1. What is CASE?
----------------

CASE allows you to add conditional logic inside SQL queries.
Works like if … else if … else.


Can be used in:

SELECT
ORDER BY
GROUP BY
HAVING




2. Syntax of CASE
-----------------

(A) Simple CASE

Matches against one expression.

CASE expression
   WHEN value1 THEN result1
   WHEN value2 THEN result2
   ELSE resultN
END












✅ Example:

SELECT order_id, status,
  CASE status
    WHEN 'P' THEN 'Pending'
    WHEN 'C' THEN 'Completed'
    WHEN 'X' THEN 'Cancelled'
    ELSE 'Unknown'
  END AS status_text
FROM orders;


(B) Searched CASE

Uses conditions (more flexible, like if/else).

CASE
   WHEN condition1 THEN result1
   WHEN condition2 THEN result2
   ELSE resultN
END




✅ Example:

SELECT order_id, profit,
  CASE
    WHEN profit < 0 THEN 'Loss'
    WHEN profit < 50 THEN 'Low Profit'
    WHEN profit < 100 THEN 'High Profit'
    ELSE 'Very High Profit'
  END AS profit_bucket
FROM orders_data;




3. Usage Examples
(i) In SELECT

Convert values to readable format:

SELECT emp_id, gender,
  CASE gender
    WHEN 'M' THEN 'Male'
    WHEN 'F' THEN 'Female'
    ELSE 'Other'
  END AS gender_text
FROM employees;





(ii) In ORDER BY

Sort rows using conditional logic:

SELECT emp_name, dept
FROM employees
ORDER BY
  CASE dept
    WHEN 'HR' THEN 1
    WHEN 'IT' THEN 2
    ELSE 3
  END;





(iii) In GROUP BY

Bucket data for aggregation:

SELECT
  CASE
    WHEN age < 18 THEN 'Teen'
    WHEN age BETWEEN 18 AND 30 THEN 'Young'
    WHEN age BETWEEN 31 AND 50 THEN 'Middle-aged'
    ELSE 'Senior'
  END AS age_group,
  COUNT(*) AS total
FROM users
GROUP BY
  CASE
    WHEN age < 18 THEN 'Teen'
    WHEN age BETWEEN 18 AND 30 THEN 'Young'
    WHEN age BETWEEN 31 AND 50 THEN 'Middle-aged'
    ELSE 'Senior'
  END;





(iv) In HAVING

Filter grouped data:

SELECT dept, COUNT(*) AS total
FROM employees
GROUP BY dept
HAVING
  CASE
    WHEN dept = 'IT' THEN COUNT(*) > 5
    ELSE COUNT(*) > 2
  END;









4. Key Points / Rules :- Imp

Always end CASE with END.
ELSE is optional (default = NULL).
Can nest multiple CASE inside each other.
Works in all SQL dialects (MySQL, PostgreSQL, SQL Server, Oracle).
Simple CASE → equality check.
Searched CASE → condition check (preferred).







5. Advanced Example (Nested CASE)

SELECT order_id, profit,
  CASE
    WHEN profit < 0 THEN 'Loss'
    WHEN profit BETWEEN 0 AND 100 THEN 
      CASE
        WHEN profit < 50 THEN 'Low Profit'
        ELSE 'Moderate Profit'
      END
    ELSE 'High Profit'
  END AS profit_category
FROM orders_data;





✅ Summary:

CASE = conditional if/else in SQL.
2 Types → Simple & Searched.
Can be used in SELECT, ORDER BY, GROUP BY, HAVING.
Supports nested logic & bucketing.
























*/
























const CaseStatement = () => {
  return (
    <div>CaseStatement</div>
  )
}

export default CaseStatement