import numpy as np
import matplotlib.pyplot as plt

# Define the sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Generate x values
x = np.linspace(-10, 10, 100)  # Range from -10 to 10 with 100 points

# Calculate sigmoid values
y = sigmoid(x)

# Plot the sigmoid function
plt.figure(figsize=(8, 5))#hello
plt.plot(x, y, label="Sigmoid Function", color="blue")
plt.title("Sigmoid Function")
plt.xlabel("x")
plt.ylabel("Sigmoid(x)")
plt.grid()
plt.axhline(0.5, color='red', linestyle='--', linewidth=0.8, label="y = 0.5")
plt.legend()
plt.show()
