

/*



Corelated Subquery
==================

Ques 1. Find all the movies that have a rating higher than the average rating of movies
        in the same genre.[Animation]
Ques 2. Find the favorite food of each customer.





Movies Table (Sample Data – 20 Rows)

| name                 | rating | genre     | year | released | score | votes | director  | writer   | star        | country | budget | gross | company    | runtime |
| -------------------- | ------ | --------- | ---- | -------- | ----- | ----- | --------- | -------- | ----------- | ------- | ------ | ----- | ---------- | ------- |
| Inception            | PG-13  | Sci-Fi    | 2010 | Yes      | 8.8   | 20000 | Nolan     | Nolan    | Leo         | USA     | 160    | 829   | WB         | 148     |
| Titanic              | PG-13  | Romance   | 1997 | Yes      | 7.9   | 18000 | Cameron   | Cameron  | Leo         | USA     | 200    | 2200  | Fox        | 195     |
| Avatar               | PG-13  | Sci-Fi    | 2009 | Yes      | 7.8   | 21000 | Cameron   | Cameron  | Sam         | USA     | 237    | 2920  | Fox        | 162     |
| Avengers: Endgame    | PG-13  | Action    | 2019 | Yes      | 8.4   | 25000 | Russo     | Markus   | RDJ         | USA     | 356    | 2798  | Marvel     | 181     |
| Jurassic Park        | PG     | Adventure | 1993 | Yes      | 8.1   | 15000 | Spielberg | Crichton | Sam         | USA     | 63     | 1045  | Universal  | 127     |
| The Dark Knight      | PG-13  | Action    | 2008 | Yes      | 9.0   | 26000 | Nolan     | Nolan    | Bale        | USA     | 185    | 1006  | WB         | 152     |
| Forrest Gump         | PG-13  | Drama     | 1994 | Yes      | 8.8   | 17000 | Zemeckis  | Roth     | Hanks       | USA     | 55     | 678   | Paramount  | 142     |
| Joker                | R      | Crime     | 2019 | Yes      | 8.5   | 23000 | Phillips  | Phillips | Phoenix     | USA     | 55     | 1074  | WB         | 122     |
| Interstellar         | PG-13  | Sci-Fi    | 2014 | Yes      | 8.6   | 19000 | Nolan     | Nolan    | McConaughey | USA     | 165    | 677   | Paramount  | 169     |
| Gladiator            | R      | Action    | 2000 | Yes      | 8.5   | 16000 | Scott     | Franzoni | Crowe       | USA     | 103    | 460   | DreamWorks | 155     |
| Spider-Man           | PG-13  | Action    | 2002 | Yes      | 7.4   | 14000 | Raimi     | Koepp    | Maguire     | USA     | 139    | 825   | Sony       | 121     |
| Iron Man             | PG-13  | Action    | 2008 | Yes      | 7.9   | 15500 | Favreau   | Favreau  | RDJ         | USA     | 140    | 585   | Marvel     | 126     |
| Toy Story            | G      | Animation | 1995 | Yes      | 8.3   | 12000 | Lasseter  | Lasseter | Hanks       | USA     | 30     | 373   | Pixar      | 81      |
| Frozen               | PG     | Animation | 2013 | Yes      | 7.5   | 16000 | Buck      | Lee      | Bell        | USA     | 150    | 1284  | Disney     | 102     |
| Lion King            | G      | Animation | 1994 | Yes      | 8.5   | 18000 | Allers    | Minkoff  | Broderick   | USA     | 45     | 968   | Disney     | 88      |
| Black Panther        | PG-13  | Action    | 2018 | Yes      | 7.3   | 20000 | Coogler   | Coogler  | Boseman     | USA     | 200    | 1347  | Marvel     | 134     |
| Harry Potter 1       | PG     | Fantasy   | 2001 | Yes      | 7.6   | 19000 | Columbus  | Rowling  | Radcliffe   | UK      | 125    | 974   | WB         | 152     |
| LOTR: Return of King | PG-13  | Fantasy   | 2003 | Yes      | 9.0   | 22000 | Jackson   | Tolkien  | Wood        | NZ      | 94     | 1142  | New Line   | 201     |
| Star Wars            | PG     | Sci-Fi    | 1977 | Yes      | 8.6   | 21000 | Lucas     | Lucas    | Hamill      | USA     | 11     | 775   | Lucasfilm  | 121     |
| Jaws                 | PG     | Thriller  | 1975 | Yes      | 8.1   | 13000 | Spielberg | Benchley | Scheider    | USA     | 9      | 470   | Universal  | 124     |





Ques 1. Find all the movies that have a rating higher than the average rating of movies
        in the same genre [Animation]
----------------------------------------------------------------------------------------

🧠 Logic (2 Steps Only)
........................
1️⃣ Calculate the average score of movies genre-wise using a correlated subquery
2️⃣ Select movies whose score is greater than their genre’s average score



✅ Final Query (Correct)
.........................

SELECT *
FROM movies m1
WHERE score > ( 
                SELECT AVG(score)
                FROM movies m2
                WHERE m1.genre = m2.genre
              )
AND genre = 'Animation';



🧩 Result Table (Final Answer)
...............................

| name      | rating | genre     | year | score |
| --------- | ------ | --------- | ---- | ----- |
| Toy Story | G      | Animation | 1995 | 8.3   |
| Lion King | G      | Animation | 1994 | 8.5   |















Dataset is zomato about delevery
---------------------------------

1. users table(Sample Data - 10) :- Column : user_id, name, email, password
2. orders table(Sample Data - 10) :- Column : order_id, user_id, r_id, amount, date, partner_id, delivery_time, delivery_rating, restorant_rating
3. order_details(Sample Data - 10) :- Column : id, order_id, f_id 
4. food (Sample Data - 10) :- Column : f_id, f_name, type
5. menu(Sample Data - 10) :- Column : menu_id, r_id, f_id, price
6. delivery_partner :- Column : partner_id, partner_name






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





Ques 2. Find the favorite food of each customer.
------------------------------------------------

🧠 Logic
.........

1️⃣ Join users → orders → order_details → food
2️⃣ Count how many times each user ordered each food
3️⃣ Select the food with maximum frequency per user



✅ Final Query (Corrected & Valid)
....................................

WITH favorite_food AS (
    SELECT 
        o1.user_id,
        u1.name AS user_name,
        f1.f_name,
        COUNT(*) AS frequency
    FROM users u1
    INNER JOIN orders o1 ON u1.user_id = o1.user_id
    INNER JOIN order_details od1 ON o1.order_id = od1.order_id
    INNER JOIN food f1 ON f1.f_id = od1.f_id
    GROUP BY o1.user_id, u1.name, od1.f_id, f1.f_name
)

SELECT user_id, user_name, f_name, frequency
FROM favorite_food m1
WHERE frequency = (
    SELECT MAX(frequency)
    FROM favorite_food m2
    WHERE m1.user_id = m2.user_id
);


📊 Result of CTE (favorite_food)
....................................

| user_id | user_name | f_name          | frequency |
| ------: | --------- | --------------- | --------: |
|       1 | Amit      | Pizza           |         3 |
|       2 | Neha      | Chicken Biryani |         2 |
|       3 | Rahul     | Fried Rice      |         1 |
|       4 | Priya     | Chicken Roll    |         1 |
|       5 | Rohit     | Ice Cream       |         1 |
|       6 | Anjali    | Burger          |         1 |
|       7 | Karan     | Paneer Tikka    |         1 |


🟢 Result Table (Final Answer)
...............................

| user_id | user_name | f_name          | frequency |
| ------: | --------- | --------------- | --------: |
|       1 | Amit      | Pizza           |         3 |
|       2 | Neha      | Chicken Biryani |         2 |
|       3 | Rahul     | Fried Rice      |         1 |
|       4 | Priya     | Chicken Roll    |         1 |
|       5 | Rohit     | Ice Cream       |         1 |
|       6 | Anjali    | Burger          |         1 |
|       7 | Karan     | Paneer Tikka    |         1 |





*/


















