
'''








===========================================
Slowly Changing Dimensions (SCD)
===========================================



-- =========================================
-- Definition
-- =========================================

-- Slowly Changing Dimension (SCD) is a technique used in data warehousing
-- to manage and track changes in dimension data over time.


-- =========================================
-- Why Do We Need SCD? (Real-World Problem)
-- =========================================

-- Problem:
-- Customer or product details change over time.

-- Example:
-- Customer moves from Delhi → Mumbai

-- If we overwrite data:
-- We lose history ❌

-- If we keep history:
-- We can track changes over time ✅

-- SCD helps maintain:
-- ✔ Historical data
-- ✔ Accurate reporting
-- ✔ Business insights over time



-- =========================================
-- Types of Slowly Changing Dimensions
-- =========================================

-- Type 0 → No Change
-- Type 1 → Overwrite (Upsert)
-- Type 2 → Maintain Full History
-- Type 3 → Store Previous Value



-- =========================================
-- Type 0 (No Change)
-- =========================================

-- Definition:
-- In Type 0, data never changes.
-- Once inserted, it remains fixed.

-- Example:
-- Date of Birth should never change

DimCustomer
--------------------------------
| customer_id | name  | dob       |
--------------------------------
| C101        | Rahul | 2000-01-01 |



-- =========================================
-- Type 1 (UPSERT - Overwrite)
-- =========================================

-- Definition:
-- In Type 1, old data is overwritten with new data.
-- No history is maintained.

---------------------------------
-- Before
---------------------------------
Product_ID | Name   | Prod_Cat
---------------------------------
1          | Honey  | Food
2          | Shirt  | Clothing
3          | Comb   | Clothing

---------------------------------
-- After (Updated)
---------------------------------
Product_ID | Name   | Prod_Cat
---------------------------------
1          | Honey  | Food
2          | Shirt  | Clothing
3          | Comb   | Hair

-- Old value lost ❌



-- =========================================
-- Type 2 (History Maintenance)
-- =========================================

-- Definition:
-- In Type 2, a new row is created whenever data changes.
-- Full history is preserved.

-- Additional Columns:
-- effect_start_date, effect_end_date, in_use

----------------------------------------------------------------------------------
-- Before
----------------------------------------------------------------------------------
Product_ID | Name  | Prod_Cat | Start_Date | End_Date   | In_Use
----------------------------------------------------------------------------------
1          | Honey | Food     | 2024-01-01 | 3000-01-01 | Yes
2          | Shirt | Clothing | 2024-01-01 | 3000-01-01 | Yes
3          | Comb  | Clothing | 2024-01-01 | 3000-01-01 | Yes


----------------------------------------------------------------------------------
-- After (Category Changed)
----------------------------------------------------------------------------------
Product_ID | Name  | Prod_Cat | Start_Date | End_Date   | In_Use
----------------------------------------------------------------------------------
1          | Honey | Food     | 2024-01-01 | 3000-01-01 | Yes
2          | Shirt | Clothing | 2024-01-01 | 3000-01-01 | Yes
3          | Comb  | Clothing | 2024-01-01 | 2024-02-01 | No
4          | Comb  | Hair     | 2024-02-01 | 3000-01-01 | Yes

-- History preserved ✅



-- =========================================
-- Type 3 (Previous Value)
-- =========================================

-- Definition:
-- In Type 3, only the previous value is stored.
-- Limited history is maintained.

-------------------------------------------------
-- Before
-------------------------------------------------
Product_ID | Name  | Prod_Cat | Prev_Prod_Cat
-------------------------------------------------
1          | Honey | Food     | Food
2          | Shirt | Clothing | Clothing
3          | Comb  | Clothing | Clothing

-------------------------------------------------
-- After
-------------------------------------------------
Product_ID | Name  | Prod_Cat | Prev_Prod_Cat
-------------------------------------------------
1          | Honey | Food     | Food
2          | Shirt | Clothing | Clothing
3          | Comb  | Hair     | Clothing

-- Only previous value stored ✅





===========================================
FINAL INTERVIEW REVISION
===========================================

Type 0 → No change
Type 1 → Overwrite (No history)
Type 2 → Full history (new row)
Type 3 → Store previous value

===========================================









'''