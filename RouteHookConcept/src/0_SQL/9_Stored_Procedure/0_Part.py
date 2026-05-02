'''



# =========================
# STORED PROCEDURE
# =========================

## Definition (Interview Ready)

lll A stored procedure is a precompiled set of SQL statements stored in the database.
    It can be executed repeatedly with a single call.

👉 Simple line:
Stored procedure is like a function in SQL that runs on the database.

---

# =========================
# DIFFERENCE: PROCEDURE vs QUERY
# =========================

| Feature        | Query                          | Stored Procedure              |
|---------------|--------------------------------|-------------------------------|
| Execution     | Runs every time                 | Stored & reusable             |
| Performance   | Slower                         | Faster (precompiled)          |
| Reusability   | No                             | Yes                           |
| Logic         | Simple SQL                     | Complex logic (IF, LOOP)      |
| Parameters    | Not supported                  | Supported                     |
| Maintenance   | Hard                           | Easy                          |

👉 Interview Line:
"Queries are ad-hoc, stored procedures are reusable and optimized."

---

# =========================
# ADVANTAGES
# =========================

👉 Improves performance (precompiled)  
👉 Reusable SQL logic  
👉 Reduces network traffic  
👉 Better security  
👉 Centralized logic  

---

# =========================
# BASIC SYNTAX
# =========================

CREATE PROCEDURE procedure_name()
BEGIN
    -- SQL statements
END;

---

# =========================
# EXECUTE PROCEDURE
# =========================

CALL procedure_name();

---

# =========================
# EXAMPLE
# =========================

-- Step 1: Query

SELECT department,
       SUM(salary) AS total_expense
FROM employees
GROUP BY department;

-- Step 2: Stored Procedure

DELIMITER $$

CREATE PROCEDURE department_expense()
BEGIN
    SELECT department,
           SUM(salary) AS total_expense
    FROM employees
    GROUP BY department;
END $$

DELIMITER ;

-- Step 3: Execute

CALL department_expense();

---

# =========================
# VARIABLES
# =========================

DELIMITER $$

CREATE PROCEDURE example_var()
BEGIN
    DECLARE total INT;
    SET total = 100;

    SELECT total;
END $$

DELIMITER ;

---

# =========================
# PARAMETERS
# =========================

DELIMITER $$

CREATE PROCEDURE get_expense(IN dept_name VARCHAR(50))
BEGIN
    SELECT department,
           SUM(salary)
    FROM employees
    WHERE department = dept_name
    GROUP BY department;
END $$

DELIMITER ;

-- Call
CALL get_expense('HR');

---

# =========================
# IF-ELSE
# =========================

DELIMITER $$

CREATE PROCEDURE check_salary(IN sal INT)
BEGIN
    IF sal > 50000 THEN
        SELECT 'High Salary';
    ELSE
        SELECT 'Low Salary';
    END IF;
END $$

DELIMITER ;

-- Call
CALL check_salary(60000);

---

# =========================
# LOOP (WHILE)
# =========================

DELIMITER $$

CREATE PROCEDURE loop_example()
BEGIN
    DECLARE i INT DEFAULT 1;

    WHILE i <= 5 DO
        SELECT i;
        SET i = i + 1;
    END WHILE;

END $$

DELIMITER ;

---

# =========================
# LOOP (REPEAT)
# =========================

DELIMITER $$

CREATE PROCEDURE repeat_example()
BEGIN
    DECLARE i INT DEFAULT 1;

    REPEAT
        SELECT i;
        SET i = i + 1;
    UNTIL i > 5
    END REPEAT;

END $$

DELIMITER ;




# =========================
# DROP STORED PROCEDURE
# =========================

-- Used to delete a stored procedure

DROP PROCEDURE procedure_name;

-- Example
DROP PROCEDURE department_expense;




# =========================
# ALTER STORED PROCEDURE
# =========================

-- MySQL does NOT support direct ALTER for procedure logic
-- Instead, use DROP + CREATE again

-- Step 1: Drop
DROP PROCEDURE procedure_name;

-- Step 2: Recreate
DELIMITER $$

CREATE PROCEDURE procedure_name()
BEGIN
    -- updated SQL logic
END $$

DELIMITER ;




# =========================
# PRINT IN STORED PROCEDURE (MySQL)
# =========================

-- MySQL does NOT have PRINT like other databases
-- We use SELECT to print/output

# SYNTAX

SELECT 'Your Message';







DELIMITER Keyword
=================

Spoken:
lll "Delimiter is used to change the default statement ending symbol in MySQL."


| Concept           | Explanation                                   |
| ----------------- | --------------------------------------------- |
| Default Delimiter | `;` (ends a query)                            |
| Problem           | Procedures have multiple `;` → MySQL confused |
| Solution          | Change delimiter (e.g., `$$`)                 |
| Usage             | `DELIMITER $$`                                |
| Procedure End     | `END $$`                                      |
| Reset             | `DELIMITER ;`                                 |






'''