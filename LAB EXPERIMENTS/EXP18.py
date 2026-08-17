import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Diabetes dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"

columns = [
    'Pregnancies',
    'Glucose',
    'BloodPressure',
    'SkinThickness',
    'Insulin',
    'BMI',
    'DiabetesPedigree',
    'Age',
    'Outcome'
]

data = pd.read_csv(url, names=columns)

# Input and output
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Scale the data
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Perceptron
model = Perceptron(max_iter=1000, random_state=42)

# Train
model.fit(X_train, y_train)

# Prediction
prediction = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, prediction)

print("Accuracy:", round(accuracy * 100, 2), "%")

# New patient
new_patient = [[2, 120, 70, 20, 80, 30, 0.5, 35]]

new_patient = scaler.transform(new_patient)

result = model.predict(new_patient)

if result[0] == 1:
    print("Prediction: Diabetes")
else:
    print("Prediction: No Diabetes")
