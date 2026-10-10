'''
✅ ✅ Correct Way to Install Plotly (Windows)


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



🔹 Step 3 — Install Plotly (Correct Command)
---------------------------------------------

    py -3.14 -m pip install plotly


👉 Always use:  py -3.14 -m pip  
👉 Do NOT use:  pip install plotly  
   (It may install in the wrong Python environment)



🔹 Step 4 — Verify Installation
--------------------------------

    py -3.14 -m pip show plotly

Or open Python:

    py -3.14


Then inside Python:

    import plotly
    print("Plotly Installed Successfully")


If no error appears → Plotly installed correctly ✅
'''




"""

1️⃣ What is Plotly?
-------------------
Plotly is a Python library used to create
interactive data visualizations.

Features:
• Interactive charts (zoom, hover, pan)
• Works in web browsers
• Supports many chart types
• Used in dashboards and data analysis


Example: Plotly Line Chart
--------------------------
"""




import plotly.express as px
import pandas as pd

data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [200, 300, 250, 400]
})

fig = px.line(data, x="Month", y="Sales", title="Monthly Sales")
fig.show()

