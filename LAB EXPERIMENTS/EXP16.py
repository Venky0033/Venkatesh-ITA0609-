# EXPERIMENT 16
# Compare Different Classification Algorithms

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

from sklearn.metrics import accuracy_score

# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = pd.read_csv(url)

# Select features
X = data[['Pclass', 'Sex', 'Age', 'Fare']].copy()
y = data['Survived']

# Convert Sex into numbers
X['Sex'] = LabelEncoder().fit_transform(X['Sex'])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "SVM": SVC()
}

# Train and compare
for name, model in models.items():

    # Fill missing values
    model_pipeline = make_pipeline(
        SimpleImputer(strategy='mean'),
        model
    )

    model_pipeline.fit(X_train, y_train)

    prediction = model_pipeline.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)

    print(name, "Accuracy =", round(accuracy * 100, 2), "%")
