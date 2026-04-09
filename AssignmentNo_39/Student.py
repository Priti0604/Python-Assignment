# ==============================
# 1. IMPORT LIBRARIES
# ==============================
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# ==============================
# 2. LOAD DATASET
# ==============================
df = pd.read_csv("student_performance_ml.csv")

print("First 5 rows:\n", df.head())

# ==============================
# 3. DATA ANALYSIS
# ==============================
print("\nDataset Shape:", df.shape)
print("\nColumn Names:", df.columns)

print("\nAverage StudyHours:", df['StudyHours'].mean())
print("Average Attendance:", df['Attendance'].mean())

# ==============================
# 4. VISUALIZATION
# ==============================
plt.hist(df['StudyHours'])
plt.title("Study Hours Distribution")
plt.xlabel("StudyHours")
plt.ylabel("Frequency")
plt.show()

# ==============================
# 5. TRAIN-TEST SPLIT
# ==============================
X = df[['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours']]
y = df['FinalResult']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# ==============================
# 6. MODEL TRAINING
# ==============================
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# ==============================
# 7. PREDICTION
# ==============================
y_pred = model.predict(X_test)

print("\nPredicted values:", y_pred)
print("Actual values:", y_test.values)

# ==============================
# 8. ACCURACY CALCULATION
# ==============================
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy * 100, "%")

# ==============================
# 9. CONFUSION MATRIX
# ==============================
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", cm)

ConfusionMatrixDisplay(cm).plot()
plt.show()

# ==============================
# 10. TRAINING VS TEST ACCURACY
# ==============================
train_acc = accuracy_score(y_train, model.predict(X_train))
test_acc = accuracy_score(y_test, y_pred)

print("\nTraining Accuracy:", train_acc)
print("Testing Accuracy:", test_acc)

# ==============================
# 11. DIFFERENT DEPTH MODELS
# ==============================
depths = [1, 3, None]

for d in depths:
    model = DecisionTreeClassifier(max_depth=d)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)
    print(f"Accuracy with max_depth={d}:", acc)

# ==============================
# 12. NEW STUDENT PREDICTION
# ==============================
new_student = [[6, 85, 66, 7, 7]]

result = model.predict(new_student)

if result[0] == 1:
    print("\nNew Student Result: PASS")
else:
    print("\nNew Student Result: FAIL")