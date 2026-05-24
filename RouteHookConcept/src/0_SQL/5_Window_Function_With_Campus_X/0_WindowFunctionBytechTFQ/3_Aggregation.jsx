/*




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




 */