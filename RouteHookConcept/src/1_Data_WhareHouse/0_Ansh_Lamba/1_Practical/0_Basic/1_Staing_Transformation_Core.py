'''

# Setup of Data Warehouse (Staging → Transformation → Core) ✅
===============================================================

---

## Step 1: Source Database (OLTP)
---------------------------------


CREATE DATABASE sales;



CREATE TABLE sales.Orders (
    OrderID INT,
    OrderDate DATE,
    CustomerID INT,
    CustomerName STRING,
    CustomerEmail STRING,
    ProductID INT,
    ProductName STRING,
    ProductCategory STRING,
    RegionID INT,
    RegionName STRING,
    Country STRING,
    Quantity INT,
    UnitPrice INT,
    TotalAmount INT
);





INSERT INTO sales.Orders
(OrderID, OrderDate, CustomerID, CustomerName, CustomerEmail, ProductID, ProductName,
 ProductCategory, RegionID, RegionName, Country, Quantity, UnitPrice, TotalAmount)
VALUES

(1001, '2024-01-15', 501, 'Amit Sharma', 'amit.sharma@gmail.com', 201, 'Laptop Pro', 'Electronics', 1, 'North', 'India', 1, 75000, 75000),
(1002, '2024-01-16', 502, 'Priya Verma', 'priya.verma@gmail.com', 202, 'Office Chair', 'Furniture', 2, 'South', 'India', 2, 8500, 17000),
(1003, '2024-01-17', 503, 'Rahul Singh', 'rahul.singh@gmail.com', 203, 'Smartphone X', 'Electronics', 1, 'North', 'India', 3, 25000, 75000),
(1004, '2024-01-18', 504, 'Neha Gupta', 'neha.gupta@gmail.com', 204, 'Dining Table', 'Furniture', 3, 'West', 'India', 1, 20000, 20000),
(1005, '2024-01-19', 505, 'Arjun Mehta', 'arjun.mehta@gmail.com', 205, 'Running Shoes', 'Sports', 4, 'East', 'India', 4, 3000, 12000),
(1006, '2024-02-01', 501, 'Amit Sharma', 'amit.sharma@gmail.com', 206, 'Headphones', 'Electronics', 1, 'North', 'India', 2, 5000, 10000),
(1007, '2024-02-03', 506, 'Sneha Kapoor', 'sneha.kapoor@gmail.com', 207, 'Refrigerator', 'Appliances', 2, 'South', 'India', 1, 45000, 45000),
(1008, '2024-02-05', 507, 'Vikas Yadav', 'vikas.yadav@gmail.com', 208, 'Cricket Bat', 'Sports', 4, 'East', 'India', 2, 2000, 4000),
(1009, '2024-02-07', 508, 'Pooja Mishra', 'pooja.mishra@gmail.com', 209, 'Washing Machine', 'Appliances', 3, 'West', 'India', 1, 30000, 30000),
(1010, '2024-02-10', 503, 'Rahul Singh', 'rahul.singh@gmail.com', 210, 'Tablet', 'Electronics', 1, 'North', 'India', 2, 15000, 30000);





SELECT * FROM sales.Orders;


| OrderID | OrderDate  | CustomerName | ProductName     | Category    | Region | Qty | Price | Total |
| ------- | ---------- | ------------ | --------------- | ----------- | ------ | --- | ----- | ----- |
| 1001    | 2024-01-15 | Amit Sharma  | Laptop Pro      | Electronics | North  | 1   | 75000 | 75000 |
| 1002    | 2024-01-16 | Priya Verma  | Office Chair    | Furniture   | South  | 2   | 8500  | 17000 |
| 1003    | 2024-01-17 | Rahul Singh  | Smartphone X    | Electronics | North  | 3   | 25000 | 75000 |
| 1004    | 2024-01-18 | Neha Gupta   | Dining Table    | Furniture   | West   | 1   | 20000 | 20000 |
| 1005    | 2024-01-19 | Arjun Mehta  | Running Shoes   | Sports      | East   | 4   | 3000  | 12000 |
| 1006    | 2024-02-01 | Amit Sharma  | Headphones      | Electronics | North  | 2   | 5000  | 10000 |
| 1007    | 2024-02-03 | Sneha Kapoor | Refrigerator    | Appliances  | South  | 1   | 45000 | 45000 |
| 1008    | 2024-02-05 | Vikas Yadav  | Cricket Bat     | Sports      | East   | 2   | 2000  | 4000  |
| 1009    | 2024-02-07 | Pooja Mishra | Washing Machine | Appliances  | West   | 1   | 30000 | 30000 |
| 1010    | 2024-02-10 | Rahul Singh  | Tablet          | Electronics | North  | 2   | 15000 | 30000 |









DATA WAREHOUSING
================


CREATE DATABASE salesDWH;



Staging Layer
-------------

CREATE TABLE salesDWH.stg_sales
AS 
SELECT * FROM sales.Orders;




Transformation
--------------

-- Suppose we want to apply simple transformation

CREATE VIEW salesDWH.trans_sales
AS
SELECT * FROM salesDWH.stg_sales WHERE Quantity IS NOT NULL;



Core Layer
----------

CREATE TABLE salesDWH.core_sales
AS
SELECT * FROM salesDWH.trans_sales;





DWH Core Layer Display
----------------------

SELECT * FROM salesDWH.core_sales;


| OrderID | OrderDate  | CustomerName | ProductName     | Category    | Region | Qty | Price | Total |
| ------- | ---------- | ------------ | --------------- | ----------- | ------ | --- | ----- | ----- |
| 1001    | 2024-01-15 | Amit Sharma  | Laptop Pro      | Electronics | North  | 1   | 75000 | 75000 |
| 1002    | 2024-01-16 | Priya Verma  | Office Chair    | Furniture   | South  | 2   | 8500  | 17000 |
| 1003    | 2024-01-17 | Rahul Singh  | Smartphone X    | Electronics | North  | 3   | 25000 | 75000 |
| 1004    | 2024-01-18 | Neha Gupta   | Dining Table    | Furniture   | West   | 1   | 20000 | 20000 |
| 1005    | 2024-01-19 | Arjun Mehta  | Running Shoes   | Sports      | East   | 4   | 3000  | 12000 |
| 1006    | 2024-02-01 | Amit Sharma  | Headphones      | Electronics | North  | 2   | 5000  | 10000 |
| 1007    | 2024-02-03 | Sneha Kapoor | Refrigerator    | Appliances  | South  | 1   | 45000 | 45000 |
| 1008    | 2024-02-05 | Vikas Yadav  | Cricket Bat     | Sports      | East   | 2   | 2000  | 4000  |
| 1009    | 2024-02-07 | Pooja Mishra | Washing Machine | Appliances  | West   | 1   | 30000 | 30000 |
| 1010    | 2024-02-10 | Rahul Singh  | Tablet          | Electronics | North  | 2   | 15000 | 30000 |





'''