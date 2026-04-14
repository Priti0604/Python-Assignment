# Step 1: Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Step 2: Load dataset
data = pd.read_csv("WinePredictor.csv")

# Step 3: Separate features and target (last column = target)
X = data.iloc[:, :-1]   # all columns except last
y = data.iloc[:, -1]    # last column

# Step 4: Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Scale data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 6: Train model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# Step 7: Predict
y_pred = model.predict(X_test)

# Step 8: Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)