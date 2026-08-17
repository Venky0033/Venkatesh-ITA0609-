# EXPERIMENT 19
# Naive Bayes Classification for Bank Loan Prediction

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Bank loan dataset

data = {
    'Age': [25, 30, 35, 40, 45, 28, 50, 32, 55, 38,
            27, 42, 48, 31, 36, 52, 29, 44, 39, 46],

    'Income': [25, 35, 50, 60, 80, 30, 90, 45, 100, 55,
               28, 70, 85, 40, 52, 95, 32, 75, 58, 82],

    'CreditScore': [580, 620, 700, 750, 800, 590, 820, 680, 850, 720,
                    600, 780, 810, 650, 710, 830, 610, 790, 730, 805],

    'LoanAmount': [20, 25, 30, 35, 40, 20, 45, 30, 50, 35,
                   22, 40, 45, 28, 32, 48, 24, 42, 34, 43],

    'Approved': [0, 0, 1, 1, 1, 0, 1, 1, 1, 1,
                 0, 1, 1, 0, 1, 1, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

# Input features
X = df[['Age', 'Income', 'CreditScore', 'LoanAmount']]

# Output
y = df['Approved']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Naive Bayes model
model = GaussianNB()

# Train
model.fit(X_train, y_train)

# Prediction
prediction = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, prediction)

print("Actual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(prediction)

print("\nAccuracy:", round(accuracy * 100, 2), "%")

# New customer
new_customer = [[35, 50, 700, 30]]

result = model.predict(new_customer)

if result[0] == 1:
    print("Loan Approved")
else:
    print("Loan Not Approved")
