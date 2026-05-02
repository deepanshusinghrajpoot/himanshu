/*



Usage with FROM
===============

⭐ MOST IMPORTANT (One-Line)
********************************
👉 When a subquery is used in the FROM clause, it acts as a temporary table (derived table) whose result can be queried like a normal table.




Question
________
Ques 1. Display average rating of all the restaurants.






Dataset is zomato about delevery
---------------------------------

1. users table(Sample Data - 10) :- Column : user_id, name, email, password
2. orders table(Sample Data - 10) :- Column : order_id, user_id, r_id, amount, date, partner_id, delivery_time, delivery_rating, restorant_rating
3. order_details(Sample Data - 10) :- Column : id, order_id, f_id 
4. food (Sample Data - 10) :- Column : f_id, f_name, type
5. menu(Sample Data - 10) :- Column : menu_id, r_id, f_id, price
6. delivery_partner :- Column : partner_id, partner_name
7. restuarants :- Column : r_id, f_name, gpt choose name(jst like row north indian food)






1️⃣ users table (Sample Data – 10)

| user_id | name   | email                                       | password |
| ------: | ------ | ------------------------------------------- | -------- |
|       1 | Amit   | [amit@gmail.com](mailto:amit@gmail.com)     | pass123  |
|       2 | Neha   | [neha@gmail.com](mailto:neha@gmail.com)     | pass123  |
|       3 | Rahul  | [rahul@gmail.com](mailto:rahul@gmail.com)   | pass123  |
|       4 | Priya  | [priya@gmail.com](mailto:priya@gmail.com)   | pass123  |
|       5 | Rohit  | [rohit@gmail.com](mailto:rohit@gmail.com)   | pass123  |
|       6 | Anjali | [anjali@gmail.com](mailto:anjali@gmail.com) | pass123  |
|       7 | Karan  | [karan@gmail.com](mailto:karan@gmail.com)   | pass123  |
|       8 | Sneha  | [sneha@gmail.com](mailto:sneha@gmail.com)   | pass123  |
|       9 | Arjun  | [arjun@gmail.com](mailto:arjun@gmail.com)   | pass123  |
|      10 | Pooja  | [pooja@gmail.com](mailto:pooja@gmail.com)   | pass123  |




2️⃣ delivery_partner table

| partner_id | partner_name |
| ---------: | ------------ |
|        101 | Ramesh       |
|        102 | Suresh       |
|        103 | Mahesh       |
|        104 | Rajesh       |
|        105 | Dinesh       |
|        106 | Mukesh       |
|        107 | Nitesh       |
|        108 | Akash        |
|        109 | Vikas        |
|        110 | Aman         |




3️⃣ food table (Sample Data – 10)

| f_id | f_name          | type    |
| ---: | --------------- | ------- |
|    1 | Pizza           | Veg     |
|    2 | Burger          | Veg     |
|    3 | Chicken Biryani | Non-Veg |
|    4 | Paneer Tikka    | Veg     |
|    5 | Fried Rice      | Veg     |
|    6 | Momos           | Veg     |
|    7 | Chicken Roll    | Non-Veg |
|    8 | Dosa            | Veg     |
|    9 | Ice Cream       | Veg     |
|   10 | Pasta           | Veg     |




4️⃣ menu table (Sample Data – 10)

| menu_id | r_id | f_id | price |
| ------: | ---: | ---: | ----: |
|       1 |  201 |    1 |   250 |
|       2 |  201 |    2 |   150 |
|       3 |  202 |    3 |   300 |
|       4 |  202 |    4 |   220 |
|       5 |  203 |    5 |   180 |
|       6 |  203 |    6 |   120 |
|       7 |  204 |    7 |   200 |
|       8 |  204 |    8 |   100 |
|       9 |  205 |    9 |    90 |
|      10 |  205 |   10 |   210 |




5️⃣ orders table (Sample Data – 10)

| order_id | user_id | r_id | amount | date       | partner_id | delivery_time | delivery_rating | restorant_rating |
| -------: | ------: | ---: | -----: | ---------- | ---------: | ------------: | --------------: | ---------------: |
|        1 |       1 |  201 |    250 | 2024-01-01 |        101 |            30 |               5 |                4 |
|        2 |       1 |  201 |    250 | 2024-01-03 |        102 |            28 |               4 |                4 |
|        3 |       1 |  201 |    250 | 2024-01-06 |        103 |            32 |               5 |                5 |
|        4 |       2 |  202 |    300 | 2024-01-02 |        104 |            35 |               4 |                5 |
|        5 |       2 |  202 |    300 | 2024-01-05 |        105 |            33 |               5 |                5 |
|        6 |       3 |  203 |    180 | 2024-01-03 |        106 |            25 |               5 |                4 |
|        7 |       4 |  204 |    200 | 2024-01-04 |        107 |            40 |               3 |                3 |
|        8 |       5 |  205 |     90 | 2024-01-05 |        108 |            20 |               5 |                5 |
|        9 |       6 |  201 |    150 | 2024-01-06 |        109 |            45 |               2 |                3 |
|       10 |       7 |  202 |    220 | 2024-01-07 |        110 |            38 |               4 |                4 |



6️⃣ order_details table (Sample Data – 10)

| id | order_id | f_id |                   |
| -: | -------: | ---: | ----------------- |
|  1 |        1 |    1 | ← Pizza           |
|  2 |        2 |    1 | ← Pizza           |
|  3 |        3 |    1 | ← Pizza           |
|  4 |        4 |    3 | ← Chicken Biryani |
|  5 |        5 |    3 | ← Chicken Biryani |
|  6 |        6 |    5 | ← Fried Rice      |
|  7 |        7 |    7 | ← Chicken Roll    |
|  8 |        8 |    9 | ← Ice Cream       |
|  9 |        9 |    2 | ← Burger          |
| 10 |       10 |    4 | ← Paneer Tikka    |


7️⃣ restaurants table

| r_id | r_name               | restaurant_type |
| ---: | -------------------- | --------------- |
|  201 | Spice Hub            | North Indian    |
|  202 | Royal Biryani House  | Biryani         |
|  203 | Veg Delight          | Pure Veg        |
|  204 | Street Food Junction | Fast Food       |
|  205 | Sweet & Treats       | Desserts        |





Ques 1. Display average rating of all the restaurants.
------------------------------------------------------

🧠 Logic
..........
1️⃣ Calculate average restaurant rating per restaurant from orders using GROUP BY.
2️⃣ Join this result with restaurants to get restaurant names.


✅ Final Query (Using INNER JOIN)
..................................

SELECT t2.r_id,
       t2.r_name,
       t1.avg_rating
FROM (
        SELECT r_id,
               AVG(restorant_rating) AS avg_rating
        FROM orders
        GROUP BY r_id
     ) t1
INNER JOIN restaurants t2
        ON t1.r_id = t2.r_id;


🧩 Sample Result Table
.......................

| r_id | r_name               | avg_rating |
| ---: | -------------------- | ---------: |
|  201 | Spice Hub            |        4.0 |
|  202 | Royal Biryani House  |       4.67 |
|  203 | Veg Delight          |        4.0 |
|  204 | Street Food Junction |        3.0 |
|  205 | Sweet & Treats       |        5.0 |










*/