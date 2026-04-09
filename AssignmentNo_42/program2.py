# Same Dataset
X = [1, 2, 3, 4, 5]
Y = [3, 4, 2, 4, 5]

n = len(X)

# Mean
mean_x = sum(X) / n
mean_y = sum(Y) / n

# Slope & Intercept
numerator = sum((X[i] - mean_x) * (Y[i] - mean_y) for i in range(n))
denominator = sum((X[i] - mean_x) ** 2 for i in range(n))
m = numerator / denominator
c = mean_y - m * mean_x

# Predictions
Y_pred = [m * x + c for x in X]

# MSE
mse = sum((Y[i] - Y_pred[i])**2 for i in range(n)) / n

# R² Score
ss_total = sum((Y[i] - mean_y)**2 for i in range(n))
ss_residual = sum((Y[i] - Y_pred[i])**2 for i in range(n))
r2 = 1 - (ss_residual / ss_total)

# Output
print("Actual Y:", Y)
print("Predicted Y:", [round(y, 2) for y in Y_pred])
print("MSE =", round(mse, 3))
print("R² Score =", round(r2, 3))