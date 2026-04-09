#1. Load Dataset & Basic Info

import pandas as pd
df = pd.read_csv("student_performance_ml.csv")
print("First 5 records:\n", df.head())
print("\nLast 5 records:\n", df.tail())
print("\nShape of dataset:", df.shape)
print("\nColumns:", df.columns)
print("\nData types:\n", df.dtypes)


#2. Count Students, Pass & Fail

print("Total students:", len(df))

passed = df[df['FinalResult'] == 1]
print("Passed students:", len(passed))

failed = df[df['FinalResult'] == 0]
print("Failed students:", len(failed))

#3. Statistical Calculations

print("Average StudyHours:", df['StudyHours'].mean())
print("Average Attendance:", df['Attendance'].mean())
print("Max PreviousScore:", df['PreviousScore'].max())
print("Min SleepHours:", df['SleepHours'].min())

#4. Value Counts & Percentage

counts = df['FinalResult'].value_counts()
print("Counts:\n", counts)

percentage = (counts / len(df)) * 100
print("\nPercentage:\n", percentage)

#5. Histogram of StudyHours

import matplotlib.pyplot as plt

plt.hist(df['StudyHours'])
plt.title("StudyHours Distribution")
plt.xlabel("Study Hours")
plt.ylabel("Frequency")
plt.show()

#6.Scatter Plot

colors = df['FinalResult'].map({1: 'green', 0: 'red'})

plt.scatter(df['StudyHours'], df['PreviousScore'], c=colors)
plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
plt.title("StudyHours vs PreviousScore")
plt.show()

#7. Boxplot for Attendance

plt.boxplot(df['Attendance'])
plt.title("Attendance Boxplot")
plt.show()

#8. Assignments vs FinalResult

import seaborn as sns

sns.boxplot(x='FinalResult', y='AssignmentsCompleted', data=df)
plt.title("Assignments vs Result")
plt.show()

#9.. SleepHours vs FinalResult

sns.boxplot(x='FinalResult', y='SleepHours', data=df)
plt.title("SleepHours vs Result")
plt.show()



