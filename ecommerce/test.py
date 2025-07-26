# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample training data (features and labels)
# x needs to be 2D for sklearn, so we reshape it
x = np.array([1, 2, 3, 4, 5]).reshape(5, 1)

y = np.array([2, 4, 5, 4, 5])

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(x, y)

# Predict y for new x values
x_test = np.array([6, 7, 8]).reshape(3, 1)
y_pred = model.predict(x_test)

# Print model parameters
print("Slope (m):", model.coef_[0])
print("Intercept (c):", model.intercept_)
print("Predictions:", y_pred)

# Plot
plt.scatter(x, y, color='blue', label='Training data')
plt.plot(x, model.predict(x), color='red', label='Regression line')
plt.scatter(x_test, y_pred, color='green', label='Predictions')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression Example")
plt.show()
