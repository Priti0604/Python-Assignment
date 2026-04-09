import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv("PlayPredictor.csv")

# Drop unwanted column
data = data.drop(columns=['Unnamed: 0'])

le = LabelEncoder()

# Correct column names
data['Whether'] = le.fit_transform(data['Whether'])
data['Temperature'] = le.fit_transform(data['Temperature'])
data['Play'] = le.fit_transform(data['Play'])

X = data[['Whether', 'Temperature']]
y = data['Play']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))