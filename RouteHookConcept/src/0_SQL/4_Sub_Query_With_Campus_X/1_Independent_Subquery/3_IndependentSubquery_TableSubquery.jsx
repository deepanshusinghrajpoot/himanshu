/*



Independent Subquery - Table Subquery(Multiple Column With Multiple Row)
========================================================================

Ques 1. Find the most profitable movie of each year
Ques 2. Find the highest rated movie of each genre votes cutoff of 25000
Ques 3. Find the highest grossing movies of top 5 actor/director combo in terms of total gross income




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







1. Find the most profitable movie of each year
----------------------------------------------


Logic:
......
1️⃣ Find the maximum profit (gross − budget) for each year
2️⃣ Fetch the movie(s) whose profit equals that yearly maximum


✅ Correct Inner Query (Year-wise Max Profit):
.......................................

SELECT year, MAX(gross - budget) AS max_profit
FROM movies
GROUP BY year;


Inner Query Result:

| year | max_profit |
| ---- | ---------- |
| 1975 | 461        |
| 1977 | 764        |
| 1993 | 982        |
| 1997 | 2000       |
| 2000 | 357        |
| 2003 | 1048       |
| 2008 | 821        |
| 2009 | 2683       |
| 2010 | 669        |
| 2013 | 1134       |



✅ Final Query (Correct):
.........................

SELECT *
FROM movies m
WHERE (m.year, (m.gross - m.budget)) IN (
      SELECT year, MAX(gross - budget)
      FROM movies
      GROUP BY year
);


Result Table (Final Answer):
............................


| name                 | year | budget | gross | profit |
| -------------------- | ---- | ------ | ----- | ------ |
| Jaws                 | 1975 | 9      | 470   | 461    |
| Star Wars            | 1977 | 11     | 775   | 764    |
| Jurassic Park        | 1993 | 63     | 1045  | 982    |
| Titanic              | 1997 | 200    | 2200  | 2000   |
| Gladiator            | 2000 | 103    | 460   | 357    |
| LOTR: Return of King | 2003 | 94     | 1142  | 1048   |
| The Dark Knight      | 2008 | 185    | 1006  | 821    |
| Avatar               | 2009 | 237    | 2920  | 2683   |
| Inception            | 2010 | 160    | 829   | 669    |
| Frozen               | 2013 | 150    | 1284  | 1134   |







Ques 2. Find the highest rated movie of each genre votes cutoff of 25000
-------------------------------------------------------------------------

Logic:
......
1️⃣ Filter movies with votes > 25000
2️⃣ Find the highest rated movie for each genre among them


✅ Correct Inner Query (Genre-wise Max Score):
.......................................

SELECT genre, MAX(score) AS max_score
FROM movies
WHERE votes > 25000
GROUP BY genre;


Inner Query Result:

| genre   | max_score |
| ------- | --------- |
| Action  | 9.0       |
| Sci-Fi  | 8.8       |
| Romance | 7.9       |



✅ Final Query (Correct):
.........................

SELECT *
FROM movies
WHERE (genre, score) IN (
      SELECT genre, MAX(score)
      FROM movies
      WHERE votes > 25000
      GROUP BY genre
)
AND votes > 25000;



Result Table (Final Answer):
............................

| name            | genre   | year | released | score | votes | director | writer  | star | country | budget | gross | profit |
| --------------- | ------- | ---- | -------- | ----- | ----- | -------- | ------- | ---- | ------- | ------ | ----- | ------ |
| The Dark Knight | Action  | 2008 | Yes      | 9.0   | 26000 | Nolan    | Nolan   | Bale | USA     | 185    | 1006  | 821    |
| Inception       | Sci-Fi  | 2010 | Yes      | 8.8   | 20000 | Nolan    | Nolan   | Leo  | USA     | 160    | 829   | 669    |
| Titanic         | Romance | 1997 | Yes      | 7.9   | 18000 | Cameron  | Cameron | Leo  | USA     | 200    | 2200  | 2000   |








Ques 3. Find the highest grossing movies of top 5 actor/director combo (by total gross)
----------------------------------------------------------------------------------------

Logic:
1️⃣ Calculate total gross per actor/director combo and select top 5 combos.
2️⃣ For each top combo, select the highest grossing movie.




✅ Final Query (Using INNER JOIN)
..................................

Note :- When you use LIMIT in your query then NOT use that table as inner subquery


WITH TopCombos AS (
    SELECT star, director, SUM(gross) AS total_gross
    FROM movies
    GROUP BY star, director
    ORDER BY total_gross DESC
    LIMIT 5
)

SELECT m.star, m.director, m.name AS movie_name, m.gross
FROM movies m
INNER JOIN TopCombos t
    ON m.star = t.star AND m.director = t.director
WHERE m.gross = (
    SELECT MAX(gross)
    FROM movies
    WHERE star = m.star AND director = m.director
)
ORDER BY t.total_gross DESC;




✅ Sample Result Table
.......................

| star | director  | movie_name        | gross |
| ---- | --------- | ----------------- | ----- |
| Sam  | Cameron   | Avatar            | 2920  |
| RDJ  | Russo     | Avengers: Endgame | 2798  |
| Leo  | Cameron   | Titanic           | 2200  |
| Sam  | Spielberg | Jurassic Park     | 1045  |
| Leo  | Nolan     | Inception         | 829   |







*/



