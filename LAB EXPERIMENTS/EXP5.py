# Simple KNN

data = [
    [2,3,"A"],
    [3,4,"A"],
    [6,7,"B"],
    [7,8,"B"]
]

test = [4,5]
k = 3

distances = []

for row in data:
    x, y, label = row
    d = ((x-test[0])**2 + (y-test[1])**2) ** 0.5
    distances.append([d, label])

distances.sort()

countA = 0
countB = 0

for i in range(k):
    if distances[i][1] == "A":
        countA += 1
    else:
        countB += 1

if countA > countB:
    print("Predicted Class: A")
else:
    print("Predicted Class: B")