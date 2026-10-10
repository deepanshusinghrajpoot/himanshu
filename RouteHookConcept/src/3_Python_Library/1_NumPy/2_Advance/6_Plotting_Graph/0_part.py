# ==========================================
# NumPy & Plotting with Matplotlib
# ==========================================

# Purpose:
# - NumPy: numerical computation and data generation
# - Matplotlib: visualize data using plots

import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1️⃣ Generating Data
# ==========================================

# np.linspace(start, end, num_points) -> generates evenly spaced points
x = np.linspace(-10, 10, 100)  # 100 points from -10 to 10

# ==========================================
# 2️⃣ Plotting Basic Graphs
# ==========================================

# Syntax:
# plt.plot(x, y)
# plt.show()
# x -> independent variable
# y -> dependent variable

# ------------------------------------------
# Linear function y = x
y = x
plt.plot(x, y)
plt.title("Linear Function: y = x")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# Diagram (Linear):
# y
#  |       *
#  |      *
#  |     *
#  |    *
#  |   *
#  |  *
#  +---------------- x
# 0

# ------------------------------------------
# Quadratic function y = x^2
y = x**2
plt.plot(x, y)
plt.title("Quadratic Function: y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# Diagram (Quadratic):
# y
#  |       *
#  |      *   *
#  |     *       *
#  |   *           *
#  | *               *
#  +---------------------- x
# 0

# ------------------------------------------
# Sine function y = sin(x)
y = np.sin(x)
plt.plot(x, y)
plt.title("Sine Function: y = sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# Diagram (Sine):
# y
# 1 |    *     *     *
# 0 | *     *     *    
# -1|    *     *     *
#  +-------------------- x

# ------------------------------------------
# x log(x) function y = x * log(x)
# Note: Avoid x <= 0 (log undefined)
x_pos = np.linspace(0.1, 10, 100)  # start from 0.1 to avoid log(0)
y = x_pos * np.log(x_pos)
plt.plot(x_pos, y)
plt.title("Function: y = x * log(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# Diagram (x*log(x)):
# y
#  |
#  |      *
#  |     *
#  |    *
#  |   *
#  |  *
#  +---------------- x
# 0

# ------------------------------------------
# Sigmoid function y = 1 / (1 + e^-x)
y = 1 / (1 + np.exp(-x))
plt.plot(x, y)
plt.title("Sigmoid Function: y = 1 / (1 + e^-x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# Diagram (Sigmoid):
# y
# 1 |**************
# 0 |       ********
#  +---------------- x

# ==========================================
# 3️⃣ Quick Tips
# ==========================================
# - Always import NumPy as np and matplotlib.pyplot as plt
# - Use np.exp(), np.sin(), np.log() for element-wise operations
# - Use linspace to generate smooth curves
# - Check domain of functions like log(x) to avoid errors
# - Sigmoid curve is important in Machine Learning for probabilities