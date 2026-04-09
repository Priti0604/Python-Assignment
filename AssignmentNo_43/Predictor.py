# Step 1: Import required libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 2: Get Data
data = pd.read_csv("PlayPredictor.csv")   # make sure file is in same folder

# Display dataset
print("Dataset:\n", data)

# Step 3: Clean, Prepare and Manipulate Data
le = LabelEncoder()

# Convert categorical data to numeric
data['Weather'] = le.fit_transform(data['Weather'])
data['Temperature'] = le.fit_transform(data['Temperature'])
data['Play'] = le.fit_transform(data['Play'])   # Yes=1, No=0

# Features and Labels
X = data[['Weather', 'Temperature']]
y = data['Play']

# Step 4: Split data (Training & Testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

# Step 5: Train Model using KNN (K = 3)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Step 6: Test Model
y_pred = model.predict(X_test)

print("\nPredicted Values:", y_pred)
print("Actual Values   :", list(y_test))

# Step 7: Accuracy Calculation
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)

# Step 8: Manual Prediction
# Example: Weather=Sunny, Temperature=Hot
# (Encoding depends on LabelEncoder mapping, so use transformed values)
sample = [[0, 0]]   # change values accordingly
result = model.predict(sample)

if result[0] == 1:
    print("\nPrediction: Yes")
else:
    print("\nPrediction: No")