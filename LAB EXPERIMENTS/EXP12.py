from sklearn.neighbors import KNeighborsClassifier

# Petal Length, Petal Width
X = [
    [1.4, 0.2],
    [1.5, 0.2],
    [1.6, 0.3],
    [4.0, 1.3],
    [4.2, 1.4],
    [4.5, 1.5],
    [5.5, 2.0],
    [5.8, 2.1],
    [6.0, 2.2]
]

# 0 = Setosa, 1 = Versicolor, 2 = Virginica
y = [0, 0, 0, 1, 1, 1, 2, 2, 2]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

flower = [[4.3, 1.4]]

result = model.predict(flower)

if result[0] == 0:
    print("Flower: Setosa")
elif result[0] == 1:
    print("Flower: Versicolor")
else:
    print("Flower: Virginica")
