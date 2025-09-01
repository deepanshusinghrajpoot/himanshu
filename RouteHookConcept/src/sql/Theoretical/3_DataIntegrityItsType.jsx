
/*



Data Integrity
--------------

👉 Data Integrity means maintaining the correctness, accuracy, and consistency of data in a database throughout its lifecycle.


Type of Data Integrity
----------------------

                                    Data Integrity
                                          |
                                          |
    ----------------------------------------------------------------------------------
    |                         |                         |                            |
Domain Integrity        Entity Integrity       Referential Integrity         User-Defined Integrity    



(1). Domain Integrity :-   Domain integrity enforces valid entries for a given column by restricting the type, the format, or the range of values.
     ---------------

| **EmpID** | **Name** | **Age** | **Email**                                 |
| --------- | -------- | ------- | ----------------------------------------- |
| 101       | Rahul    | 25      | [rahul@gmail.com](mailto:rahul@gmail.com) |
| 102       | Ankit    | 30      | [ankit@yahoo.com](mailto:ankit@yahoo.com) |
| 103       | Priya    | -5 ❌   | priya(at)gmail.com ❌                    |




(2). Entity Integrity :- Entity Integrity ensures that every table has a unique identifier (Primary Key), so no duplicate rows or NULL values are allowed in the key column.
     ----------------

| **StudentID (PK)** | **Name** | **Course** |
| ------------------ | -------- | ---------- |
| 1                  | Rahul    | DBMS       |
| 2                  | Ankit    | Java       |
| 3                  | Priya    | SQL        |
| 3 ❌ (Duplicate)   | Priya    | SQL        |
| NULL ❌            | Aman     | Python     |




(3). Referential Integrity :- Referential Integrity ensures that relationships between tables remain consistent. A foreign key in one table must always refer to a valid primary key in another table.
     ---------------------

🔹 Example: Student & Course Tables

Course Table
| **CourseID (PK)** | **CourseName** |
| ----------------- | -------------- |
| 101               | DBMS           |
| 102               | Java           |
| 103               | SQL            |


Student Table
| **StudentID (PK)** | **Name** | **CourseID (FK)** |
| ------------------ | -------- | ----------------- |
| 1                  | Rahul    | 101               |
| 2                  | Ankit    | 102               |
| 3                  | Priya    | 103               |



🔹 Explanation

If we try to delete CourseID = 101 (DBMS) from the Course table → ❌ It breaks Referential Integrity because Rahul (StudentID 1) is enrolled in that course.

Similarly, if we try to insert a student with CourseID = 105 (not present in Course table) → ❌ It also breaks Referential Integrity.

✅ Maintained using Foreign Key constraint.





(4). User-defined Integrity :- User-defined integrity enforces specific business rules defined by the user that are not covered by domain, entity, or referential integrity.
     ----------------------

🔹 Example: Employee Table

| **EmpID (PK)** | **Name** | **Age** | **Salary** |
| -------------- | -------- | ------- | ---------- |
| 1              | Rahul    | 25      | 30,000     |
| 2              | Ankit    | 17 ❌    | 20,000     |
| 3              | Priya    | 30      | -5000 ❌    |



🔹 Explanation

Age must be ≥ 18 → Employee with Age = 17 breaks user-defined rule.

Salary must be > 0 → Negative salary breaks user-defined rule.

These rules are not automatically enforced by DBMS but added by user with CHECK constraints, triggers, or stored procedures.




*/