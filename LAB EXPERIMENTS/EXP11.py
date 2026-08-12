from sklearn.tree import DecisionTreeClassifier

# Age, Income, Loan Amount
X = [
    [22, 20000, 15000],
    [25, 25000, 10000],
    [30, 30000, 12000],
    [35, 40000, 15000],
    [40, 50000, 10000],
    [45, 60000, 8000],
    [50, 70000, 5000],
    [55, 80000, 4000]
]

# 0 = Poor Credit, 1 = Good Credit
y = [0, 0, 0, 1, 1, 1, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

age = 32
income = 35000
loan = 12000

result = model.predict([[age, income, loan]])

if result[0] == 1:
    print("Credit Score: Good")
else:
    print("Credit Score: Poor")
