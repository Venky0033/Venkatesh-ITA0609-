# Expectation Maximization Algorithm
# Dataset: Construction workers' productivity

# Productivity values of construction workers
data = [45, 48, 50, 52, 55, 70, 72, 75, 78, 80]

# Initial average productivity of two worker groups
mean1 = 50
mean2 = 75

for iteration in range(10):

    group1 = []
    group2 = []

    # E-Step
    for value in data:
        if abs(value - mean1) < abs(value - mean2):
            group1.append(value)
        else:
            group2.append(value)

    # M-Step
    mean1 = sum(group1) / len(group1)
    mean2 = sum(group2) / len(group2)

print("Construction Worker Group 1 Average Productivity:",
      round(mean1, 2))

print("Construction Worker Group 2 Average Productivity:",
      round(mean2, 2))
