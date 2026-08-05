# Simple Neural Network

inputs = [
    [0,0],
    [0,1],
    [1,0],
    [1,1]
]

outputs = [0,0,0,1]

weights = [0.5, 0.5]
bias = -0.7
learning_rate = 0.1

for epoch in range(100):
    for i in range(len(inputs)):
        x1, x2 = inputs[i]
        target = outputs[i]

        output = x1*weights[0] + x2*weights[1] + bias

        if output >= 0:
            prediction = 1
        else:
            prediction = 0

        error = target - prediction

        weights[0] += learning_rate * error * x1
        weights[1] += learning_rate * error * x2
        bias += learning_rate * error

print("Weights:", weights)
print("Bias:", bias)

test = [1,1]
result = test[0]*weights[0] + test[1]*weights[1] + bias

if result >= 0:
    print("Prediction: 1")
else:
    print("Prediction: 0")