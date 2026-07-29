import pandas as pd
import numpy as np

# Dataset
data = pd.DataFrame({
    'Outlook': ['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast','Sunny','Sunny','Rain'],
    'Temperature': ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild'],
    'Humidity': ['High','High','High','High','Normal','Normal','Normal','High','Normal','Normal'],
    'Wind': ['Weak','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Weak','Weak'],
    'PlayTennis': ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes']
})

# Function to calculate entropy
def entropy(target):
    values, counts = np.unique(target, return_counts=True)
    entropy = 0
    for i in range(len(values)):
        p = counts[i] / np.sum(counts)
        entropy -= p * np.log2(p)
    return entropy

# Function to calculate information gain
def info_gain(data, feature, target="PlayTennis"):
    total_entropy = entropy(data[target])
    
    values, counts = np.unique(data[feature], return_counts=True)
    
    weighted_entropy = 0
    for i in range(len(values)):
        subset = data[data[feature] == values[i]]
        weighted_entropy += (counts[i]/np.sum(counts)) * entropy(subset[target])
    
    return total_entropy - weighted_entropy

# ID3 Algorithm
def id3(data, features, target="PlayTennis"):
    
    # If all target values same → return class
    if len(np.unique(data[target])) == 1:
        return np.unique(data[target])[0]
    
    # If no features left → return majority class
    if len(features) == 0:
        return data[target].mode()[0]
    
    # Select best feature
    gains = [info_gain(data, feature, target) for feature in features]
    best_feature = features[np.argmax(gains)]
    
    tree = {best_feature: {}}
    
    for value in np.unique(data[best_feature]):
        subset = data[data[best_feature] == value]
        
        if subset.shape[0] == 0:
            tree[best_feature][value] = data[target].mode()[0]
        else:
            remaining_features = [f for f in features if f != best_feature]
            tree[best_feature][value] = id3(subset, remaining_features, target)
    
    return tree

# Build decision tree
features = list(data.columns[:-1])
tree = id3(data, features)

print("Decision Tree:")
print(tree)

# Prediction function
def predict(tree, sample):
    for key in tree.keys():
        value = sample[key]
        subtree = tree[key][value]
        
        if isinstance(subtree, dict):
            return predict(subtree, sample)
        else:
            return subtree

# Test with new sample
sample = {
    'Outlook': 'Sunny',
    'Temperature': 'Cool',
    'Humidity': 'High',
    'Wind': 'Strong'
}

result = predict(tree, sample)

print("\nNew Sample:", sample)
print("Prediction:", result)