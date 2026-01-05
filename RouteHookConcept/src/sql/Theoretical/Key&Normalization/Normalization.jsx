/*




🔹 Normalization
-----------------

lll Definition: Normalization is the process of organizing data in a database.

Purpose: The main purpose of normalization is

lll Eliminates anomalies: Insertion, Update, Deletion.
lll Minimizes redundancy (duplicate data).
lll Divides large tables into smaller related tables and links them using relationships (keys).

Goal: To make the database consistent, efficient, and easy to maintain.





🔹 Redundancy

Types of Redundancy

Row Level Redundancy → Duplicate rows
Column Level Redundancy → Repeated information across columns → causes anomalies





1️⃣ Row Level Redundancy
------------------------

👉 Initial Table (With Redundancy)

| StudentID | Student Name | Age |             |
| --------- | ------------ | --- | ----------- |
| 1         | Rahul        | 20  |             |
| 1         | Rahul        | 20  | ❌ Duplicate |
| 2         | Ankit        | 21  |             |

👉 After Removing Row Redundancy (Using Primary Key)

| StudentID (PK) | Student Name | Age |
| -------------- | ------------ | --- |
| 1              | Rahul        | 20  |
| 2              | Ankit        | 21  |







2️⃣ Column Level Redundancy
---------------------------

👉 Initial Table (With Column Redundancy)

| StudentID | Student Name | Age | CourseID | Course Name | TeacherID | Teacher Name | Teacher Salary |
| --------- | ------------ | --- | -------- | ----------- | --------- | ------------ | -------------- |
| 1         | Rahul        | 20  | C101     | DBMS        | T01       | Sharma       | 50,000         |
| 2         | Ankit        | 21  | C101     | DBMS        | T01       | Sharma       | 50,000         |
| 3         | Priya        | 22  | C102     | Java        | T02       | Verma        | 55,000         |

⚠ Problems:

Insertion Anomaly → Can’t insert teacher unless a student exists.
Deletion Anomaly → If all students of a teacher are deleted, teacher info is lost.
Update Anomaly → If teacher’s salary changes, must update in multiple rows.


(a) Insertion Anomaly
    -----------------

👉 Problem: Cannot insert teacher Mehta (T03) without a student.

👉 Solution (Normalized Tables):

Student Table

| StudentID | Student Name | Age | CourseID |
| --------- | ------------ | --- | -------- |
| 1         | Rahul        | 20  | C101     |
| 2         | Ankit        | 21  | C101     |
| 3         | Priya        | 22  | C102     |


Teacher Table

| TeacherID | Teacher Name | Teacher Salary                                |
| --------- | ------------ | --------------------------------------------- |
| T01       | Sharma       | 50,000                                        |
| T02       | Verma        | 55,000                                        |
| T03       | Mehta        | 60,000 ✅ now possible to insert teacher alone |



(b) Deletion Anomaly
    ----------------
👉 Problem: If Priya (StudentID = 3) is deleted → Teacher Verma’s info also lost.

👉 Solution (Normalized Tables):

Student Table

| StudentID | Student Name | Age | CourseID |
| --------- | ------------ | --- | -------- |
| 1         | Rahul        | 20  | C101     |
| 2         | Ankit        | 21  | C101     |

Teacher Table

| TeacherID | Teacher Name | Teacher Salary                        |
| --------- | ------------ | ------------------------------------- |
| T01       | Sharma       | 50,000                                |
| T02       | Verma        | 55,000 ✅ info safe even if no student |



(c) Update Anomaly
    --------------

👉 Problem: If Teacher Sharma’s salary changes → must update in many rows.

👉 Solution (Normalized Tables):

Student Table

| StudentID | Student Name | Age | CourseID |
| --------- | ------------ | --- | -------- |
| 1         | Rahul        | 20  | C101     |
| 2         | Ankit        | 21  | C101     |

Teacher Table

| TeacherID | Teacher Name | Teacher Salary            |
| --------- | ------------ | ------------------------- |
| T01       | Sharma       | 55,000 ✅ update only once |
| T02       | Verma        | 55,000                    |







Type of normalization form
--------------------------

There are foure type of Normalization form

(1). 1NF
(2). 2NF
(3). 3NF
(4). BCNF


*/









import React from 'react'

const Normalization = () => {
  return (
    <div>Normalization</div>
  )
}

export default Normalization