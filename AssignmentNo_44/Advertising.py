import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("Advertising.csv")

# Drop extra column
data = data.drop(columns=['Unnamed: 0'])

# Features and target
X = data[['TV', 'radio', 'newspaper']]
y = data['sales']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print("Predicted Sales:", y_pred)