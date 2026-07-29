# Artificial Neural Network using Backpropagation

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split dataset into Training and Testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create ANN Model using Backpropagation
ann = MLPClassifier(
    hidden_layer_sizes=(8, 8),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

# Train the model
ann.fit(X_train, y_train)

# Predict
y_pred = ann.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# Test with a new sample
sample = [[5.1, 3.5, 1.4, 0.2]]

sample = scaler.transform(sample)

prediction = ann.predict(sample)

print("\nNew Sample Prediction:")
print("Predicted Class:", iris.target_names[prediction][0])