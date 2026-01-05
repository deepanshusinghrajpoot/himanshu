import React from 'react'



/*




📅 SQL Date & Time Functions (Most Important First)
----------------------------------------------------




🏆 Tier 1: Must-Know (Interview Favorites)
-------------------------------------------

| Function                                   | Use                 | Example                       | Result                |
| ------------------------------------------ | ------------------- | ----------------------------- | --------------------- |
| `CURRENT_DATE` / `GETDATE()`               | Current date        | `SELECT CURRENT_DATE;`        | `2025-08-29`          |
| `CURRENT_TIMESTAMP` / `NOW()`              | Current date + time | `SELECT NOW();`               | `2025-08-29 10:25:30` |
| `DATE()`                                   | Extract date part   | `DATE('2025-08-29 10:30:00')` | `2025-08-29`          |
| `TIME()`                                   | Extract time part   | `TIME('2025-08-29 10:30:00')` | `10:30:00`            |
| `YEAR(date)` / `MONTH(date)` / `DAY(date)` | Extract components  | `YEAR('2025-08-29')`          | `2025`                |





🥈 Tier 2: Frequently Used
---------------------------

| Function          | Use                   | Example                   | Result   |
| ----------------- | --------------------- | ------------------------- | -------- |
| `DAYNAME(date)`   | Day of week           | `DAYNAME('2025-08-29')`   | `Friday` |
| `MONTHNAME(date)` | Month name            | `MONTHNAME('2025-08-29')` | `August` |
| `WEEK(date)`      | Week number           | `WEEK('2025-08-29')`      | `35`     |
| `DAYOFWEEK(date)` | Sunday=1 … Saturday=7 | `DAYOFWEEK('2025-08-29')` | `6`      |
| `DAYOFYEAR(date)` | Day number in year    | `DAYOFYEAR('2025-08-29')` | `241`    |





🥉 Tier 3: Date Arithmetic
---------------------------

| Function                          | Use                   | Example                                         | Result       |
| --------------------------------- | --------------------- | ----------------------------------------------- | ------------ |
| `DATE_ADD(date, INTERVAL n unit)` | Add interval          | `DATE_ADD('2025-08-29', INTERVAL 10 DAY)`       | `2025-09-08` |
| `DATE_SUB(date, INTERVAL n unit)` | Subtract interval     | `DATE_SUB('2025-08-29', INTERVAL 1 MONTH)`      | `2025-07-29` |
| `DATEDIFF(date1, date2)`          | Difference in days    | `DATEDIFF('2025-09-10','2025-08-29')`           | `12`         |
| `TIMESTAMPDIFF(unit, d1, d2)`     | Diff in specific unit | `TIMESTAMPDIFF(YEAR,'2000-08-29','2025-08-29')` | `25`         |



🧑‍💻 Tier 4: Formatting & Advanced
---------------------------------

| Function                        | Use                         | Example                                | Result       |
| ------------------------------- | --------------------------- | -------------------------------------- | ------------ |
| `STR_TO_DATE(str, format)`      | Convert string → date       | `STR_TO_DATE('29-08-2025','%d-%m-%Y')` | `2025-08-29` |
lll | `DATE_FORMAT(date, format)`     | Format date output          | `DATE_FORMAT('2025-08-29','%d/%m/%Y')` | `29/08/2025` |
| `EXTRACT(unit FROM date)`       | Extract part (standard SQL) | `EXTRACT(MONTH FROM '2025-08-29')`     | `8`          |
| `LAST_DAY(date)` (MySQL/Oracle) | Last day of month           | `LAST_DAY('2025-08-29')`               | `2025-08-31` |






✅ Quick Memory Hack for Interviews:

Current date/time → NOW(), CURRENT_DATE, CURRENT_TIMESTAMP.
Extract parts → YEAR, MONTH, DAY, DAYNAME.
Arithmetic → DATE_ADD, DATE_SUB, DATEDIFF.
Formatting → DATE_FORMAT, STR_TO_DATE.







*/














const DateFunction = () => {
  return (
    <div>DateFunction</div>
  )
}

export default DateFunction