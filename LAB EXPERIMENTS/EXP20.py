# EXPERIMENT 20
# Future Sales Prediction

import pandas as pd

from sklearn.linear_model import LinearRegression

# Monthly sales data

data = {
    'Month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],

    'Sales': [
        12000,
        13500,
        14200,
        15000,
        16500,
        17200,
        18000,
        19500,
        20500,
        21800,
        23000,
        24500
    ]
}

df = pd.DataFrame(data)

# Input
X = df[['Month']]

# Output
y = df['Sales']

# Create Linear Regression model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict next month
future_month = [[13]]

prediction = model.predict(future_month)

print("Predicted Sales for Month 13:",
      round(prediction[0], 2))

# Show all predictions
df['Predicted Sales'] = model.predict(X)

print("\nSales Prediction Table:")
print(df)

# Graph
import matplotlib.pyplot as plt

plt.scatter(X, y)
plt.plot(X, model.predict(X))

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Future Sales Prediction")

plt.show()
