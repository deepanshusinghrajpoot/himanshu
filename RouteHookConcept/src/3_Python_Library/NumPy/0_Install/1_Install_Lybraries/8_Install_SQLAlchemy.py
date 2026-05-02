
'''
✅ ✅ Correct Way to Install SQLAlchemy (Windows)


🔹 Step 1 — Check Python Version
---------------------------------

Open Command Prompt:

    python --version

Make sure it shows:
    Python 3.14.x


If multiple versions exist:

    py --list


🔹 Step 2 — Upgrade pip (Recommended)
--------------------------------------

    py -3.14 -m pip install --upgrade pip


Why update pip?
---------------

• Fixes old bugs  
• Supports latest packages  
• Prevents installation errors  


🔹 Step 3 — Install SQLAlchemy (Correct Command)
-----------------------------------------------

    py -3.14 -m pip install SQLAlchemy


👉 Always use:  py -3.14 -m pip  
👉 Do NOT use:  pip install SQLAlchemy  
   (It may install in the wrong Python environment)


🔹 Step 4 — Verify Installation
--------------------------------

    py -3.14 -m pip show SQLAlchemy

Or open Python:

    py -3.14


Then inside Python:

    import sqlalchemy
    print("SQLAlchemy Installed Successfully")


If no error appears → SQLAlchemy installed correctly ✅
'''







"""
📌 Python Libraries for MySQL / Database Connection

1️⃣ SQLAlchemy
--------------------
Role:
- Acts as a high-level ORM (Object Relational Mapper) and database engine layer.
- Provides a uniform interface to connect and interact with multiple databases (MySQL, PostgreSQL, SQLite, etc.).

Uses:
- Create database engine/connection for Pandas or applications.
- Execute SQL queries.
- Map Python objects to database tables (ORM).
- Ideal for production-grade database workflows.

Characteristics:
- Supports multiple databases with one consistent API.
- Fully tested with Pandas read_sql.
- Can be used as ORM or core SQL engine.
- Stable, standard in industry.

Example:
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:@127.0.0.1/world")

--------------------------------------------------

2️⃣ mysql-connector-python
--------------------
Role:
- Official MySQL driver developed by Oracle.
- Connect Python directly to MySQL server without ORM.

Uses:
- Run SQL queries from Python.
- Manage database connections.
- Execute DDL/DML operations.

Characteristics:
- Pure Python implementation, maintained by MySQL team.
- Does not require extra dependencies.
- Can be slower for large-scale queries compared to SQLAlchemy + PyMySQL.

Example:
import mysql.connector
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="world"
)

--------------------------------------------------

3️⃣ PyMySQL
--------------------
Role:
- Third-party MySQL driver written in pure Python.
- Used as a DBAPI driver with SQLAlchemy or directly with Python.

Uses:
- Connect Python to MySQL server.
- Can be used as the driver for Pandas with SQLAlchemy.
- Execute SQL queries, fetch data.

Characteristics:
- Pure Python (no C extensions needed).
- Often used with SQLAlchemy for stable Pandas integration.
- Cross-platform and actively maintained.

Example:
import pymysql
conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="world"
)
"""

"""
| Library                    | Used For in Innovaccer                 | Notes                                     |
| -------------------------- | -------------------------------------- | ----------------------------------------- |
| **mysql-connector-python** | Direct queries from Python scripts     | Official MySQL driver, no ORM             |
| **PyMySQL + SQLAlchemy**   | Data analysis & Pandas `read_sql`      | Most common for data pipelines / analysis |
| **SQLAlchemy ORM**         | App backend with Python object mapping | Used for maintainable production apps     |
"""

