# ==========================================================
# Linear Regression - Soil Moisture vs Irrigation Requirement
# ==========================================================

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ----------------------------------------------------------
# Step 1: Create Dataset
# ----------------------------------------------------------
data = {
    'Soil_Moisture': [10, 15, 18, 20, 22,
                      25, 28, 30, 35, 38,
                      40, 45, 50, 55, 60,
                      65, 70, 75, 80, 85],

    'Irrigation_Liters': [95, 90, 87, 84, 80,
                          76, 72, 68, 60, 56,
                          52, 45, 38, 30, 24,
                          18, 12, 8, 4, 0]
}

df = pd.DataFrame(data)

print("=" * 50)
print("      SOIL MOISTURE DATASET")
print("=" * 50)
print(df)

# ----------------------------------------------------------
# Step 2: Select Feature and Target
# ----------------------------------------------------------
X = df[['Soil_Moisture']]
y = df['Irrigation_Liters']

# ----------------------------------------------------------
# Step 3: Split Dataset
# ----------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# ----------------------------------------------------------
# Step 4: Create Linear Regression Model
# ----------------------------------------------------------
model = LinearRegression()

# ----------------------------------------------------------
# Step 5: Train Model
# ----------------------------------------------------------
model.fit(X_train, y_train)

# ----------------------------------------------------------
# Step 6: Predict Test Data
# ----------------------------------------------------------
y_pred = model.predict(X_test)

# ----------------------------------------------------------
# Step 7: Display Results
# ----------------------------------------------------------
print("\n")
print("=" * 50)
print("LINEAR REGRESSION RESULTS")
print("=" * 50)

print("Slope (Coefficient) :", model.coef_[0])
print("Intercept           :", model.intercept_)
print("Mean Squared Error  :", mean_squared_error(y_test, y_pred))
print("R2 Score            :", r2_score(y_test, y_pred))

# ----------------------------------------------------------
# Step 8: Predict New Soil Moisture Value
# ----------------------------------------------------------
new_soil = pd.DataFrame({'Soil_Moisture': [32]})

prediction = model.predict(new_soil)

print("\nPrediction")
print("-" * 40)
print("Soil Moisture : 32 %")
print("Predicted Irrigation :", round(prediction[0], 2), "Liters")

# ----------------------------------------------------------
# Step 9: Plot Regression Line
# ----------------------------------------------------------
plt.figure(figsize=(8,5))

plt.scatter(
    X,
    y,
    color='green',
    s=80,
    label='Actual Data'
)

plt.plot(
    X,
    model.predict(X),
    color='red',
    linewidth=2,
    label='Regression Line'
)

plt.title("Linear Regression - Soil Moisture vs Irrigation")
plt.xlabel("Soil Moisture (%)")
plt.ylabel("Irrigation Requirement (Liters)")
plt.legend()
plt.grid(True)

plt.show()
