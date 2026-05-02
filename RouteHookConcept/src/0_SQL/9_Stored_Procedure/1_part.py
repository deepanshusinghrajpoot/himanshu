'''






# ==========================================
# STORE TWO VALUES (SUM + AVG) INTO VARIABLES
# ==========================================

## Goal
Take SUM and AVG from query → store in variables → print

---

# SYNTAX

DELIMITER $$

CREATE PROCEDURE get_sum_avg_salary()
BEGIN
    DECLARE total_sal INT;
    DECLARE avg_sal DECIMAL(10,2);

    -- Store SUM and AVG into variables
    SELECT 
        SUM(salary),
        AVG(salary)
    INTO 
        total_sal,
        avg_sal
    FROM employees;

    -- Print values
    SELECT total_sal, avg_sal;

END $$

DELIMITER ;

---

# EXECUTE

CALL get_sum_avg_salary();

---

# WITH CONDITION (IMPORTANT)

DELIMITER $$

CREATE PROCEDURE get_sum_avg_by_dept(IN dept_name VARCHAR(50))
BEGIN
    DECLARE total_sal INT;
    DECLARE avg_sal DECIMAL(10,2);

    SELECT 
        SUM(salary),
        AVG(salary)
    INTO 
        total_sal,
        avg_sal
    FROM employees
    WHERE department = dept_name;

    SELECT total_sal, avg_sal;

END $$

DELIMITER ;

-- Call
CALL get_sum_avg_by_dept('HR');

---

# INTERVIEW LINES

👉 "We can store multiple values using SELECT INTO with multiple variables."  

👉 "Order of columns must match order of variables."

---

# FINAL FLOW

DECLARE → SELECT (SUM, AVG) INTO → SELECT (PRINT)








'''