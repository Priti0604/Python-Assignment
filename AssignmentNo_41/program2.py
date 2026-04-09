import math

# Same dataset
data = [
    (1, 2, 'Red'),
    (2, 3, 'Red'),
    (3, 1, 'Blue'),
    (6, 5, 'Blue')
]

# Input (same as assignment)
x, y = 2, 2

# Distance calculation
distances = []
for px, py, label in data:
    dist = math.sqrt((x - px)**2 + (y - py)**2)
    distances.append((dist, label))

# Sort distances
distances.sort()

def predict(k):
    neighbors = distances[:k]
    votes = {}
    for d, label in neighbors:
        votes[label] = votes.get(label, 0) + 1
    return max(votes, key=votes.get)

# Results
print("Prediction Results\n")

for k in [1, 3, 5]:
    result = predict(k)
    print(f"K = {k} → {result}")