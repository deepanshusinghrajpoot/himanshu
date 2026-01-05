/*




✅ SQL Window Functions – Final Interview Notes (Complete + Correct + Easy)

We use the employee table for all examples.




⭐ PARENT TABLE (employee)


| emp_id | emp_name | dept_name | salary |
| ------ | -------- | --------- | ------ |
| 101    | Aditi    | IT        | 90000  |
| 102    | Rahul    | IT        | 90000  |
| 103    | Sneha    | IT        | 85000  |
| 104    | Karan    | HR        | 70000  |
| 105    | Priya    | HR        | 60000  |
| 106    | Amit     | HR        | 60000  |
| 107    | John     | Finance   | 95000  |
| 108    | Riya     | Finance   | 90000  |
| 109    | Mohan    | Finance   | 85000  |




🔹 What is a Window Function?

lll A window function performs calculations across a set of rows related to the current row, 
    without merging rows (unlike aggregate functions).


🔹 Why OVER()?

Because when you write:

MAX(salary) OVER(PARTITION BY dept_name)


SQL treats MAX() as a window function, not an aggregate.

Window functions do NOT collapse rows.



-----------------------------------
🔥 1. MAX() OVER(PARTITION BY)
-----------------------------------

Query

SELECT e.*,
       MAX(salary) OVER(PARTITION BY dept_name) AS max_salary
FROM employee e;

| emp_id | emp_name | dept    | salary | max_salary |
| ------ | -------- | ------- | ------ | ---------- |
| 101    | Aditi    | IT      | 90000  | 90000      |
| 102    | Rahul    | IT      | 90000  | 90000      |
| 103    | Sneha    | IT      | 85000  | 90000      |
| 104    | Karan    | HR      | 70000  | 70000      |
| 105    | Priya    | HR      | 60000  | 70000      |
| 106    | Amit     | HR      | 60000  | 70000      |
| 107    | John     | Finance | 95000  | 95000      |
| 108    | Riya     | Finance | 90000  | 95000      |
| 109    | Mohan    | Finance | 85000  | 95000      |

Explanation

OVER() → Creates a window.
PARTITION BY dept_name → One window per department.

Every row shows the highest salary of its department.



-------------------------
🔥 2. ROW_NUMBER()
-------------------------
Definition

lll Assigns a unique sequential number to each row in a window.
    No ties → always 1, 2, 3...


Query

SELECT e.*,
       ROW_NUMBER() OVER(PARTITION BY dept_name ORDER BY emp_id) AS rn
FROM employee e;


| emp_id | dept    | salary | ROW_NUMBER |
| ------ | ------- | ------ | ---------- |
| 101    | IT      | 90000  | 1          |
| 102    | IT      | 90000  | 2          |
| 103    | IT      | 85000  | 3          |
| 104    | HR      | 70000  | 1          |
| 105    | HR      | 60000  | 2          |
| 106    | HR      | 60000  | 3          |
| 107    | Finance | 95000  | 1          |
| 108    | Finance | 90000  | 2          |
| 109    | Finance | 85000  | 3          |

⭐ Interview Question

❓ Fetch the first 2 employees from each department.

Query

SELECT x.*
FROM (
        SELECT e.*,
               ROW_NUMBER() OVER(PARTITION BY dept_name ORDER BY emp_id) AS rn
        FROM employee e
     ) x
WHERE x.rn <= 2;


| emp_id | emp_name | dept    | salary | rn |
| ------ | -------- | ------- | ------ | -- |
| 101    | Aditi    | IT      | 90000  | 1  |
| 102    | Rahul    | IT      | 90000  | 2  |
| 104    | Karan    | HR      | 70000  | 1  |
| 105    | Priya    | HR      | 60000  | 2  |
| 107    | John     | Finance | 95000  | 1  |
| 108    | Riya     | Finance | 90000  | 2  |




----------------------
🔥 3. RANK()
----------------------
Definition

lll Gives a rank within each window with gaps (skips) when ties occur.
    Same values → same rank
    Next rank → jumps

Query

SELECT e.*,
       RANK() OVER(PARTITION BY dept_name ORDER BY salary DESC) AS rnk
FROM employee e;


| emp_id | dept    | salary | RANK |
| ------ | ------- | ------ | ---- |
| 101    | IT      | 90000  | 1    |
| 102    | IT      | 90000  | 1    |
| 103    | IT      | 85000  | 3    |
| 104    | HR      | 70000  | 1    |
| 105    | HR      | 60000  | 2    |
| 106    | HR      | 60000  | 2    |
| 107    | Finance | 95000  | 1    |
| 108    | Finance | 90000  | 2    |
| 109    | Finance | 85000  | 3    |


Why rank skips?

| Salary | Rank                   |
| ------ | ---------------------- |
| 90000  | 1                      |
| 90000  | 1                      |
| 85000  | **3** ← rank 2 skipped |



⭐ Interview Question
❓ Fetch top 3 salary holders from each department.


SELECT x.*
FROM (
        SELECT e.*,
               RANK() OVER(PARTITION BY dept_name ORDER BY salary DESC) AS rnk
        FROM employee e
     ) x
WHERE x.rnk <= 3;





-----------------------------
🔥 4. DENSE_RANK()
-----------------------------
Definition

lll Ranks rows within a partition without gaps.

Same values → same rank
Next rank increments normally

Query

SELECT e.*,
       DENSE_RANK() OVER(PARTITION BY dept_name ORDER BY salary DESC) AS dense_rnk
FROM employee e;


| emp_id | dept    | salary | DENSE_RANK |
| ------ | ------- | ------ | ---------- |
| 101    | IT      | 90000  | 1          |
| 102    | IT      | 90000  | 1          |
| 103    | IT      | 85000  | 2          |
| 104    | HR      | 70000  | 1          |
| 105    | HR      | 60000  | 2          |
| 106    | HR      | 60000  | 2          |
| 107    | Finance | 95000  | 1          |
| 108    | Finance | 90000  | 2          |
| 109    | Finance | 85000  | 3          |


⭐ Difference Table (Super Clear)

| Salary | ROW_NUMBER | RANK | DENSE_RANK |
| ------ | ---------- | ---- | ---------- |
| 90000  | 1          | 1    | 1          |
| 90000  | 2          | 1    | 1          |
| 85000  | 3          | 3    | 2          |


Summary

ROW_NUMBER() → Always unique
RANK() → Ties + gaps
DENSE_RANK() → Ties + no gaps






*/








