
/*



Independent Subquery - Scalary Subquery
---------------------------------------


Ques(1):- Find the movie with heighest profit
Ques(2):- Find how many movies have a rating > the avg of all the movie ratings(Find the count of above average movies)
Ques(3):- Find the heighest rated movie of 2000
Ques(4):- Find the heighest rated movie among all movies whose number of votes are > the dataset avg votes





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




Ques(1):- Find the movie with heighest profit
---------------------------------------------


Logic:
......
1️⃣ Find the highest profit
2️⃣ Find the movie with that profit


Inner Query:
............
SELECT MAX(gross - budget)
FROM movies;


Final Query (Correct ✅):
.........................
SELECT *
FROM movies
WHERE (gross - budget) = (
      SELECT MAX(gross - budget)
      FROM movies
);




Result Table (Final Answer)
...........................

| name   | rating | genre  | year | released | score | votes | director | writer  | star | country | budget | gross | company | runtime |
| ------ | ------ | ------ | ---- | -------- | ----- | ----- | -------- | ------- | ---- | ------- | ------ | ----- | ------- | ------- |
| Avatar | PG-13  | Sci-Fi | 2009 | Yes      | 7.8   | 21000 | Cameron  | Cameron | Sam  | USA     | 237    | 2920  | Fox     | 162     |






Ques(2):- Find how many movies have a rating > the avg of all the movie ratings(Find the count of above average movies)
-----------------------------------------------------------------------------------------------------------------------

Logic:
......
1️⃣ First find the average rating of all movies
2️⃣ Then count movies having rating greater than the average


Inner Query:
............

SELECT AVG(score)
FROM movies;


Final Query (Correct ✅):
.........................

SELECT COUNT(*)
FROM movies
WHERE score > (
      SELECT AVG(score)
      FROM movies
);




Result Table:
............

| count |
| ----: |
|    11 |








Ques(3):- Find the heighest rated movie of 2000
-----------------------------------------------

Logic:
......
1️⃣ First find the highest rating in year 2000
2️⃣ Then find the movie of year 2000 having that rating


Inner Query:
............
SELECT MAX(score)
FROM movies
WHERE year = 2000;


Final Query (Correct ✅):
.........................
SELECT *
FROM movies
WHERE year = 2000
AND score = (
      SELECT MAX(score)
      FROM movies
      WHERE year = 2000
);


Result Table:
.............

| name      | rating | genre  | year | released | score | votes | director | writer   | star  | country | budget | gross | company    | runtime |
| --------- | ------ | ------ | ---- | -------- | ----- | ----- | -------- | -------- | ----- | ------- | ------ | ----- | ---------- | ------- |
| Gladiator | R      | Action | 2000 | Yes      | 8.5   | 16000 | Scott    | Franzoni | Crowe | USA     | 103    | 460   | DreamWorks | 155     |








Ques(4):- Find the heighest rated movie among all movies whose number of votes are > the dataset avg votes
----------------------------------------------------------------------------------------------------------

Logic:
......
1️⃣ Find the average votes from all movies
2️⃣ From movies having votes > average votes, find the maximum rating
3️⃣ Fetch the movie(s) having that rating


Inner Query 1 (Average Votes):
..............................

SELECT AVG(votes)
FROM movies;



Inner Query 2 (Max Score where votes > avg):
............................................

SELECT MAX(score)
FROM movies
WHERE votes > (
      SELECT AVG(votes)
      FROM movies
);



Final Query (Correct ✅):
.........................

SELECT *
FROM movies
WHERE score = (
      SELECT MAX(score)
      FROM movies
      WHERE votes > (
            SELECT AVG(votes)
            FROM movies
      )
);



Result Table:
.............

| name                 | rating | genre   | year | released | score | votes | director | writer  | star | country | budget | gross | company  | runtime |
| -------------------- | ------ | ------- | ---- | -------- | ----- | ----- | -------- | ------- | ---- | ------- | ------ | ----- | -------- | ------- |
| The Dark Knight      | PG-13  | Action  | 2008 | Yes      | 9.0   | 26000 | Nolan    | Nolan   | Bale | USA     | 185    | 1006  | WB       | 152     |
| LOTR: Return of King | PG-13  | Fantasy | 2003 | Yes      | 9.0   | 22000 | Jackson  | Tolkien | Wood | NZ      | 94     | 1142  | New Line | 201     |











*/