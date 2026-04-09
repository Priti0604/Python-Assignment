# Dataset
X = [1, 2, 3, 4, 5]
Y = [3, 4, 2, 4, 5]

n = len(X)

# Mean of X and Y
mean_x = sum(X) / n
mean_y = sum(Y) / n

# Slope (m)
numerator = sum((X[i] - mean_x) * (Y[i] - mean_y) for i in range(n))
denominator = sum((X[i] - mean_x) ** 2 for i in range(n))
m = numerator / denominator

# Intercept (c)
c = mean_y - m * mean_x

# Output
print("Mean of X =", mean_x)
print("Mean of Y =", mean_y)
print("Slope (m) =", round(m, 2))
print("Intercept (c) =", round(c, 2))

# Equation
print("\nRegression Equation:")
print(f"Y = {round(m,2)}X + {round(c,2)}")

# Prediction
x_new = 6
y_pred = m * x_new + c
print("\nPredicted Y for X = 6:", round(y_pred, 2))