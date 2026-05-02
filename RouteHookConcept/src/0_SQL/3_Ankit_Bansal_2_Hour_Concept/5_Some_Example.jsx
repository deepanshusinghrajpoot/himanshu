import React from 'react'





/*

Perfect, Deepanshu 👌
I’ll clean up your notes, fix spelling/typos (like `salse → sales`, `oders_data → orders_data`), ensure consistency (`orders_date` vs `orders_data`), add small explanations, and format them into **interview-ready SQL notes**.

Here’s your **corrected + polished version**:

---


# 📘 SQL Interview Notes (Clean & Corrected)























************************************
------------------------------------
## 3. Creating New temporary Columns
------------------------------------
************************************


📌 Parent Table: orders_data

| order\_id | order\_date | ship\_date | customer\_name | region | city    | category   | product\_id | sales | quantity | profit |
| --------- | ----------- | ---------- | -------------- | ------ | ------- | ---------- | ----------- | ----- | -------- | ------ |
| 101       | 2025-01-05  | 2025-01-08 | Rahul Sharma   | North  | Delhi   | Furniture  | P001        | 1200  | 2        | 200    |
| 102       | 2025-01-07  | 2025-01-10 | Priya Singh    | South  | Chennai | Technology | P002        | 2500  | 1        | 500    |
| 103       | 2025-01-08  | 2025-01-12 | Aman Verma     | North  | Lucknow | OfficeSup  | P003        | 800   | 5        | 100    |
| 104       | 2025-01-10  | 2025-01-15 | Neha Gupta     | West   | Mumbai  | Furniture  | P004        | 1500  | 3        | 250    |
| 105       | 2025-01-11  | 2025-01-16 | Suresh Kumar   | East   | Kolkata | Technology | P005        | 3000  | 2        | 600    |



SELECT *, profit / sales AS profit_ratio 
FROM orders_data;


📌 Result Table

👉 A new column profit_ratio is calculated for each row (profit ÷ sales).

| order\_id | order\_date | ship\_date | customer\_name | region | city    | category   | product\_id | sales | quantity | profit | profit\_ratio |
| --------- | ----------- | ---------- | -------------- | ------ | ------- | ---------- | ----------- | ----- | -------- | ------ | ------------- |
| 101       | 2025-01-05  | 2025-01-08 | Rahul Sharma   | North  | Delhi   | Furniture  | P001        | 1200  | 2        | 200    | 0.1667        |
| 102       | 2025-01-07  | 2025-01-10 | Priya Singh    | South  | Chennai | Technology | P002        | 2500  | 1        | 500    | 0.2000        |
| 103       | 2025-01-08  | 2025-01-12 | Aman Verma     | North  | Lucknow | OfficeSup  | P003        | 800   | 5        | 100    | 0.1250        |
| 104       | 2025-01-10  | 2025-01-15 | Neha Gupta     | West   | Mumbai  | Furniture  | P004        | 1500  | 3        | 250    | 0.1667        |
| 105       | 2025-01-11  | 2025-01-16 | Suresh Kumar   | East   | Kolkata | Technology | P005        | 3000  | 2        | 600    | 0.2000        |



📌 Functionality of SQL Keywords

SELECT * → Selects all existing columns.
profit / sales → Performs a calculation for each row.
AS profit_ratio → Gives a name (alias) to the calculated column.
FROM orders_data → Source table.





📌 Execution Order

FROM → Load the table.
SELECT →
          Include all columns (*).
          Calculate profit / sales.
          Rename it as profit_ratio.


✅ Now you have a derived column that doesn’t exist in the table but is calculated on the fly.
























































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

