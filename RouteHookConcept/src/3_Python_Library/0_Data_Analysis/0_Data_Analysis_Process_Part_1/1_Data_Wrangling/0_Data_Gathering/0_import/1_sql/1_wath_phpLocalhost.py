"""
🟢 What is localhost/phpmyadmin ?

phpMyAdmin is a **web-based interface used to manage MySQL / MariaDB databases**.
It runs through your browser when using XAMPP.

URL:
    http://localhost/phpmyadmin/

It allows you to **control and manage databases visually** without writing many SQL commands.

---

🟢 Role of phpMyAdmin

1️⃣ Database Management
    - Create new databases
    - Delete databases
    - Rename databases

2️⃣ Table Management
    - Create tables
    - Edit table structure
    - Delete tables
    - Add or remove columns

3️⃣ Data Management
    - Insert records (rows)
    - Update records
    - Delete records
    - View stored data

4️⃣ SQL Query Execution
    - Run SQL queries directly
    - Example:
        SELECT * FROM city;
        SELECT * FROM country;

5️⃣ Import & Export Data
    - Import SQL files
    - Export database to:
        • SQL
        • CSV
        • JSON
        • Excel

6️⃣ User Management
    - Create database users
    - Set passwords
    - Manage permissions

7️⃣ Backup & Restore
    - Export full database backup
    - Restore database from SQL file

---

🟢 How It Works

Browser
   ↓
http://localhost/phpmyadmin
   ↓
Apache Server (XAMPP)
   ↓
MySQL / MariaDB Database

---

🟢 Role for Python Developers

phpMyAdmin is mainly used to:

✔ Create databases  
✔ Create tables  
✔ Insert test data  
✔ Check query results  

Then Python connects to that database using libraries like:

    pymysql
    mysql-connector-python
    sqlalchemy

Example Python Connection:

    host = "127.0.0.1"
    user = "root"
    database = "world"

---

✅ Summary

phpMyAdmin = **GUI tool to manage MySQL databases in browser**

Python → connects to MySQL  
phpMyAdmin → manages the database visually
"""