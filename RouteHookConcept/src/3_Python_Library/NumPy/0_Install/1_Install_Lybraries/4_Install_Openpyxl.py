"""



📦 Role of openpyxl in Python

openpyxl is a Python library used to read, write, and modify Excel .xlsx files.

When you work with Excel files in pandas, pandas uses 
openpyxl as the engine to handle .xlsx files.





✅ ✅ Correct Way to Install openpyxl (Windows)


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



🔹 Step 3 — Install openpyxl (Correct Command)
-----------------------------------------------

    py -3.14 -m pip install openpyxl


👉 Always use:  py -3.14 -m pip  
👉 Do NOT use:  pip install openpyxl  
   (It may install in the wrong Python environment)



🔹 Step 4 — Verify Installation
--------------------------------

    py -3.14 -m pip show openpyxl

Or open Python:

    py -3.14


Then inside Python:

    import openpyxl
    print("openpyxl Installed Successfully")


If no error appears → openpyxl installed correctly ✅

"""