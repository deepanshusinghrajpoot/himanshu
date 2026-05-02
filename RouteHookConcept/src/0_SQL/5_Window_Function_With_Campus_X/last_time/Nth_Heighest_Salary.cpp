/*





Nth Highest Salary from employee table
---------------------------------------



Answer 1:-
.........

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement

     SELECT salary
     FROM( 
          SELECT DISTINCT salary,
                 DENSE_RANK() OVER w AS dnk
          FROM Employee
          WINDOW w AS (ORDER BY salary DESC)
     )t
     WHERE dnk = N
      
  );
END



Answer 2:-
.........

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT DISTINCT salary
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET N-1
  );
END;







*/