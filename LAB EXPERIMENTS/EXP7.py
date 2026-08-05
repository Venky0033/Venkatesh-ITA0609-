import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

# Create Loan Prediction Dataset
data = {
    'Gender': ['Male','Female','Male','Male','Female','Male','Female','Male','Female','Male',
               'Male','Female','Male','Female','Male','Female','Male','Male','Female','Male'],
    'Married': ['Yes','No','Yes','Yes','No','Yes','Yes','No','No','Yes',
                'Yes','No','Yes','Yes','No','Yes','No','Yes','No','Yes'],
    'Education': ['Graduate','Graduate','Graduate','Not Graduate','Graduate','Graduate','Graduate',
                  'Not Graduate','Graduate','Graduate','Graduate','Not Graduate','Graduate',
                  'Graduate','Graduate','Graduate','Not Graduate','Graduate','Graduate','Graduate'],
    'ApplicantIncome': [5000,3000,4000,2500,6000,7000,3500,2800,4500,5200,
                        6100,2900,4800,5500,3200,6800,2600,7200,4100,5300],
    'LoanAmount': [120,80,100,70,150,180,90,65,110,130,
                   140,75,115,145,85,170,60,190,105,125],
    'Credit_History': [1,0,1,1,1,1,0,0,1,1,
                       1,0,1,1,0,1,0,1,1,1],
    'Loan_Status': ['Y','N','Y','Y','Y','Y','N','N','Y','Y',
                    'Y','N','Y','Y','N','Y','N','Y','Y','Y']
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Encode categorical columns
le = LabelEncoder()

df['Gender'] = le.fit_transform(df['Gender'])
df['Married'] = le.fit_transform(df['Married'])
df['Education'] = le.fit_transform(df['Education'])
df['Loan_Status'] = le.fit_transform(df['Loan_Status'])

# Features and Target
X = df.drop('Loan_Status', axis=1)
y = df['Loan_Status']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Create Logistic Regression model
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Display results
print("Actual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(y_pred)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nAccuracy: {:.2f}%".format(accuracy_score(y_test, y_pred) * 100))
