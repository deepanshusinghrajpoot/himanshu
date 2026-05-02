'''



177. Nth Highest Salary
========================


Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the nth highest distinct salary from the Employee table. If there are less than n distinct salaries, return null.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+

















CREATE FUNCTION getNthHighestSalary(n INT) RETURNS INT
BEGIN

     DECLARE nth_salary INT;

     SELECT MAX(t.salary) INTO nth_salary
     FROM (
            SELECT salary,
                    DENSE_RANK() OVER w AS dn_rnk
            FROM Employee
            WHERE salary IS NOT NULL
            WINDOW w AS (ORDER BY salary DESC)
     ) t
     WHERE t.dn_rnk = n;

    RETURN nth_salary;

END ;



'''