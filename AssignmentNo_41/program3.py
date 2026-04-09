import math

# Dataset: (Study Hours, Attendance, Result)
data = [
    (2, 60, 'Fail'),
    (5, 80, 'Pass'),
    (6, 85, 'Pass'),
    (1, 50, 'Fail')
]

# Input
study_hours = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance: "))

# Step 1: Calculate distance
distances = []
for sh, att, result in data:
    dist = math.sqrt((study_hours - sh)**2 + (attendance - att)**2)
    distances.append((dist, result))

# Step 2: Sort
distances.sort()

# Step 3: Choose K
k = 3
neighbors = distances[:k]

# Step 4: Voting
votes = {}
for d, result in neighbors:
    votes[result] = votes.get(result, 0) + 1

prediction = max(votes, key=votes.get)

# Output
print("\nPredicted Result:", prediction)