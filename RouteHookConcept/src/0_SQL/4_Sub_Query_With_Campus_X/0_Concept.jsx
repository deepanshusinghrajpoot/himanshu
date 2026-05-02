


/*






=========== SUBQUERY ===========

lll Definition:
---------------
A subquery is a query written inside another SQL query.
It is also called a nested query.


When We Apply Subquery:
-----------------------
         lll A subquery is used when:
                     A problem has more than one logical step
                     The result of one query is needed by another query



Example: Find the movie with the highest rating
...............................................

This problem has two parts:

1️⃣ Find the highest rating
2️⃣ Find the movie having that rating


Inner Query (Subquery):  SELECT MAX(score)
                         FROM movies;


✔ Finds the highest score from the table.

Outer Query:  SELECT *
              FROM movies
              WHERE score = (SELECT MAX(score) FROM movies);


✔ Uses the result of the inner query.






lll Order of Execution:
-----------------------
1️⃣ First executes Inner query
2️⃣ Then executesOuter query 







Parent Table: movies

| name         | rating | genre   | year | released | score | votes | director | writer  | star | country | budget | gross | company   | runtime |
| ------------ | ------ | ------- | ---- | -------- | ----- | ----- | -------- | ------- | ---- | ------- | ------ | ----- | --------- | ------- |
| Inception    | PG-13  | Sci-Fi  | 2010 | Yes      | 8.8   | 20000 | Nolan    | Nolan   | Leo  | USA     | 160M   | 829M  | WB        | 148     |
| Titanic      | PG-13  | Romance | 1997 | Yes      | 7.9   | 18000 | Cameron  | Cameron | Leo  | USA     | 200M   | 2200M | Fox       | 195     |
| Interstellar | PG-13  | Sci-Fi  | 2014 | Yes      | 8.6   | 17000 | Nolan    | Nolan   | Matt | USA     | 165M   | 677M  | Paramount | 169     |


Query (Corrected):  SELECT *
                    FROM movies
                    WHERE score = (SELECT MAX(score) FROM movies);


Result Table:

| name      | rating | genre  | year | released | score | votes | director | writer | star | country | budget | gross | company | runtime |
| --------- | ------ | ------ | ---- | -------- | ----- | ----- | -------- | ------ | ---- | ------- | ------ | ----- | ------- | ------- |
| Inception | PG-13  | Sci-Fi | 2010 | Yes      | 8.8   | 20000 | Nolan    | Nolan  | Leo  | USA     | 160M   | 829M  | WB      | 148     |

















=========== TYPES OF SUBQUERY ===========

lll Based On
------------
1️⃣ Based on subquery return result
2️⃣ Based on execution




lll Type 1:- Based on Subquery Return Result
--------------------------------------------
They are divided into three types


(1). Scalar Subquery
....................

Definition: Here the inner query returns only a single scalar value
            (one row and one column).


SELECT *
FROM movies
WHERE score = (SELECT MAX(score) FROM movies);



(2). Row Subquery
.................

Definition: Here the inner query returns multiple rows but only one column.


SELECT *
FROM movies
WHERE score IN (SELECT score FROM movies WHERE year = 2023);



(3). Table Subquery
...................

Definition: Here the inner query returns a table with multiple rows and multiple columns.


SELECT *
FROM movies
WHERE (genre, score) IN (
      SELECT genre, MAX(score)
      FROM movies
      WHERE votes > 25000
      GROUP BY genre
)
AND votes > 25000;






lll Type 2:- Based on Execution
-------------------------------
They are divided into two types


(1). Independent Subquery
.........................

Definition: Here the inner query does not depend on the outer query.
            It can execute independently.


SELECT *
FROM movies
WHERE score > (SELECT AVG(score) FROM movies);



(2). Correlated Subquery
........................

Definition: Here the inner query depends on the outer query.
            It executes once for each row of the outer query.


            
SELECT name, score
FROM movies m1
WHERE score > (
    SELECT AVG(score)
    FROM movies m2
    WHERE m2.genre = m1.genre
);




    


=========== WHERE WE CAN USE SUBQUERY ===========

SUBQUERY
│
├── With DML Statements
│   │
│   ├── INSERT
│   │
│   ├── SELECT
│   │
│   ├── UPDATE
│   │
│   └── DELETE
│
└── With SELECT Statement Clauses
    │
    ├── SELECT   → Scalar subquery
    │
    ├── FROM     → Table subquery
    │
    ├── WHERE    → Filtering using subquery
    │
    └── HAVING   → Filtering aggregated data










*/