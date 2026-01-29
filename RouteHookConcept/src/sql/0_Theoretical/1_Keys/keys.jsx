/*



Super Key
---------

Definition:
A Super Key is any attribute or a set of attributes in a table that can uniquely identify each row in that table.


Key Points:

A table can have multiple Super Keys.
Every Candidate Key and Primary Key is a Super Key.
But not every Super Key is minimal (so not all Super Keys are Candidate Keys).


Example Table: Student

| StudentID | RollNo | StudentName | PhoneNo    |
| --------- | ------ | ----------- | ---------- |
| 1         | 101    | Amit        | 9876543210 |
| 2         | 102    | Neha        | 8765432109 |
| 3         | 103    | Ramesh      | 7654321098 |


Possible Super Keys

{StudentID} → unique for each student.
{RollNo} → unique for each student.
{PhoneNo} → unique for each student.
{StudentID, StudentName} → still unique.
{RollNo, PhoneNo} → also unique.

Conclusion

👉 Any attribute (alone or in combination) that gives uniqueness to table rows is a Super Key.












Candidate Key
-------------

Definition:
A Candidate Key is a minimal set of attributes that can uniquely identify each row (tuple) in a table.

      Minimal means no attribute can be removed from it while still maintaining uniqueness.
      A table can have multiple Candidate Keys.
      Out of all Candidate Keys, one is chosen as the Primary Key.


Example Table: Student

| StudentID | RollNo | StudentName | PhoneNo    |
| --------- | ------ | ----------- | ---------- |
| 1         | 101    | Amit        | 9876543210 |
| 2         | 102    | Neha        | 8765432109 |
| 3         | 103    | Ramesh      | 7654321098 |


Candidate Keys in this table:

{StudentID} → unique for each row ✅
{RollNo} → unique for each row ✅
{PhoneNo} → unique for each row ✅


Difference from Super Key:

Super Key: Any attribute(s) that uniquely identifies rows (can be minimal or non-minimal).
Candidate Key: A minimal Super Key (no extra attribute is present).


✅ Example:

{StudentID, RollNo} → Super Key (unique but not minimal, since either StudentID or RollNo alone is enough).

{StudentID} → Candidate Key (minimal).










Primary Key
-----------

Definition:
A Primary Key is a special Candidate Key selected to uniquely identify each row in a table.


Properties of Primary Key

Uniqueness – Values must be unique for each row.
Not Null – Cannot contain NULL values.
Single per table – A table can have only one Primary Key.
Minimal – Chosen from Candidate Keys.
Immutable – Should not change frequently.


Example Table: Employee

| EmpID | EmpCode | Name   | PhoneNo    |
| ----- | ------- | ------ | ---------- |
| 1     | E101    | Amit   | 9876543210 |
| 2     | E102    | Neha   | 8765432109 |
| 3     | E103    | Ramesh | 7654321098 |


Candidate Keys: {EmpID}, {EmpCode}, {PhoneNo}
Primary Key chosen: {EmpID}

So EmpID becomes the Primary Key of this table.


Difference with Other Keys

Super Key: Any attribute(s) that can uniquely identify rows.
Candidate Key: Minimal Super Keys.
Primary Key: One selected Candidate Key for the table.












Alternate Key
-------------

Definition:
An Alternate Key is any Candidate Key that is not chosen as the Primary Key.
  lll  In other words, all Candidate Keys except the Primary Key are Alternate Keys.

Example Table: Employee

| EmpID | EmpCode | Name   | PhoneNo    |
| ----- | ------- | ------ | ---------- |
| 1     | E101    | Amit   | 9876543210 |
| 2     | E102    | Neha   | 8765432109 |
| 3     | E103    | Ramesh | 7654321098 |


Candidate Keys: {EmpID}, {EmpCode}, {PhoneNo}
Primary Key (chosen): {EmpID}
Alternate Keys: {EmpCode}, {PhoneNo}


Key Points
----------

1. Alternate Keys are unique and not null like the Primary Key.
2. A table can have multiple Alternate Keys.
3. They act as a backup option if the Primary Key is not available.









Foreign Key
-----------

Definition:

lll A Foreign Key is an attribute (or set of attributes) in one table that refers to the Primary Key of another table.
lll Foreign Key is used to link two tables together.
lll Foreign Keys help in maintaining Referential Integrity.



Example
Table: Department

| DeptID (PK) | DeptName |
| ----------- | -------- |
| 101         | HR       |
| 102         | IT       |
| 103         | Finance  |


Table: Employee

| EmpID (PK) | Name   | DeptID (FK) |
| ---------- | ------ | ----------- |
| 1          | Amit   | 101         |
| 2          | Neha   | 102         |
| 3          | Ramesh | 103         |


Explanation

In the Employee table, DeptID is a Foreign Key that refers to DeptID in the Department table.
This ensures an employee can only belong to a department that actually exists in the Department table.



Key Points

A table can have multiple Foreign Keys.
A Foreign Key can accept NULL values (if relationship is optional).
Helps prevent orphan records (records that reference non-existing entries).



Composite Key
-------------

A key formed by two or more attributes together that can uniquely identify a row (when a single attribute is not enough).
Used when no single attribute alone can make a record unique.

Example:
Table: Enrollment

| StudentID | CourseID | Grade |
| --------- | -------- | ----- |
| 101       | C01      | A     |
| 101       | C02      | B     |
| 102       | C01      | A     |

Here:

StudentID alone is not unique (same student can enroll in multiple courses).
CourseID alone is not unique (multiple students can take the same course).
But the combination (StudentID, CourseID) uniquely identifies each row.
      👉 So (StudentID, CourseID) is a Composite Key.



      

*/








import React from 'react'



const keys = () => {


  return (
    <div>keys</div>
  )


}

export default keys