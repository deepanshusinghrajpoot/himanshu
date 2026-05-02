'''





# ==========================================
# STORED PROCEDURE WITH TRY-CATCH (MEANING)
# ==========================================

## Definition (Interview Ready)

A stored procedure with TRY-CATCH is used to execute SQL logic safely.
If any error occurs, it is handled using a HANDLER to prevent failure.

👉 Simple Line:
"It executes SQL logic and handles errors using DECLARE HANDLER."

---

## IMPORTANT

-- MySQL does NOT support TRY-CATCH directly
-- We use HANDLER as CATCH

TRY   → Main SQL logic  
CATCH → DECLARE HANDLER  

---

# ==========================================
# SIMPLE EXAMPLE
# ==========================================

DELIMITER $$

CREATE PROCEDURE safe_update()
BEGIN
    -- CATCH (Error Handling)
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'Error occurred';
    END;

    -- TRY (Main Logic)
    START TRANSACTION;

    UPDATE employees
    SET salary = salary + 1000
    WHERE emp_id = 101;

    COMMIT;

    SELECT 'Success';

END $$

DELIMITER ;

---

# ==========================================
# EXECUTION
# ==========================================

CALL safe_update();

---

# ==========================================
# FLOW
# ==========================================

IF no error → COMMIT → Success  

IF error → HANDLER → ROLLBACK → Error message  

---

# ==========================================
# INTERVIEW LINE
# ==========================================

👉 "In MySQL, TRY-CATCH is implemented using DECLARE HANDLER."

👉 "We use transactions with HANDLER to ensure safe execution."

👉 "If error occurs, rollback prevents partial data changes."






















================================================================================================================





# ==========================================
# GET ERROR MESSAGE IN STORED PROCEDURE
# ==========================================

## KEY IDEA

-- Use HANDLER to catch error
-- Use GET DIAGNOSTICS to get error message

---

# SYNTAX

DELIMITER $$

CREATE PROCEDURE get_error_message()
BEGIN
    DECLARE err_msg TEXT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Get actual error message
        GET DIAGNOSTICS CONDITION 1
            err_msg = MESSAGE_TEXT;

        -- Print error
        SELECT err_msg;
    END;

    -- Generate error
    SELECT 10 / 0;

END $$

DELIMITER ;

---

# EXECUTE

CALL get_error_message();

---

# OUTPUT

Division by 0

--------------------------------------------------

# FULL ERROR DETAILS (ADVANCED)

DELIMITER $$

CREATE PROCEDURE get_full_error()
BEGIN
    DECLARE err_msg TEXT;
    DECLARE err_code INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
            err_code = MYSQL_ERRNO,
            err_msg  = MESSAGE_TEXT;

        SELECT err_code, err_msg;
    END;

    SELECT 10 / 0;

END $$

DELIMITER ;

--------------------------------------------------

# INTERVIEW LINES

👉 "We use GET DIAGNOSTICS to fetch error message."  

👉 "MESSAGE_TEXT gives actual error description."  

👉 "MYSQL_ERRNO gives error code."
















'''