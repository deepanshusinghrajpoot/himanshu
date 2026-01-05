import React from 'react'




/*


.

🔹 SQL String Functions (Most Important First)
------------------------------------------------


🏆 Tier 1: Must-Know (Very Important)

| Function                     | Use                    | Example                      | Result       |
| ---------------------------- | ---------------------- | ---------------------------- | ------------ |
| `LENGTH(str)` / `LEN(str)`   | Count characters       | `LENGTH('Deep')`             | `4`          |
| `UPPER(str)` / `LOWER(str)`  | Case conversion        | `UPPER('sql')`               | `SQL`        |
| `TRIM(str)`                  | Remove spaces          | `TRIM(' sql ')`              | `sql`        |
| `SUBSTRING(str, start, len)` | Extract part of string | `SUBSTRING('Database',2,3)`  | `ata`        |
| `REPLACE(str, from, to)`     | Replace substring      | `REPLACE('2025-08','-','/')` | `2025/08`    |
| `CONCAT(str1, str2, …)`      | Join strings           | `CONCAT('Deep','anshu')`     | `Deepanshu`  |
| `CONCAT_WS(sep, str1, …)`    | Join with separator    | `CONCAT_WS('-',2025,08,29)`  | `2025-08-29` |



🥈 Tier 2: Frequently Used (Good to Know)

| Function                                         | Use                            | Example                 | Result     |
| ------------------------------------------------ | ------------------------------ | ----------------------- | ---------- |
| `LEFT(str, n)` / `RIGHT(str, n)`                 | Extract from start/end         | `LEFT('Database',4)`    | `Data`     |
| `INSTR(str, substr)` / `POSITION(substr IN str)` | Find position                  | `INSTR('Database','a')` | `2`        |
| `RTRIM(str)` / `LTRIM(str)`                      | Remove trailing/leading spaces | `LTRIM('  sql')`        | `sql`      |
| `LPAD(str, len, pad)`                            | Pad left                       | `LPAD('7',3,'0')`       | `007`      |
| `RPAD(str, len, pad)`                            | Pad right                      | `RPAD('7',3,'0')`       | `700`      |
| `REPEAT(str, n)`                                 | Repeat string                  | `REPEAT('Hi ',3)`       | `Hi Hi Hi` |



🥉 Tier 3: Less Common but Useful

| Function                         | Use                | Example                | Result      |
| -------------------------------- | ------------------ | ---------------------- | ----------- |
lll| `REVERSE(str)`                   | Reverse string     | `REVERSE('SQL')`       | `LQS`       |
| `ASCII(char)`                    | ASCII code of char | `ASCII('A')`           | `65`        |
| `CHAR(code)`                     | Char from ASCII    | `CHAR(65)`             | `A`         |
| `INITCAP(str)` (Oracle/Postgres) | Capitalize words   | `INITCAP('sql world')` | `Sql World` |
| `FORMAT(num, d)`                 | Format numbers     | `FORMAT(1234.567,2)`   | `1,234.57`  |



🧑‍🤝‍🧑 Tier 4: Group String Functions

| Function                                     | Use                | Example                 | Result  |
| -------------------------------------------- | ------------------ | ----------------------- | ------- |
| `GROUP_CONCAT(col)` (MySQL)                  | Merge group values | `GROUP_CONCAT(name)`    | `A,B,C` |
| `STRING_AGG(col, sep)` (SQL Server/Postgres) | Merge group values | `STRING_AGG(name, ',')` | `A,B,C` |





✅ Quick Interview Tip:

If interviewer asks “most important string functions in SQL” → Start with LENGTH, UPPER/LOWER, TRIM, SUBSTRING, REPLACE, CONCAT.
If they go deeper → mention padding, searching (INSTR, LEFT, RIGHT).
For advanced questions → explain GROUP_CONCAT / STRING_AGG (very useful in reporting).




*/












const StringFunction = () => {
  return (
    <div>StringFunction</div>
  )
}

export default StringFunction