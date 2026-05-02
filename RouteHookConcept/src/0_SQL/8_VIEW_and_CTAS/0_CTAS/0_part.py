'''








What is CTAS?
=============

Spoken:
"In CTAS, we do not need to define the table schema manually.
The schema is automatically created based on the SELECT query result."


---

CTAS Syntax
-----------

MySQL
-----

CREATE TABLE data_base.employees_copy
SELECT *
FROM data_base.employees;



PostgreSQL/Snowflake
--------------------

CREATE TABLE table_name AS (

      SELECT
      FROM
      WHERE

)





💡 Simple Memory Trick
MySQL → No AS ❌
PostgreSQL/Snowflake → Use AS ✅

---







Use Case
========

Spoken:
"CTAS is used to quickly create a table from existing data,
for backup, transformation, or temporary analysis."








'''