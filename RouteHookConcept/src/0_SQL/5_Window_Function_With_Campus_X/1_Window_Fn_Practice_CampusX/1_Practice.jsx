

/*



++++++++++++++++++++ Practice window function (ROW_NUMBER(), RANK(), DENSE_RANK()) ++++++++++++++++++++++++++++++++++++
___________________________________________________________________________________________________________




🎓 Student Table (Parent Table – Sample Data)

Table name: students

| student_id | name    | branch | marks |
| ---------- | ------- | ------ | ----- |
| 101        | Rahul   | CSE    | 85    |
| 102        | Anjali  | CSE    | 92    |
| 103        | Amit    | ECE    | 78    |
| 104        | Neha    | ECE    | 88    |
| 105        | Rohit   | ME     | 74    |
| 106        | Priya   | ME     | 81    |
| 107        | Karan   | CSE    | 90    |
| 108        | Pooja   | IT     | 95    |
| 109        | Arjun   | IT     | 89    |
| 110        | Sneha   | ECE    | 82    |
| 111        | Rakesh  | ME     | 69    |
| 112        | Kavita  | CSE    | 88    |
| 113        | Mohit   | IT     | 76    |
| 114        | Nisha   | CSE    | 91    |
| 115        | Aman    | ME     | 85    |
| 116        | Deepak  | ECE    | 90    |
| 117        | Shalini | IT     | 84    |
| 118        | Varun   | CSE    | 78    |
| 119        | Simran  | ME     | 88    |
| 120        | Akash   | ECE    | 95    |







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


 




Ques 1 : Find top 2 most paying customers of each month
-------------------------------------------------------




🧠 Logic (2 Steps Only)
........................
1️⃣ Calculate total amount spent by each user per month
2️⃣ Rank users month-wise by total spending and filter top 2



✅ Query Using Subquery
.........................

SELECT *
FROM (
    SELECT 
        MONTHNAME(date) AS month_name,
        user_id,
        SUM(amount) AS total_exp,
        RANK() OVER (PARTITION BY MONTHNAME(date) ORDER BY SUM(amount) DESC) AS rn
    FROM orders
    GROUP BY MONTHNAME(date), user_id
) t
WHERE rn <= 2
ORDER BY month_name, rn;



🧩 Result Table (Final Answer)
...............................

| month_name | user_id | total_exp | rn |
| ---------- | ------: | --------: | -: |
| January    |       7 |       600 |  1 |
| January    |       2 |       520 |  2 |








*/