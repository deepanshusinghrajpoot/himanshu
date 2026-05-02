
import React from 'react'


/*


Question 2
-----------

Display higest and lowest salary from the given employee table, display the highest and lowest salary corresponding to 
each department. Return the result corresponding to each employee record.
=======================================================================================================================



SELECT 
    emp_id,
    emp_name,
    dept,
    salary,
    MAX(salary) OVER (PARTITION BY dept) AS highest_salary,
    MIN(salary) OVER (PARTITION BY dept) AS lowest_salary
FROM employees;






📤 Final Output


| emp_id | dept    | salary | highest_salary | lowest_salary |
| ------ | ------- | ------ | -------------- | ------------- |
| 1      | IT      | 60000  | 80000          | 50000         |
| 2      | IT      | 80000  | 80000          | 50000         |
| 3      | IT      | 50000  | 80000          | 50000         |
| 4      | HR      | 40000  | 70000          | 40000         |
| 5      | HR      | 70000  | 70000          | 40000         |
| 6      | Finance | 90000  | 90000   

📋 Parent Table: employees

| emp_id | emp_name | dept | salary |
| ------ | -------- | ---- | ------ |
| 1      | A        | IT   | 80000  |
| 2      | B        | IT   | 60000  |
| 3      | C        | IT   | 50000  |
| 4      | D        | HR   | 70000  |
| 5      | E        | HR   | 40000  |


🧠 Concept (Why FULL FRAME is Used)

Using ORDER BY inside OVER() creates a running window
Default frame becomes:
UNBOUNDED PRECEDING → CURRENT ROW
MIN() with a running frame gives running minimum
Full frame (UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) forces SQL to:
Scan all rows in the department
Return true department-level minimum for every employee

📤 Output Table

| emp_id | emp_name | dept | salary | highest_salary | lowest_salary |
| ------ | -------- | ---- | ------ | -------------- | ------------- |
| 1      | A        | IT   | 80000  | 80000          | 50000         |
| 2      | B        | IT   | 60000  | 80000          | 50000         |
| 3      | C        | IT   | 50000  | 80000          | 50000         |
| 4      | D        | HR   | 70000  | 70000          | 40000         |
| 5      | E        | HR   | 40000  | 70000          | 40000         |

✔ highest_salary appears correct due to descending order
✔ lowest_salary is correct only because full frame is explicitly used


*/




const Highest_lowest = () => {
  return (
    <div>2_Highest_lowest</div>
  )
}

export default Highest_lowest