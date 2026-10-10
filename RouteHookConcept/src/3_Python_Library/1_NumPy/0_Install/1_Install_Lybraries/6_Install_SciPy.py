'''
📦 What is SciPy?
==================
SciPy is an open-source Python library used for scientific and technical computing.
It is built on top of NumPy and provides many advanced mathematical algorithms.

👉 In simple terms:

NumPy → handles arrays and basic math
SciPy → provides advanced scientific functions


🧠 Why SciPy is Used
---------------------

SciPy is used for tasks like:

Advanced mathematics
Statistics
Optimization
Signal processing
Image processing
Scientific simulations
Clustering algorithms (used by sns.clustermap())




✅ ✅ Correct Way to Install SciPy (Windows)
=============================================

🔹 Step 1 — Check Python Version
---------------------------------

Open Command Prompt:

    python --version

Make sure it shows:
    Python 3.14.x


If multiple Python versions exist:

    py --list



🔹 Step 2 — Upgrade pip (Recommended)
--------------------------------------

    py -3.14 -m pip install --upgrade pip


Why update pip?
---------------

• Fixes installation bugs  
• Supports latest packages  
• Avoids dependency conflicts  



🔹 Step 3 — Install SciPy
--------------------------

    py -3.14 -m pip install scipy


👉 Always use:

    py -3.14 -m pip

instead of

    pip install scipy

because `pip` may install packages in the wrong Python environment.



🔹 Step 4 — Verify Installation
--------------------------------

Check installation:

    py -3.14 -m pip show scipy


Or open Python:

    py -3.14


Then inside Python:

    import scipy
    print("SciPy Installed Successfully")


If no error appears → SciPy installed correctly ✅
'''




"""
2️⃣ What is SciPy?
------------------
SciPy is a Python library used for
scientific and mathematical computing.

SciPy is built on top of NumPy.

Main Uses:
• Statistics
• Optimization
• Linear algebra
• Signal processing
• Scientific calculations


Example: Mean using SciPy
-------------------------
"""

from scipy import stats

data = [10, 20, 30, 40, 50]

mean_value = stats.tmean(data)

print("Mean:", mean_value)

