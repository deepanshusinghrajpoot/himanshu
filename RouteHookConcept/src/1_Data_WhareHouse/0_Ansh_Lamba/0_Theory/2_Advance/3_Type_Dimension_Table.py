
'''


===========================================
Types of Dimension Tables
===========================================


-- =========================================
-- 1. Conformed Dimension
-- =========================================

-- Definition:
-- A conformed dimension is a dimension that is shared across multiple fact tables.
-- It has the same structure, meaning, and values in all places it is used.

-- Real-World Example:

DimDate
-------------------------------
| date_key | date       | month | year |
-------------------------------
| D101     | 2026-01-01 | Jan   | 2026 |
| D102     | 2026-01-02 | Jan   | 2026 |

-- Used in multiple fact tables:

FactSales
-------------------------------
| date_key | sales_amount |
-------------------------------
| D101     | 5000         |

FactOrders
-------------------------------
| date_key | order_count |
-------------------------------
| D101     | 10          |

-- Same DimDate is shared → Conformed Dimension



-- =========================================
-- 2. Role Playing Dimension
-- =========================================

-- Definition:
-- A role-playing dimension is a single dimension that is used multiple times
-- in a fact table with different roles.

-- Real-World Example:

DimDate
-------------------------------
| date_key | date       |
-------------------------------
| D101     | 2026-01-01 |
| D102     | 2026-01-02 |

FactOrder
-----------------------------------------------------------
| order_id | order_date_key | ship_date_key | delivery_date_key |
-----------------------------------------------------------
| 1001     | D101           | D102          | D103              |

-- Same DimDate used as:
-- Order Date, Ship Date, Delivery Date → Role Playing



-- =========================================
-- 3. Junk Dimension
-- =========================================

-- Definition:
-- A junk dimension is a collection of small, low-cardinality attributes
-- (like flags or indicators) combined into a single dimension table.

-- Real-World Example:

DimJunk
---------------------------------------------------
| junk_key | is_active | is_returned | payment_mode |
---------------------------------------------------
| J1       | Yes       | No          | COD          |
| J2       | No        | Yes         | Card         |

FactSales
-------------------------------
| order_id | junk_key | amount |
-------------------------------
| 1001     | J1       | 5000   |

-- Combines multiple flags into one table → Junk Dimension



-- =========================================
-- 4. Degenerate Dimension
-- =========================================

-- Definition:
-- A degenerate dimension is a dimension attribute stored directly in the
-- fact table without a separate dimension table.

-- Real-World Example:

FactSales
---------------------------------------------------------
| order_id | customer_id | product_id | amount |
---------------------------------------------------------
| 1001     | C101        | P501       | 5000   |
| 1002     | C102        | P502       | 3000   |

-- order_id acts as a dimension but no separate table exists
-- → Degenerate Dimension




===========================================
FINAL INTERVIEW REVISION
===========================================

Conformed Dimension   → Shared across multiple fact tables
Role Playing Dimension→ Same dimension, multiple roles
Junk Dimension        → Combined small flags/attributes
Degenerate Dimension  → Dimension stored in fact table

===========================================


'''