

'''


===========================================
Types of Fact Tables (Real-World Example)
===========================================



-- =========================================
-- 1. Transaction / Granular Fact Table
-- One Row = One Transaction
-- One row per transaction (detailed data)
-- =========================================

FactSales
---------------------------------------------------------
| order_id | customer_id | product_id | date       | amount | quantity |
---------------------------------------------------------
| 1001     | C101        | P501       | 2026-01-10 | 1500   | 1        |
| 1002     | C102        | P502       | 2026-01-10 | 3000   | 2        |
| 1003     | C101        | P503       | 2026-01-11 | 2000   | 1        |


DimCustomer
-------------------------------
| customer_id | name   | city   |
-------------------------------
| C101        | Rahul  | Delhi  |
| C102        | Aman   | Mumbai |


DimProduct
-----------------------------------------
| product_id | product_name | category   |
-----------------------------------------
| P501       | Laptop       | Electronics|
| P502       | Mobile       | Electronics|
| P503       | Shoes        | Fashion    |



-- =========================================
-- 2. Periodic / Snapshot Fact Table
-- One Row ≠ One Transaction (Monthly Data)
-- One row per time interval (summary data)
-- =========================================

FactMonthlySales
-----------------------------------------------------
| month    | product_id | total_sales | total_quantity |
-----------------------------------------------------
| Jan-2026 | P501       | 50000       | 20             |
| Jan-2026 | P502       | 75000       | 35             |
| Feb-2026 | P501       | 60000       | 25             |


DimDate
-------------------------
| month | year |
-------------------------
| Jan   | 2026 |
| Feb   | 2026 |



-- =========================================
-- 3. Accumulating Fact Table
-- One Row = One Process (Order Lifecycle)
-- One row per lifecycle/process
-- =========================================

FactOrderLifecycle
---------------------------------------------------------------------------------------------------------
| order_id | customer_id | order_date | confirm_date | seller_confirm | dispatch_date | delivered_date |
---------------------------------------------------------------------------------------------------------
| 2001     | C101        | 2026-01-01 | 2026-01-02   | 2026-01-03     | 2026-01-04    | 2026-01-06     |
| 2002     | C102        | 2026-01-05 | 2026-01-06   | 2026-01-07     | 2026-01-08    | 2026-01-10     |


DimCustomer
-------------------------------
| customer_id | name   | city   |
-------------------------------
| C101        | Rahul  | Delhi  |
| C102        | Aman   | Mumbai |




===========================================
FINAL INTERVIEW POINTS
===========================================

Transaction  → One row per transaction (detailed data)
Periodic     → One row per time interval (summary data)
Accumulating → One row per lifecycle/process

===========================================


'''





