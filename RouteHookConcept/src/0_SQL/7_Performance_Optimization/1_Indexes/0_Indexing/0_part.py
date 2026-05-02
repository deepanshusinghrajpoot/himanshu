

'''
# =========================================================
# Indexing Fundamentals — PART 1
# =========================================================

# Interview-Friendly Definition
# -----------------------------
# Before understanding how indexing works in DBMS, we must
# understand how table data is physically stored in memory
# and how the database organizes that data internally.


# =========================================================
# Key Concepts to Understand Before Indexing
# =========================================================

Index is performantion Optimization techniques.

#lll   “Sir, I want explain indexing in a step-by-step manner.”

#      1. How table data (rows) are actually stored?
#      2. What data structure is used for indexing and how it works?
#      3. What types of indexing are present?


# After understanding these concepts, we can combine them
# to understand how DBMS performs indexing internally.


# =========================================================
# 1. Logical Representation of Table Data
# =========================================================

# Example Table
#---------------

# Emp ID      Name       Address
# 1           A          City A
# 2           B          City B
# 3           C          City C
# 4           D          City D

# Important
# ---------
#lll This is only a logical representation of data.
#    Actual data is NOT stored in this tabular format in memory.


# =========================================================
# 2. How DBMS Actually Stores Table Data
# =========================================================
#
#      In DBMS, table data rows are stored inside Data Pages.
#      Data Pages are stored inside Data Blocks.
#      And these Data Blocks are stored on disk (loaded into memory when required).

#      And Data Page is a fixed-size memory structure that
#      stores multiple table rows.
#      it has memory size usually around 8KB (8192 bytes)
#      But it may vary depending on the DBMS.


# =========================================================
# Structure of a Data Page
# =========================================================

# Example Data Page Layout

#lll Data Page has tree main part 
#        First header
#        Second Data Records
#        Offset array


#                ................
#                |   Header    |
#      96 bytes  |             | ---> Page Number
#                |             | ---> Free Space Info
#                |             | ---> Checksum etc.
#                ................
#   8KB Total    |   Data      |
#   (8192 bytes) |   Records   |
#                |             | ---> Actual table rows stored here
#     8060 bytes |             |
#                ................
#                |   Offset    |
#      36 bytes  |   Array     | ---> Pointer array to each record
#                ................



# 1 KB is 1024 bytes


# lll Explanation
# ----------------

# 1. Header
#    Contains metadata about the page:
#    • Page ID
#    • Free space information
#    • Integrity checks

# 2. Data Records
#    Contains table rows.

# 3. Offset Array
#    Contains pointers to each row stored in the page.




# =========================================================
# Example: Row Storage in Data Page
# =========================================================

# Suppose each table row is 64 bytes.

# Example rows

# Emp ID      Name       Address
# 1           A          City A
# 2           B          City B
# 3           C          City C
# 4           D          City D

# Each row ≈ 64 bytes

# If page size ≈ 8KB (8060 usable bytes)

# Approx rows per page:

# 8060 / 64 ≈ 125 rows per data page


# =========================================================
# Example Representation of Data Page
# =========================================================

#        ...............
#        PageID : 1
#        ...............
#        Row1
#        ...............
#        Row2
#        ...............
#        Row3
#        ...............
#        Row4
#        ...............
#        Row5
#        ...............


# Offset Array (Pointer Table)

#        ...............
#        |R1|R3|R5|R4|R2|
#        ...............

# Explanation
# -----------

# Offset array stores pointers to row locations.

# This allows the DBMS to:
# • Quickly locate rows
# • Rearrange records without moving actual data


# =========================================================
# Multiple Data Pages for One Table
# =========================================================

# For large tables, DBMS creates multiple data pages.

# Example

# Page 1 → Rows 1 – 125
# Page 2 → Rows 126 – 250
# Page 3 → Rows 251 – 375
# ...


# DBMS manages these pages internally.


# =========================================================
# Where Are Data Pages Stored?
# =========================================================

# Data Pages are stored inside:
#             • Data Blocks


# =========================================================
# What is a Data Block?
# =========================================================

# Definition
# ----------
# A Data Block is the minimum amount of data that can
# be read or written during a disk I/O operation.

# Managed By
# ----------
# Data Blocks are controlled by the storage system
# (like hard disk or SSD), not by the DBMS.


# Typical Data Block Size
# -----------------------

# Usually between:

# 4KB → 32KB

# Most common size:
# 8KB


# =========================================================
# Relationship Between Data Pages and Data Blocks
# =========================================================

# One Data Block can store one or multiple Data Pages.

# Interview-Friendly Definition
# -----------------------------
#lll DBMS also maintains a mapping between Data Pages and Data Blocks
#    so that it can locate where the actual table data is stored
#    on the disk.

# Example Mapping

# Data Page 1  → Data Block 1
# Data Page 2  → Data Block 1
# Data Page 3  → Data Block 2
# Data Page 4  → Data Block 2


# =========================================================
# Important Concept
# =========================================================

# DBMS Controls:
# --------------
# • Data Pages
# • Row placement inside pages
# • Order of pages

# Storage System Controls:
# ------------------------
# • Data Blocks
# • Physical disk layout

# Therefore, data blocks may be scattered across the disk.


# =========================================================
# Quick Revision Points
# =========================================================

# ✔ Tables are logically represented as rows and columns
# ✔ Physically stored inside Data Pages
# ✔ Data Page size is typically around 8KB
# ✔ Each Data Page stores multiple rows
# ✔ Offset array stores pointers to rows
# ✔ Data Pages are stored inside Data Blocks
# ✔ Data Block is the minimum I/O unit on disk
'''







