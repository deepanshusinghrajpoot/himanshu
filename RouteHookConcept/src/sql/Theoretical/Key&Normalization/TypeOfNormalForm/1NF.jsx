/*




First Normal Form (1NF)
-----------------------

lll A relation will be in 1NF if:

lll It contains only atomic values (indivisible values).
lll Each column must hold a single value, not multiple or repeating groups.


Example without atomic values ❌ (Not in 1NF)

| TeacherID | Subject          | TeacherSalary |
| --------- | ---------------- | ------------- |
| T01       | Math, Science    | 50000         |
| T02       | English, History | 45000         |
| T03       | Physics          | 55000         |


⚠️ Problem:

The column Subject contains multiple values (e.g., Math, Science).
This violates 1NF because values are not atomic.


Example with atomic values ✅ (In 1NF)

| TeacherID | Subject | TeacherSalary |
| --------- | ------- | ------------- |
| T01       | Math    | 50000         |
| T01       | Science | 50000         |
| T02       | English | 45000         |
| T02       | History | 45000         |
| T03       | Physics | 55000         |


✔️ Fixed:

Each cell has only one value (atomic).
Repeating groups are removed.
Now the table is in 1NF.









*/