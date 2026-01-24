import React from 'react'

/*



🔹 What is a Window Function?
-------------------------------

lll A window function performs calculations across a set of rows related to the current row, 
    without merging rows (unlike aggregate functions).


Syntax of window function
-------------------------

SELECT *,
        WINDOW_FUNCTION_NAME(....) OVER (PARTITION BY .... ORDER BY .... DESC)  AS .....,
FROM .......




Alternate way to write SQL query using Window Functions
-------------------------------------------------------

SELECT *,
        WINDOW_FUNCTION_NAME(....) OVER w AS .....,
FROM .......
WINDOW w AS (PARTITION BY .... ORDER BY .... DESC);






🔹 SQL Syntax Order (Query Writing Order)
------------------------------------------

Correct Order:

SELECT – choose columns or expressions from source table
DISTINCT – remove duplicate rows from source 
FROM – specify source table(s)
JOIN / ON – combine tables using conditions
WHERE – filter rows before gouping
GROUP BY – group rows of the source table
HAVING – filter row after gouping
ORDER BY – sort the final result.
LIMIT / TOP / OFFSET – restrict number of rows


lll ==================================== VVV.Imp =======================================================

SELECT  column...,
        WINDOW_FUNCTION_NAME OVER w AS xyz
FROM    ................
JOIN    ................
        ON ..................
WHERE   .................
GROUP BY ................
HAVING ..................
WINDOW  w AS (
                  PARTITION BY ....  
                  ORDER BY ....  
                  full-frame-use 
              )
ORDER BY ..............
LIMIT / TOP / OFFSET 

=============================================================================================


lll =================================== VVV.Imp ==================================================

🔹 SQL Logical Execution Order(How DB Executes)

Correct Order:

FROM – specify the source table(s).
JOIN / ON – apply joins between tables.
lll WHERE – filter rows (before grouping).
GROUP BY – group the filtered rows.
lll HAVING – filter groups (after grouping).
WINDOW FUNCTION
SELECT – choose the columns/expressions.
DISTINCT – remove duplicates from result set.
Aggregate Functions – SUM(), COUNT(), MIN(), MAX(), AVG(), GROUP_CONCAT() are applied here (inside SELECT).
ORDER BY – sort the final result.
LIMIT / TOP / OFFSET – return only required rows.


============================================================================================================













lll 🧠 ONE-FRAME MEMORY TABLE (🔥 Interview Gold)
--------------------------------------------------

| Category     | Functions                                     | ORDER BY     |
| ------------ | --------------------------------------------- | ------------ |
| Ranking      | ROW_NUMBER, RANK, DENSE_RANK, NTILE           | ✅ Mandatory |
| Navigation   | LAG, LEAD, FIRST_VALUE, LAST_VALUE, NTH_VALUE | ✅ Mandatory |
| Aggregate    | SUM, AVG, MIN, MAX, COUNT                     | ❌ Optional  |
| Distribution | PERCENT_RANK, CUME_DIST                       | ✅ Mandatory |





lll 🧠 ONE-FRAME MEMORY TABLE — PARTITION BY
---------------------------------------------

| Category         | Functions                                               | PARTITION BY                 |
| ---------------- | ------------------------------------------------------- | ---------------------------- |
| **Ranking**      | `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`             | ❌ Optional                   |
| **Navigation**   | `LAG`, `LEAD`, `FIRST_VALUE`, `LAST_VALUE`, `NTH_VALUE` | ❌ Optional (✔ Commonly Used) |
| **Aggregate**    | `SUM`, `AVG`, `MIN`, `MAX`, `COUNT`                     | ❌ Optional                   |
| **Distribution** | `PERCENT_RANK`, `CUME_DIST`                             | ❌ Optional                   |












✅ How two use window function to get desire result
-----------------------------------------------------

“A window function adds calculated columns to the existing result set.
These calculated columns can then be referenced using a subquery or CTE for filtering.”





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









Question :- Find movies with the 2nd highest score
--------------------------------------------------


✅ Example 1: Using CTE (Recommended / Readable)
.................................................

WITH ranked_movies AS (
    SELECT *,
           DENSE_RANK() OVER (ORDER BY score DESC) AS drn
    FROM movies
)

SELECT *
FROM ranked_movies
WHERE drn = 2;





✅ Example 2: Using Subquery (Compact)
.......................................

SELECT *
FROM (
      SELECT *,
             DENSE_RANK() OVER (ORDER BY score DESC) AS drn
      FROM movies
) ranked_movies
WHERE drn = 2;




🧩 Output (Same for both)
--------------------------

| name         | score |
| ------------ | ----- |
| Inception    | 8.8   |
| Forrest Gump | 8.8   |










 */






const Concept = () => {
  return (
    <div>Concept</div>
  )
}

export default Concept