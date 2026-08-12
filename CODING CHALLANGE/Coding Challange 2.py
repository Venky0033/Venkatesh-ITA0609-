import math

# Training data
# [Soil Moisture, Temperature]

X = [
    [20, 34],
    [25, 33],
    [30, 32],
    [35, 31],
    [40, 30],
    [45, 29],
    [50, 28],
    [55, 27],
    [60, 26],
    [65, 25]
]

# 1 = Irrigation Required
# 0 = Irrigation Not Required

Y = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

# Initial values
w1 = 0
w2 = 0
b = 0

learning_rate = 0.1
epochs = 1000


# Sigmoid function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# Gradient Descent
for epoch in range(epochs):

    dw1 = 0
    dw2 = 0
    db = 0

    for i in range(len(X)):

        x1 = X[i][0]
        x2 = X[i][1]
        y = Y[i]

        # Prediction
        z = w1 * x1 + w2 * x2 + b

        p = sigmoid(z)

        # Error
        error = p - y

        # Gradients
        dw1 = dw1 + error * x1
        dw2 = dw2 + error * x2
        db = db + error

    # Update weights
    w1 = w1 - learning_rate * dw1 / len(X)
    w2 = w2 - learning_rate * dw2 / len(X)
    b = b - learning_rate * db / len(X)


print("Final Weight 1 =", round(w1, 4))
print("Final Weight 2 =", round(w2, 4))
print("Final Bias =", round(b, 4))


# Test data
test = [
    [22, 34],
    [38, 30],
    [48, 28],
    [58, 26],
    [64, 25]
]

actual = [1, 1, 0, 0, 0]

predictions = []

print("\nTest Results:")

for i in range(len(test)):

    x1 = test[i][0]
    x2 = test[i][1]

    z = w1 * x1 + w2 * x2 + b

    probability = sigmoid(z)

    if probability >= 0.5:
        prediction = 1
    else:
        prediction = 0

    predictions.append(prediction)

    print(
        "Soil Moisture =", x1,
        "Temperature =", x2,
        "Sigmoid =", round(probability, 4),
        "Class =", prediction
    )


# Accuracy
correct = 0

for i in range(len(actual)):
    if predictions[i] == actual[i]:
        correct += 1

accuracy = correct / len(actual) * 100

print("\nAccuracy =", accuracy, "%")
