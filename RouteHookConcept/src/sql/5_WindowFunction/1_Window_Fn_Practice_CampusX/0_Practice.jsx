
/*




++++++++++++++++++++ Practice window function using aggregate function ++++++++++++++++++++++++++++++++++++
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






Ques 1 : Find all the students who have marks higher than the avg marks of their respective branch
--------------------------------------------------------------------------------------------------


🧠 Logic (2 Steps Only)
........................
1️⃣ Compute the branch-wise average marks for each student using a window function
2️⃣ Filter students whose marks are greater than the branch average



✅ Query Using CTE
...................

WITH student_col_avg AS (
    SELECT *,
           AVG(marks) OVER (PARTITION BY branch) AS avg_mark
    FROM students
)
SELECT *
FROM student_col_avg
WHERE marks > avg_mark;




✅ Query Using Subquery
........................

SELECT *
FROM (
      SELECT *,
             AVG(marks) OVER (PARTITION BY branch) AS avg_mark
      FROM students
) student_col_avg
WHERE marks > avg_mark;




🧩 Result Table (Final Answer)
...............................

| student_id | name   | branch | marks | avg_mark |
| ---------- | ------ | ------ | ----- | -------- |
| 102        | Anjali | CSE    | 92    | 86.4     |
| 107        | Karan  | CSE    | 90    | 86.4     |
| 114        | Nisha  | CSE    | 91    | 86.4     |
| 108        | Pooja  | IT     | 95    | 86.0     |
| 109        | Arjun  | IT     | 89    | 86.0     |
| 116        | Deepak | ECE    | 90    | 87.75    |
| 120        | Akash  | ECE    | 95    | 87.75    |
| 104        | Neha   | ECE    | 88    | 87.75    |
| 115        | Aman   | ME     | 85    | 78.4     |
| 106        | Priya  | ME     | 81    | 78.4     |
| 119        | Simran | ME     | 88    | 78.4     |























*/