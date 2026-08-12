# ==========================================================
# Compare Linear Regression and Polynomial Regression
# Dataset: Package Weight vs Delivery Cost
# ==========================================================

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# ----------------------------------------------------------
# Step 1: Create Dataset
# ----------------------------------------------------------
data = {
    'Package_Weight': [1,2,3,4,5,6,7,8,9,10,
                       11,12,13,14,15,16,17,18,19,20],

    'Delivery_Cost': [50,55,62,70,82,97,115,136,160,188,
                      220,255,295,340,390,445,505,570,640,715]
}

df = pd.DataFrame(data)

print("="*55)
print("PACKAGE WEIGHT DATASET")
print("="*55)
print(df)

# ----------------------------------------------------------
# Step 2: Features and Target
# ----------------------------------------------------------
X = df[['Package_Weight']]
y = df['Delivery_Cost']

# ----------------------------------------------------------
# Step 3: Split Dataset
# ----------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==========================================================
# LINEAR REGRESSION
# ==========================================================
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

linear_pred = linear_model.predict(X_test)

print("\n")
print("="*55)
print("LINEAR REGRESSION")
print("="*55)
print("Slope:", linear_model.coef_[0])
print("Intercept:", linear_model.intercept_)
print("Mean Squared Error:", mean_squared_error(y_test, linear_pred))
print("R2 Score:", r2_score(y_test, linear_pred))

# ==========================================================
# POLYNOMIAL REGRESSION
# ==========================================================
poly = PolynomialFeatures(degree=2)

X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_poly_train, y_train)

poly_pred = poly_model.predict(X_poly_test)

print("\n")
print("="*55)
print("POLYNOMIAL REGRESSION")
print("="*55)
print("Mean Squared Error:", mean_squared_error(y_test, poly_pred))
print("R2 Score:", r2_score(y_test, poly_pred))

# ==========================================================
# Prediction
# ==========================================================
new_weight = pd.DataFrame({'Package_Weight':[13]})

linear_result = linear_model.predict(new_weight)

new_poly = poly.transform(new_weight)
poly_result = poly_model.predict(new_poly)

print("\n")
print("="*55)
print("PREDICTION")
print("="*55)
print("Package Weight : 13 kg")
print("Linear Regression Cost : ₹", round(linear_result[0],2))
print("Polynomial Regression Cost : ₹", round(poly_result[0],2))

# ==========================================================
# Visualization
# ==========================================================
plt.figure(figsize=(10,6))

# Scatter Plot
plt.scatter(X, y, color='blue', s=70, label='Actual Data')

# Linear Regression Line
plt.plot(X, linear_model.predict(X),
         color='red',
         linewidth=2,
         label='Linear Regression')

# Polynomial Curve
X_grid = np.linspace(min(X.values), max(X.values), 200).reshape(-1,1)
X_grid_poly = poly.transform(X_grid)

plt.plot(X_grid,
         poly_model.predict(X_grid_poly),
         color='green',
         linewidth=3,
         label='Polynomial Regression')

plt.title("Linear vs Polynomial Regression")
plt.xlabel("Package Weight (kg)")
plt.ylabel("Delivery Cost (₹)")
plt.legend()
plt.grid(True)

plt.show()
