

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







Ques 1 : Find the branch toppers
--------------------------------

🧠 Logic (2 Steps Only)

........................
1️⃣ Add maximum marks of each branch using a window function
2️⃣ Filter students whose marks equal the branch maximum



✅ Query Using Subquery
........................

SELECT *
FROM (
      SELECT *,
             MAX(marks) OVER (PARTITION BY branch) AS max_marks
      FROM students
     ) s
WHERE marks = max_marks;



🧩 Result Table (Final Answer)
...............................

| student_id | name   | branch | marks | max_marks |
| ---------- | ------ | ------ | ----- | --------- |
| 3          | Rahul  | CSE    | 92    | 92        |
| 6          | Anjali | ECE    | 89    | 89        |
| 9          | Arjun  | ME     | 85    | 85        |







Ques 2 : Find the last guy of each branch according to marks
------------------------------------------------------------



🧠 Logic (2 Steps Only)
........................
1️⃣ Sort students branch-wise by marks in descending order
2️⃣ Use LAST_VALUE() with a full window frame to get lowest marks and filter



✅ Query Using Subquery
........................

SELECT *
FROM (
      SELECT *,
             LAST_VALUE(marks) OVER (
                 PARTITION BY branch
                 ORDER BY marks DESC
                 RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
             ) AS last_guy
      FROM students
     ) s
WHERE marks = last_guy;



🧩 Result Table (Final Answer)
...............................

| student_id | name  | branch | marks | last_guy |
| ---------- | ----- | ------ | ----- | -------- |
| 4          | Priya | CSE    | 45    | 45       |
| 7          | Karan | ECE    | 50    | 50       |
| 10         | Pooja | ME     | 48    | 48       |





How To Write Window Function Alternative way
_____________________________________________



Ques 3 : Find the 2nd last guy of each branch, 5th topper of each branch according to marks
-------------------------------------------------------------------------------------------

🧠 Logic (2 Steps Only)
........................
1️⃣ Order students branch-wise by marks (ASC for last guys, DESC for toppers)
2️⃣ Use NTH_VALUE() with full window frame and filter matching rows



✅ Query Using Subquery
........................

SELECT t.name, t.branch, t.marks
FROM (
      SELECT s.*,
             NTH_VALUE(marks, 2) OVER w_ase AS second_last_guy_marks,

             NTH_VALUE(marks, 5) OVER w_desc AS fifth_topper_marks
      FROM students s
      WINDOW w_ase (
                     PARTITION BY branch
                     ORDER BY marks ASC
                     RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
                   ),
             w_desc (
                     PARTITION BY branch
                     ORDER BY marks DESC
                     RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
                   )

     ) t
WHERE t.marks = t.second_last_guy_marks
   OR t.marks = t.fifth_topper_marks;




🧩 Result Table (Final Answer)
...............................

| name  | branch | marks |                |
| ----- | ------ | ----- | -------------- |
| Aman  | CSE    | 50    | ← 2nd last guy |
| Rohit | CSE    | 72    | ← 5th topper   |
| Karan | ECE    | 55    | ← 2nd last guy |
| Neha  | ECE    | 70    | ← 5th topper   |






*/