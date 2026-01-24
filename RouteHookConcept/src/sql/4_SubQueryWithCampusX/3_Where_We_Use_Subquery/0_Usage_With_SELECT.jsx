/*





Usage with SELECT
==================


⭐ MOST IMPORTANT (One-Line)
********************************
A subquery in the SELECT clause must be a scalar subquery 
that mean it should return exactly one value (one row, one column), otherwise SQL throws an error.


Note:- Avoid correlated subquery in SELECT → runs per row → slow.



Question
________
Ques 1. Display all movie names, genre, score and avg(score) of genre.
Ques 2. Get the percentage of votes for each movie compared to the total number of votes.





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









Ques 1. Display all movie names, genre, score and avg(score) of genre.
----------------------------------------------------------------------

🧠 Logic (2 Steps Only)
........................
1️⃣ For each movie, calculate the average score of its genre using a correlated subquery  
2️⃣ Display movie details along with the calculated genre-wise average score



✅ Final Query (Correct – Using Correlated Subquery)
....................................................

SELECT 
       name,
       genre,
       score,
       (SELECT AVG(score)
        FROM movies m1
        WHERE m1.genre = m2.genre) AS avg_score_genre
FROM movies m2;



🧩 Sample Result Table (Final Answer)
....................................

| name              | genre     | score | avg_score_genre |
|-------------------|-----------|------:|----------------:|
| Toy Story         | Animation | 8.3   | 8.1             |
| Frozen            | Animation | 7.5   | 8.1             |
| Lion King         | Animation | 8.5   | 8.1             |
| Inception         | Sci-Fi    | 8.8   | 8.45            |
| Avatar            | Sci-Fi    | 7.8   | 8.45            |
| Interstellar      | Sci-Fi    | 8.6   | 8.45            |
| Star Wars         | Sci-Fi    | 8.6   | 8.45            |
| Avengers: Endgame | Action    | 8.4   | 8.08            |
| The Dark Knight   | Action    | 9.0   | 8.08            |
| Iron Man          | Action    | 7.9   | 8.08            |

📌 Note:
- `avg_score_genre` repeats for movies of the same genre  
- This confirms the subquery runs **per row (correlated subquery)**  





Ques 2. Get the percentage of votes for each movie compared to the total number of votes.
-----------------------------------------------------------------------------------------

🧠 Logic
.........
1️⃣ Calculate total votes of all movies
2️⃣ For each movie → (movie_votes / total_votes) * 100



✅ Final Query (Correct)
.........................

SELECT 
    name,
    votes,
    ROUND(votes * 100.0 / (SELECT SUM(votes) FROM movies), 2) 
        AS vote_percentage
FROM movies;

🧮 Total Votes Calculation (from given data)
Total Votes = 370,500



📊 Result Table (Final Answer)
....................................

| Movie Name           | Votes | Vote % |
| -------------------- | ----: | -----: |
| Inception            | 20000 |   5.40 |
| Titanic              | 18000 |   4.86 |
| Avatar               | 21000 |   5.67 |
| Avengers: Endgame    | 25000 |   6.75 |
| Jurassic Park        | 15000 |   4.05 |
| The Dark Knight      | 26000 |   7.02 |
| Forrest Gump         | 17000 |   4.59 |
| Joker                | 23000 |   6.21 |
| Interstellar         | 19000 |   5.13 |
| Gladiator            | 16000 |   4.32 |
| Spider-Man           | 14000 |   3.78 |
| Iron Man             | 15500 |   4.18 |
| Toy Story            | 12000 |   3.24 |
| Frozen               | 16000 |   4.32 |
| Lion King            | 18000 |   4.86 |
| Black Panther        | 20000 |   5.40 |
| Harry Potter 1       | 19000 |   5.13 |
| LOTR: Return of King | 22000 |   5.94 |
| Star Wars            | 21000 |   5.67 |
| Jaws                 | 13000 |   3.51 |













*/