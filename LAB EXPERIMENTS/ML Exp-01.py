# FIND-S Algorithm Implementation

import pandas as pd

# Training Dataset
data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

columns = ['Sky', 'AirTemp', 'Humidity', 'Wind',
           'Water', 'Forecast', 'EnjoySport']

df = pd.DataFrame(data, columns=columns)

print("Training Data:\n")
print(df)

# Initialize the most specific hypothesis
hypothesis = ['0'] * (len(columns) - 1)

print("\nInitial Hypothesis:")
print(hypothesis)

# FIND-S Algorithm
for index, row in df.iterrows():

    if row['EnjoySport'] == 'Yes':

        for i in range(len(hypothesis)):

            if hypothesis[i] == '0':
                hypothesis[i] = row[i]

            elif hypothesis[i] != row[i]:
                hypothesis[i] = '?'

    print("\nHypothesis after Training Example", index + 1)
    print(hypothesis)

print("\nFinal Most Specific Hypothesis:")
print(hypothesis)