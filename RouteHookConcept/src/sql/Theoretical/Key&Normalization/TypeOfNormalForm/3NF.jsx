/*






Third Normal Form (3NF)
-----------------------

Definition

A relation will be in 3NF if:
       It is already in 2NF
       There is no transitive dependency for non-prime attributes



Transitive Dependency
      When a non-prime attribute determines another non-prime attribute, it is called transitive dependency.
      Non-prime Attribute = An attribute that is not part of any candidate key.



Example (Not in 3NF ❌)

| StudentID | StudentName | DepartmentID | DepartmentName |
| --------- | ----------- | ------------ | -------------- |
| 1         | Amit        | D1           | Physics        |
| 2         | Priya       | D2           | Chemistry      |
| 3         | Rohan       | D3           | Math           |

Candidate Key = StudentID
StudentName depends on StudentID ✅
But DepartmentName depends on DepartmentID, and DepartmentID depends on StudentID ❌ (transitive dependency).




Example (In 3NF ✅)

Student Table

| StudentID | StudentName | DepartmentID |
| --------- | ----------- | ------------ |
| 1         | Amit        | D1           |
| 2         | Priya       | D2           |
| 3         | Rohan       | D3           |


Department Table

| DepartmentID | DepartmentName |
| ------------ | -------------- |
| D1           | Physics        |
| D2           | Chemistry      |
| D3           | Math           |

✔ Now all non-prime attributes depend only on the key.
✔ No non-prime attribute depends on another non-prime attribute.
✔ Hence, relation is in 3NF.


Key Point
  2NF removes Partial Dependency
  3NF removes Transitive Dependency















*/