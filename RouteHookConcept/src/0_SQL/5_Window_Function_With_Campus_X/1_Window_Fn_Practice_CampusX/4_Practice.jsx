/*



++++++++++++++++++++ Practice window function (LEAD(arg1, arg2, arg3), LAG(arg1, arg2, arg3)) ++++++++++++++++++++++++++++++++++++
__________________________________________________________________________________________________________________________________



5️⃣ orders table (Sample Data – 10)

| order_id | user_id | r_id | amount | date       | partner_id | delivery_time | delivery_rating | restorant_rating |
| -------: | ------: | ---: | -----: | ---------- | ---------: | ------------: | --------------: | ---------------: |
|        1 |       1 |  201 |    400 | 2024-01-01 |        101 |            30 |               5 |                4 |
|        2 |       2 |  202 |    520 | 2024-01-02 |        102 |            35 |               4 |                5 |
|        3 |       3 |  203 |    300 | 2024-01-03 |        103 |            25 |               5 |                4 |
|        4 |       4 |  204 |    350 | 2024-01-04 |        104 |            40 |               3 |                3 |
|        5 |       5 |  205 |    280 | 2024-01-05 |        105 |            20 |               5 |                5 |
|        6 |       6 |  201 |    450 | 2024-01-06 |        106 |            45 |               2 |                3 |
|        7 |       7 |  202 |    600 | 2024-01-07 |        107 |            38 |               4 |                4 |
|        8 |       8 |  203 |    320 | 2024-01-08 |        108 |            28 |               5 |                4 |
|        9 |       9 |  204 |    360 | 2024-01-09 |        109 |            33 |               4 |                3 |
|       10 |      10 |  205 |    290 | 2024-01-10 |        110 |            22 |               5 |                5 |




Ques 1 : Find month of month revenue growth of zomato
-----------------------------------------------------

🧠 Logic (2 Steps Only)
........................
1️⃣ Aggregate total revenue per month
2️⃣ Use LAG() to compare current month revenue with previous month

👉 MoM Growth = current_month_revenue − previous_month_revenue



✅ Query Using Subquery
........................

SELECT month_name,
       current_month_revenue,
       previous_month_revenue,
       (current_month_revenue - previous_month_revenue) AS revenue_growth
FROM (
      SELECT 
             MONTHNAME(order_date) AS month_name,
             SUM(amount) AS current_month_revenue,
             LAG(SUM(amount)) OVER (
                 ORDER BY MONTH(order_date)
             ) AS previous_month_revenue
      FROM orders
      GROUP BY MONTH(order_date), MONTHNAME(order_date)
) t
ORDER BY MONTH(order_date);




🧩 Result Table (Final Answer)
...............................

| month_name | current_month_revenue | previous_month_revenue | revenue_growth |
| ---------- | --------------------- | ---------------------- | -------------- |
| January    | 120000                | NULL                   | NULL           |
| February   | 135000                | 120000                 | 15000          |
| March      | 160000                | 135000                 | 25000          |
| April      | 150000                | 160000                 | -10000         |










*/