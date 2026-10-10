'''
✅ ✅ Correct Way to Install PyMySQL (Windows)


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


🔹 Step 3 — Install PyMySQL (Correct Command)
---------------------------------------------

    py -3.14 -m pip install PyMySQL


👉 Always use:  py -3.14 -m pip  
👉 Do NOT use:  pip install PyMySQL  
   (It may install in the wrong Python environment)


🔹 Step 4 — Verify Installation
--------------------------------

    py -3.14 -m pip show PyMySQL

Or open Python:

    py -3.14


Then inside Python:

    import pymysql
    print("PyMySQL Installed Successfully")


If no error appears → PyMySQL installed correctly ✅
'''