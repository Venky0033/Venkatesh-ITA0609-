from sklearn.linear_model import LinearRegression

# Age, Mileage, Engine Size
X = [
    [1, 10000, 2.0],
    [2, 15000, 2.0],
    [3, 20000, 1.8],
    [4, 30000, 1.6],
    [5, 40000, 1.6],
    [6, 50000, 1.5],
    [7, 60000, 1.4],
    [8, 70000, 1.2]
]

# Price in thousands
y = [18, 17, 15, 13, 11, 9, 7, 6]

model = LinearRegression()
model.fit(X, y)

# New car: age=3 years, mileage=22000, engine=1.8
prediction = model.predict([[3, 22000, 1.8]])

print("Predicted Car Price:", round(prediction[0], 2), "Lakhs")
