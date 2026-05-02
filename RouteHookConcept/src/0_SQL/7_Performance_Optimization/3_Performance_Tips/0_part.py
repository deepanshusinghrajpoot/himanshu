'''


Always check the execution plan to confirm performance 
improvements when optimizing your query.


If there's no improvement then just focus on readability.


=================================
Best Practices of FETCHING DATA
=================================


TIP 1 : Select Only What Needed
--------------------------------

-- Bad Practice
SELECT * FROM Sales.Customers;


-- Good Practice
SELECT CustomerID, FirstName, LastName FROM Sales.Customers;




TIP 2 : unesessary DISTINCT & ORDER BY
---------------------------------------

-- Bad Practice
SELECT DISTINCT 
       FirstName
FROM Sales.Customers
ORDER BY FirstName


-- Good Practice
SELECT FirstName
FROM Sales.Customers;





TIP 3 : For Exporation Purpose, Limit Rows
------------------------------------------

-- Bad Practice
SELECT 
       OrderID,
       Sales
FROM Sales.Orders;


-- Good Practice
SELECT TOP 10
       OrderID,
       Sales
FROM Sales.Orders;









===================================
Best Practices FILTERING DATA
===================================


TIP 4 : Create nonclustered index on frequently used columns in WHERE clause
-----------------------------------------------------------------------------

gpt give code of mySql



TIP 5 : Avoid applying Functions to columns in WHERE clause
-----------------------------------------------------------

-- Bad Practice
SELECT * FROM Sales.Orders
WHERE LOWER(OrderStatus) = 'delivered';


Note : Functions on columns can block index usage



-- Good Practice
SELECT * FROM Sales.Orders
WHERE OrderStatus = 'Delivered';




TIP 6 : Avoid leading wildcards as they prevent index usage
------------------------------------------------------------

-- Bad Practice
SELECT *
FROM Sales.Customers
WHERE LastName LIKE '%Gold%';


-- Good Practice
SELECT *
FROM Sales.Customers
WHERE LastName LIKE 'Gold%';




TIP 7 : Use IN instead of multiple OR conditions
------------------------------------------------

-- Bad Practice
SELECT *
FROM Sales.Orders
WHERE CustomerID = 1 OR CustomerID = 2 CustomerID = 3;



-- Good Practice
SELECT *
FROM Sales.Orders
WHERE CustomerID IN (1, 2, 3);








======================================================
Best Practices JOINING DATA
======================================================


TIP 8 : Understand The Speed of Joins & Use INNER JOIN when possible
--------------------------------------------------------------------

-- Performance 
INNER JOIN > LEFT JOIN = RIGHT JOIN > OUTER JOIN






TIP 9 : Use Explicit Join (ANSI Join) Instead of Implicit Join (non-ANSI Join)
-------------------------------------------------------------------------------


-- Bad Practice
SELECT o.OrderID, c.FirstName
FROM Sales.Customers c , Sales.Orders o
ON c.CustomerID = o.CustomerID;



-- Good Practice
SELECT o.OrderID, c.FirstName
FROM Sales.Customers c
INNER JOIN Sales.Orders o
        ON c.CustomerID = o.CustomerID;



TIP 10 : Make sure to index the columns used in the ON clause
-------------------------------------------------------------


TIP 11 : Filter Before Joining (Big Tables)
--------------------------------------------

-- Good Practice
SELECT c.FirstName, o.OrderID
FROM Sales.Customers c
INNER JOIN (SELECT OrderID, CustomerID FROM Sales.Orders WHERE OrderStatus = 'Delivered') o
ON c.CustomerID = o.CustomerID;




TIP 12 : Aggregate Before Joining (Big Tables)
-----------------------------------------------

-- Good Practice
SELECT c.CustomerID , c.FirstName, o.OrderCount
FROM Sales.Customers c
INNER JOIN (
    SELECT CustomerID, COUNT(OrderID) AS OrderCount
    FROM Sales.Customers c
    GROUP BY CustomerID
) o
ON c.CustomerID = o.CustomerID;






'''