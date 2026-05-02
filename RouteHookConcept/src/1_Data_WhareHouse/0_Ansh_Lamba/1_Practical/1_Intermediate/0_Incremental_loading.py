'''

# Incremental Data Loading ✅
=============================

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




INSERT INTO sales.Orders
(OrderID, OrderDate, CustomerID, CustomerName, CustomerEmail, ProductID, ProductName,
 ProductCategory, RegionID, RegionName, Country, Quantity, UnitPrice, TotalAmount)
VALUES

(1011, '2024-02-15', 509, 'Karan Malhotra', 'karan.m@gmail.com', 211, 'Gaming Mouse', 'Electronics', 1, 'North', 'India', 2, 1500, 3000),
(1012, '2024-02-18', 501, 'Amit Sharma', 'amit.sharma@gmail.com', 212, 'Monitor 24 inch', 'Electronics', 1, 'North', 'India', 1, 12000, 12000),
(1013, '2024-02-20', 510, 'Riya Sen', 'riya.sen@gmail.com', 213, 'Yoga Mat', 'Sports', 4, 'East', 'India', 3, 800, 2400),
(1014, '2024-02-22', 506, 'Sneha Kapoor', 'sneha.kapoor@gmail.com', 214, 'Microwave Oven', 'Appliances', 2, 'South', 'India', 1, 10000, 10000),
(1015, '2024-02-25', 503, 'Rahul Singh', 'rahul.singh@gmail.com', 215, 'Bluetooth Speaker', 'Electronics', 1, 'North', 'India', 2, 3500, 7000);





SELECT * FROM sales.Orders;


gpt give table







DATA WAREHOUSING
================


CREATE DATABASE salesDWH;



Staging Layer
-------------

CREATE OR REPLACE TABLE salesDWH.stg_sales
AS 
SELECT * FROM sales.Orders
WHERE OrderDate > '2024-02-10';




Transformation
--------------

-- Suppose we want to apply simple transformation

CREATE VIEW salesDWH.trans_sales
AS
SELECT * FROM salesDWH.stg_sales WHERE Quantity IS NOT NULL;




-- verify

SELECT * FROM salesDWH.trans_sales;

| OrderID | OrderDate  | CustomerName   | ProductName       | Qty | Total |
| ------- | ---------- | -------------- | ----------------- | --- | ----- |
| 1011    | 2024-02-15 | Karan Malhotra | Gaming Mouse      | 2   | 3000  |
| 1012    | 2024-02-18 | Amit Sharma    | Monitor 24 inch   | 1   | 12000 |
| 1013    | 2024-02-20 | Riya Sen       | Yoga Mat          | 3   | 2400  |
| 1014    | 2024-02-22 | Sneha Kapoor   | Microwave Oven    | 1   | 10000 |
| 1015    | 2024-02-25 | Rahul Singh    | Bluetooth Speaker | 2   | 7000  |




Core Layer
----------

Note : Actualy we not server data as well as because we create data models.

CREATE OR REPLACE TABLE salesDWH.core_sales (
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


INSERT INTO salesDWH.core_sales
SELECT * FROM salesDWH.trans_sales;





DWH Core Layer Display
----------------------

SELECT * FROM salesDWH.core_sales;

| OrderID | OrderDate  | CustomerName   | ProductName       | Category    | Qty | Total |
| ------- | ---------- | -------------- | ----------------- | ----------- | --- | ----- |
| 1011    | 2024-02-15 | Karan Malhotra | Gaming Mouse      | Electronics | 2   | 3000  |
| 1012    | 2024-02-18 | Amit Sharma    | Monitor 24 inch   | Electronics | 1   | 12000 |
| 1013    | 2024-02-20 | Riya Sen       | Yoga Mat          | Sports      | 3   | 2400  |
| 1014    | 2024-02-22 | Sneha Kapoor   | Microwave Oven    | Appliances  | 1   | 10000 |
| 1015    | 2024-02-25 | Rahul Singh    | Bluetooth Speaker | Electronics | 2   | 7000  |




'''