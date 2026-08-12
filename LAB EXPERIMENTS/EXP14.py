from sklearn.linear_model import LinearRegression

# Area in sq.ft, Bedrooms, Age of house
X = [
    [800, 2, 10],
    [1000, 2, 8],
    [1200, 3, 7],
    [1400, 3, 5],
    [1600, 3, 4],
    [1800, 4, 3],
    [2000, 4, 2],
    [2200, 4, 1]
]

# Price in Lakhs
y = [30, 35, 40, 48, 55, 65, 75, 85]

model = LinearRegression()
model.fit(X, y)

# New house
prediction = model.predict([[1500, 3, 5]])

print("Predicted House Price:", round(prediction[0], 2), "Lakhs")
