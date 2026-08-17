# EXPERIMENT 17
# MOBILE PRICE PREDICTION USING DECISION TREE

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Create mobile dataset
data = {
    "RAM": [2, 3, 4, 6, 8, 12, 4, 6, 8, 12],
    "Battery": [3000, 3200, 4000, 4500, 5000, 6000, 3500, 4500, 5000, 5500],
    "Camera": [8, 12, 16, 32, 48, 108, 16, 32, 64, 108],
    "Storage": [32, 64, 64, 128, 128, 256, 64, 128, 256, 256],
    "Price": [0, 0, 1, 1, 2, 3, 1, 2, 2, 3]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

print("MOBILE DATASET")
print(df)

# Select input features
X = df[["RAM", "Battery", "Camera", "Storage"]]

# Select output
y = df["Price"]

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Create Decision Tree model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predict test data
prediction = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, prediction)

print("\nACTUAL VALUES:")
print(y_test.values)

print("\nPREDICTED VALUES:")
print(prediction)

print("\nACCURACY:", accuracy * 100, "%")

# Predict price of a new mobile
new_mobile = pd.DataFrame(
    [[8, 5000, 64, 256]],
    columns=["RAM", "Battery", "Camera", "Storage"]
)

result = model.predict(new_mobile)

print("\nNEW MOBILE DETAILS:")
print(new_mobile)

print("\nNEW MOBILE PREDICTION:", result[0])

# Display price category
if result[0] == 0:
    print("PRICE RANGE: LOW")
elif result[0] == 1:
    print("PRICE RANGE: MEDIUM")
elif result[0] == 2:
    print("PRICE RANGE: HIGH")
else:
    print("PRICE RANGE: VERY HIGH")
