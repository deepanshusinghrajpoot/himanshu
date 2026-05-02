/*




Second Normal Form (2NF)
------------------------


Definition

It is already in 1NF.
In 2NF, all non-prime attributes (non-key attributes) must be fully functionally dependent on the entire primary key.
2NF eliminates Partial Dependency.



🔹 Non-key attributes (non-prime attributes)

👉 Attributes that are not part of any candidate key.
Example: If (TeacherID + Subject) is the primary key, then TeacherSalary is a non-key attribute.



🔹 Functional Dependency Rule
if (r1.x == r2.x) then (r1.y == r2.y)


➡️ Meaning: If two rows have the same value for attribute X, they must also have the same value for attribute Y.


Example:
If two rows have the same TeacherID = 25, then their TeacherSalary must also be the same (30,000).





🔹 Fully Functional Dependency

👉 A dependency X → Y is fully functional if:

     Y is dependent on the whole of X, and
     Y is not dependent on any proper subset of X.


⚠️ If Y depends only on a part of X, it is a Partial Dependency (violates 2NF).


❌ Example (Table before 2NF – violates rule)

| TeacherID | Subject   | TeacherSalary |
| --------- | --------- | ------------- |
| 25        | Chemistry | 30000         |
| 25        | Biology   | 30000         |
| 26        | Physics   | 35000         |
| 26        | Math      | 35000         |
| 27        | English   | 40000         |


⚠️ Problem:

Candidate Key = (TeacherID, Subject)
TeacherSalary depends only on TeacherID, not on the full composite key.
This is a Partial Dependency, so table is not in 2NF.


✅ Example (Table in 2NF)

We split into two tables:

Teacher Table:

| TeacherID | TeacherSalary |
| --------- | ------------- |
| 25        | 30000         |
| 26        | 35000         |
| 27        | 40000         |

Teacher_Subject Table:

| TeacherID | Subject   |
| --------- | --------- |
| 25        | Chemistry |
| 25        | Biology   |
| 26        | Physics   |
| 26        | Math      |
| 27        | English   |


✔️ Now:

TeacherSalary is fully functionally dependent on TeacherID.
Subject is fully functionally dependent on (TeacherID, Subject).
No Partial Dependency → relation is in 2NF.










 */