/*

🪟 WINDOW FRAME IN SQL (Interview-Ready)
_________________________________________

A window frame defines which rows are included for a window function relative to the current row.



(1) Default Frame in SQL
------------------------

RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW


📌 Meaning
...........
Includes all rows before the current row
Includes the current row




(2) Full Frame in SQL
---------------------

RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
-- OR
ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING


📌 Meaning
...........
Includes all rows before
Includes current row
Includes all rows after


⚠ Required for
***************
LAST_VALUE()
NTH_VALUE()





(3) Variable Frame in SQL
-------------------------
ROWS BETWEEN 3 PRECEDING AND 2 FOLLOWING
-- OR
RANGE BETWEEN 3 PRECEDING AND 2 FOLLOWING


📌 Meaning
...........
Includes 3 rows before the current row
Includes current row
Includes 2 rows after the current row



*/