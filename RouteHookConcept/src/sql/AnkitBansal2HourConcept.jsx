import React from 'react'





/*

Perfect, Deepanshu 👌
I’ll clean up your notes, fix spelling/typos (like `salse → sales`, `oders_data → orders_data`), ensure consistency (`orders_date` vs `orders_data`), add small explanations, and format them into **interview-ready SQL notes**.

Here’s your **corrected + polished version**:

---


# 📘 SQL Interview Notes (Clean & Corrected)






## 1. Select Statements

* Select all columns:

```sql
SELECT * 
FROM orders_data;
```

* Select specific columns:

```sql
SELECT order_id, order_date, sales, profit 
FROM orders_data;
```

* Select top rows:

```sql
-- SQL Server
SELECT TOP 10 order_id, order_date, sales, profit 
FROM orders_data;

-- MySQL / PostgreSQL
SELECT order_id, order_date, sales, profit 
FROM orders_data 
LIMIT 10;
```

---











## 2. Sorting (ORDER BY)

* Sort by multiple columns:

```sql
SELECT * 
FROM orders_data 
ORDER BY order_date, profit;
```

* Descending & ascending order:

```sql
SELECT * 
FROM orders_data 
ORDER BY order_date DESC, profit ASC;
```

⚡ Execution Order:
`FROM → SELECT → ORDER BY → TOP`

---











## 3. Creating New Columns

```sql
SELECT *, profit / sales AS profit_ratio 
FROM orders_data;
```

---













## 4. Filtering Data (WHERE)

* Filter by region:

```sql
SELECT * 
FROM orders_data 
WHERE region = 'Central';
```

* Filter by date:

```sql
SELECT * 
FROM orders_data 
WHERE order_date > '2019-09-17'
ORDER BY order_date;
```

* Operators: `AND`, `OR`, `NOT`, `IN`, `BETWEEN`, `LIKE`

```sql
-- AND
SELECT * FROM orders_data 
WHERE quantity > 3 AND category = 'Technology' AND region = 'Central';

-- OR
SELECT * FROM orders_data 
WHERE quantity > 3 OR category = 'Technology' OR region = 'Central';

-- IN / BETWEEN
SELECT * FROM orders_data 
WHERE quantity BETWEEN 3 AND 5;

SELECT * FROM orders_data 
WHERE quantity IN (3, 4, 5);
```

* Pattern Matching (`LIKE`):

```sql
SELECT * FROM orders_data
WHERE customer_name LIKE 'A%';   -- starts with A
-- '%A' → ends with A
-- '%A%' → contains A
-- '_A%' → 2nd character is A
-- '_[ae]%' → 2nd character is a or e
```




⚡ Execution Order:
-------------------------------------
`FROM → WHERE → SELECT → ORDER BY`
-------------------------------------

---












## 5. Aggregate Functions

```sql
SELECT SUM(sales) AS total_sales FROM orders_data;
SELECT COUNT(*) AS total_records FROM orders_data;
SELECT SUM(sales)/COUNT(*) AS avg_sales FROM orders_data;
```

* Distinct:

```sql
SELECT DISTINCT category, region 
FROM orders_data;
```

* Group By:

```sql
SELECT category, SUM(sales) AS category_sales, SUM(profit) AS category_profit
FROM orders_data
GROUP BY category;
```

* Having (filter groups):

```sql
SELECT city, SUM(sales) AS city_sales
FROM orders_data
GROUP BY city
HAVING SUM(sales) > 100;
```

⚡ Execution Order:
`FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → TOP`

---














## 6. Joins

* Inner Join:

```sql
SELECT *
FROM orders_data o
INNER JOIN returns_data r ON o.order_id = r.order_id
WHERE r.return_reason = 'Wrong Item' AND city = 'Los Angeles';
```

* Left Join (including non-returned orders):

```sql
SELECT o.*, r.return_reason
FROM orders_data o
LEFT JOIN returns_data r ON o.order_id = r.order_id;
```

* Find non-returned orders:

```sql
SELECT o.*
FROM orders_data o
LEFT JOIN returns_data r ON o.order_id = r.order_id
WHERE r.return_reason IS NULL;
```

---















## 7. CASE Statement (Bucketing)

```sql
SELECT *, 
  CASE 
    WHEN profit < 0 THEN 'Loss'
    WHEN profit < 50 THEN 'Low Profit'
    WHEN profit < 100 THEN 'High Profit'
    ELSE 'Very High Profit'
  END AS profit_bucket
FROM orders_data;
```

---

















## 8. String Functions

```sql
SELECT *,
  LEN(customer_name) AS cust_length,
  LEFT(customer_name, 3) AS first_three_char,
  RIGHT(customer_name, 3) AS last_three_char,
  SUBSTRING(customer_name, 1, 3) AS substring_name,
  REPLACE(customer_name, ' ', '_') AS replaced_name,
  UPPER(customer_name) AS upper_case,
  LOWER(customer_name) AS lower_case,
  REVERSE(customer_name) AS reverse_name,
  TRIM(customer_name) AS trimmed_name,
  CHARINDEX('A', customer_name) AS index_of_A
FROM orders_data;
```

---



















## 9. Date Functions

* Extract parts of a date:

```sql
SELECT 
  DATEPART(year, order_date) AS order_year,
  DATEPART(month, order_date) AS order_month,
  DATEPART(day, order_date) AS order_day,
  SUM(sales) AS total_sales
FROM orders_data
GROUP BY DATEPART(year, order_date), DATEPART(month, order_date), DATEPART(day, order_date)
ORDER BY order_year, order_month, order_day;
```

* Date differences and additions:

```sql
SELECT order_id, order_date, ship_date,
  DATEDIFF(day, order_date, ship_date) AS days_to_ship,
  DATEADD(day, 5, order_date) AS five_days_later
FROM orders_data;
```

---



*/








const AnkitBansal2HourConcept = () => {
  return (
    <div>AnkitBansal2HourConcept</div>
  )
}

export default AnkitBansal2HourConcept

