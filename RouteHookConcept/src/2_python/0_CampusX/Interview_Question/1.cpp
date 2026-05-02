/*



create a deep copy
===================

✅ Method 1: Using slicing
a = [1, 2, 3]
b = a[:]

✅ Method 2: Using list() constructor
b = list(a)

✅ Method 3: Using .copy() method
b = a.copy()







SELECT DISTINCT salary
FROM (
         SELECT *,
         DENSE_RANK() OVER(ORDER BY salary DESC)  AS d_rnk
         FROM Employees
) t
WHERE d_rnk = 2






*/