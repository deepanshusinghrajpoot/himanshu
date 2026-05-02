

# How to install NumPy
#======================


#(1) check version of python
#----------------------------

# python --version



#(2) check pip version
#----------------------

# gpt explain what is pip

# py -m pip --version




#(3) Update pip version
#----------------------

# gpt why update pip before install the NumPy library

# python -m pip install --upgrade pip --user

# OR

# python.exe -m pip install --upgrade pip

# OR

# py -3.14 -m pip install numpy





#(4) Now install the NumPy libraray
#------------------------------------

# py -m pip install numpy




#(5) Open IDLE (window search) 
#--------------

# import numpy as np


#(6) check version in IDLE
#--------------------------

# np.__version__







"""



✅ ✅ Correct Way to Install NumPy (Windows)


🔹 Step 1 — Check Python Version
---------------------------------

Open Command Prompt: python --version

Make sure it shows:   Python 3.14.x



If multiple versions exist:

py --list





🔹 Step 2 — Upgrade pip (Recommended)
--------------------------------------

py -3.14 -m pip install --upgrade pip

Why update pip?
...............

Fixes old bugs
Supports latest packages
Prevents installation errors




🔹 Step 3 — Install NumPy (Correct Command)
--------------------------------------------

py -3.14 -m pip install numpy


👉 Always use py -3.14 -m pip
👉 Do NOT use just pip install numpy (can install in wrong Python)






🔹 Step 4 — Verify Installation
--------------------------------

py -3.14 -m pip show numpy

Or:

py -3.14






Then inside Python:
-------------------

import numpy as np
print(np.__version__)








"""