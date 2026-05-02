'''


----------------------------------
Method : Window Function
----------------------------------



SELECT MAX(t.salary) AS SecondHighestSalary
FROM(
        SELECT salary,
            DENSE_RANK() OVER w AS dn_rnk
        FROM Employee
        WHERE salary IS NOT NULL
        WINDOW w AS (ORDER BY salary DESC)
) t
WHERE t.dn_rnk = 2;





---------------------------------------------------------------------
Note: MAX() ensures:
      No row → returns NULL instead of empty result
----------------------------------------------------------------------




'''