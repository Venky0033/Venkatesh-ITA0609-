from sklearn.naive_bayes import GaussianNB

# Length, Width
X = [
    [2.0, 1.0],
    [2.2, 1.1],
    [2.4, 1.2],
    [4.0, 2.0],
    [4.2, 2.1],
    [4.4, 2.2],
    [6.0, 3.0],
    [6.2, 3.1],
    [6.4, 3.2]
]

# 0 = Flower A, 1 = Flower B, 2 = Flower C
y = [0, 0, 0, 1, 1, 1, 2, 2, 2]

model = GaussianNB()
model.fit(X, y)

flower = [[4.3, 2.1]]

result = model.predict(flower)

if result[0] == 0:
    print("Flower: Flower A")
elif result[0] == 1:
    print("Flower: Flower B")
else:
    print("Flower: Flower C")
