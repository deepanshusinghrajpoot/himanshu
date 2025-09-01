/*





Boyce-Codd Normal Form (BCNF)
-----------------------------

1. Definition

BCNF is an advanced version of 3NF.

lll BCNF is stricter than 3NF.

A relation will be in BCNF if:
   👉 For every Functional Dependency (X → Y),
    X must be a Super Key.




2. Why BCNF?

lll Even if a relation is in 3NF, sometimes anomalies (insertion, update, deletion) still occur.
lll BCNF removes these anomalies by ensuring every determinant is a super key.




3. Important Concepts

Super Key: An attribute (or set of attributes) that uniquely identifies a row.
Candidate Key: Minimal super key (cannot be reduced further).
Determinant: In X → Y, the attribute set X is called determinant.

👉 BCNF Rule: Every determinant must be a super key.



4. Example (Not in BCNF ❌)

Table: Course Table

| CourseID | Teacher | Room |
| -------- | ------- | ---- |
| C1       | A       | R1   |
| C2       | B       | R2   |
| C3       | A       | R1   |


Functional Dependencies:

CourseID → Teacher (each course has one teacher)
Teacher → Room (each teacher teaches in one room)
Candidate Key = {CourseID}

Problem: Teacher → Room but Teacher is not a super key ❌

So, table violates BCNF.



5. Example (In BCNF ✅)
We split the table:

Course Table

| CourseID | Teacher |
| -------- | ------- |
| C1       | A       |
| C2       | B       |
| C3       | A       |

Teacher Table

| Teacher | Room |
| ------- | ---- |
| A       | R1   |
| B       | R2   |

✔ Now, every functional dependency has a super key.
✔ No anomaly → Table is in BCNF.



6. Key Point Summary

    1NF → Atomic values only
    2NF → No Partial Dependency
    3NF → No Transitive Dependency
    BCNF → For every FD (X → Y), X must be a Super Key









 */