import numpy as np


# ====================================================
# Working with Mathematical Formulas using NumPy
# ====================================================

a = np.arange(10)

print(a)
# [0 1 2 3 4 5 6 7 8 9]


# ====================================================
# Sigmoid Function
# ====================================================

# Sigmoid formula:
# 1 / (1 + e^(-x))

def sigmoid(array):
    return 1 / (1 + np.exp(-array))

print(sigmoid(a))

# Output
# [0.5        0.73105858 0.88079708 0.95257413 0.98201379
#  0.99330715 0.99752738 0.99908895 0.99966465 0.99987661]



# ====================================================
# Mean Squared Error (MSE)
# ====================================================

# Formula:
# MSE = (1/n) * Σ (yi - ŷi)^2

# Where:
# n   = total number of observations
# yi  = actual value
# ŷi  = predicted value

# MSE measures the average squared difference
# between actual and predicted values.

actual = np.random.randint(1, 50, 25)
predicted = np.random.randint(1, 50, 25)

print("Actual values:", actual)
print("Predicted values:", predicted)

def mse(actual, predicted):
    return np.mean((actual - predicted) ** 2)

print("MSE:", mse(actual, predicted))



# ====================================================
# Binary Cross Entropy (BCE)
# ====================================================

# BCE is a loss function used in binary classification.

# Formula:
# BCE = -(1/n) * Σ [ yi * log(ŷi) + (1 - yi) * log(1 - ŷi) ]

# Where:
# yi  = actual label (0 or 1)
# ŷi  = predicted probability (0 to 1)

# If yi = 1 → Loss = -log(ŷi)
# If yi = 0 → Loss = -log(1 - ŷi)

# Example

y_actual = np.array([1, 0, 1])
y_pred = np.array([0.9, 0.2, 0.8])  # predicted probabilities

bce = -np.mean(
    y_actual * np.log(y_pred) +
    (1 - y_actual) * np.log(1 - y_pred)
)

print("Binary Cross Entropy:", bce)

# Binary Cross Entropy: 0.18388253942874858