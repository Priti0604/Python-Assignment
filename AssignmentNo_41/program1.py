import math

# Dataset
data = [
    ('A', 1, 2, 'Red'),
    ('B', 2, 3, 'Red'),
    ('C', 3, 1, 'Blue'),
    ('D', 6, 5, 'Blue')
]

# Input
x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))

# Step 1: Calculate Euclidean Distance
distances = []
for point in data:
    name, px, py, label = point
    dist = math.sqrt((x - px)**2 + (y - py)**2)
    distances.append((name, dist, label))

# Step 2: Sort distances
distances.sort(key=lambda d: d[1])

# Step 3: Select K nearest neighbors
k = 3
neighbors = distances[:k]

# Step 4: Majority voting
votes = {}
for n in neighbors:
    label = n[2]
    votes[label] = votes.get(label, 0) + 1

predicted_class = max(votes, key=votes.get)

# Output
print("\nNearest Neighbors:")
for n in neighbors:
    print(f"{n[0]} - Distance: {round(n[1], 2)}")

print("\nPredicted Class:", predicted_class)