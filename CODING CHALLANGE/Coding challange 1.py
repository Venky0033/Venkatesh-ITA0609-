import math

# Construction Worker Dataset
# [Experience in years, Working hours per day]

X = [
    [1, 9],
    [2, 9],
    [2, 10],
    [3, 9],
    [4, 8],
    [5, 8],
    [6, 8],
    [7, 7],
    [8, 7],
    [9, 6]
]

# 0 = Low Productivity
# 1 = High Productivity

Y = [
    0, 0, 0, 0, 0,
    1, 1, 1, 1, 1
]

# Test data
test = [
    [3, 10],
    [5, 9],
    [7, 8],
    [9, 7]
]

# Actual test labels
actual = [0, 1, 1, 1]

# Get K from user
k = int(input("Enter the value of K: "))

predictions = []

# KNN prediction
for point in test:

    distances = []

    # Calculate Euclidean distance
    for i in range(len(X)):

        distance = math.sqrt(
            (point[0] - X[i][0]) ** 2 +
            (point[1] - X[i][1]) ** 2
        )

        distances.append((distance, Y[i]))

    # Sort distances
    distances.sort()

    # Select K nearest neighbors
    nearest = distances[:k]

    # Count classes
    low = 0
    high = 0

    for distance, label in nearest:

        if label == 0:
            low += 1
        else:
            high += 1

    # Majority voting
    if high > low:
        prediction = 1
    else:
        prediction = 0

    predictions.append(prediction)


# Display predictions
print("\nPredicted Class Labels:")

for i in range(len(predictions)):

    if predictions[i] == 0:
        print("Test", i + 1, ": Low Productivity")
    else:
        print("Test", i + 1, ": High Productivity")


# Calculate accuracy
correct = 0

for i in range(len(actual)):

    if predictions[i] == actual[i]:
        correct += 1

accuracy = (correct / len(actual)) * 100

print("\nAccuracy:", accuracy, "%")
