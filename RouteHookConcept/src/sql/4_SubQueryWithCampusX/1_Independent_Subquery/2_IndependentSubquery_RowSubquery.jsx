
/*



Independent Subquery - Row Subquery(One Column With Multiple Rows)
==================================================================

Ques(1):- Find all users who never ordered
Ques(2):- Find all movies made by top directors(in terms of total gross income)
Ques(3):- Find all movies of all those actors whose filmography's avg rating > 8.5(take 25000 vots as cutoff)




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




6️⃣ order_details table (Sample Data – 10)

| id | order_id | f_id |
| -: | -------: | ---: |
|  1 |        1 |    1 |
|  2 |        2 |    3 |
|  3 |        3 |    5 |
|  4 |        4 |    7 |
|  5 |        5 |    9 |
|  6 |        6 |    2 |
|  7 |        7 |    4 |
|  8 |        8 |    6 |
|  9 |        9 |    8 |
| 10 |       10 |   10 |






Ques(1):- Find all users who never ordered
------------------------------------------

Logic:
......
1️⃣ Find users who have placed at least one order
2️⃣ Find users who do NOT belong to that list

Inner Query:
............

SELECT DISTINCT user_id
FROM orders;


Final Query (Correct ✅):
.........................

SELECT uu.*
FROM users uu
WHERE uu.user_id NOT IN (
      SELECT DISTINCT user_id
      FROM orders
);


Alternate Approach (Using JOIN):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SELECT *
FROM users uu
WHERE uu.user_id NOT IN (
      SELECT u.user_id
      FROM users u
      INNER JOIN orders o
              ON u.user_id = o.user_id
);



Result Table (Final Answer):
............................

No rows returned
| user_id | name | email | password |
| ------: | ---- | ----- | -------- |
|       — | —    | —     | —        |































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







Ques(2):- Find all movies made by top directors(in terms of total gross income)
-------------------------------------------------------------------------------

Logic:
......
1️⃣ Find top directors based on total gross income
2️⃣ Find all movies made by those directors



✅ Correct Inner Query (Top Directors):
.......................................
SELECT director
FROM movies
GROUP BY director
ORDER BY SUM(gross) DESC
LIMIT 3;


✅ Final Query (Correct):
.........................
SELECT *
FROM movies
WHERE director IN (
      SELECT director
      FROM movies
      GROUP BY director
      ORDER BY SUM(gross) DESC
      LIMIT 3
);


Director-wise Total Gross (From Dataset)
........................................

| Director | Total Gross |
| -------- | ----------- |
| Cameron  | 5120        |
| Russo    | 2798        |
| Nolan    | 2512        |

✅ Top 3 Directors:
Cameron, Russo, Nolan




Result Table (Final Answer):
............................

| name              | rating | genre   | year | released | score | votes | director | writer  | star        | country | budget | gross | company   | runtime |
| ----------------- | ------ | ------- | ---- | -------- | ----- | ----- | -------- | ------- | ----------- | ------- | ------ | ----- | --------- | ------- |
| Titanic           | PG-13  | Romance | 1997 | Yes      | 7.9   | 18000 | Cameron  | Cameron | Leo         | USA     | 200    | 2200  | Fox       | 195     |
| Avatar            | PG-13  | Sci-Fi  | 2009 | Yes      | 7.8   | 21000 | Cameron  | Cameron | Sam         | USA     | 237    | 2920  | Fox       | 162     |
| Avengers: Endgame | PG-13  | Action  | 2019 | Yes      | 8.4   | 25000 | Russo    | Markus  | RDJ         | USA     | 356    | 2798  | Marvel    | 181     |
| Inception         | PG-13  | Sci-Fi  | 2010 | Yes      | 8.8   | 20000 | Nolan    | Nolan   | Leo         | USA     | 160    | 829   | WB        | 148     |
| The Dark Knight   | PG-13  | Action  | 2008 | Yes      | 9.0   | 26000 | Nolan    | Nolan   | Bale        | USA     | 185    | 1006  | WB        | 152     |
| Interstellar      | PG-13  | Sci-Fi  | 2014 | Yes      | 8.6   | 19000 | Nolan    | Nolan   | McConaughey | USA     | 165    | 677   | Paramount | 169     |








Ques(3):- Find all movies of all those actors whose filmography's avg rating > 8.5(take 25000 vots as cutoff)
-------------------------------------------------------------------------------------------------------------

Logic:
......
1️⃣ Find stars with votes > 25000 whose average rating > 8.5
2️⃣ Fetch all movies of those stars



✅ Correct Inner Query (Qualified Stars):
.......................................

SELECT star
FROM movies
WHERE votes > 25000
GROUP BY star
HAVING AVG(score) > 8.5;




✅ Final Query (Correct):
.........................

SELECT *
FROM movies
WHERE star IN (
      SELECT star
      FROM movies
      WHERE votes > 25000
      GROUP BY star
      HAVING AVG(score) > 8.5
);



Dataset Validation 🔍
..................
Movies with votes > 25000:

| name            | star | votes | score |
| --------------- | ---- | ----- | ----- |
| The Dark Knight | Bale | 26000 | 9.0   |



Result Table (Final Answer):
............................

| name            | rating | genre  | year | released | score | votes | director | writer | star | country | budget | gross | company | runtime |
| --------------- | ------ | ------ | ---- | -------- | ----- | ----- | -------- | ------ | ---- | ------- | ------ | ----- | ------- | ------- |
| The Dark Knight | PG-13  | Action | 2008 | Yes      | 9.0   | 26000 | Nolan    | Nolan  | Bale | USA     | 185    | 1006  | WB      | 152     |








*/