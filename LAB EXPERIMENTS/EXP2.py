# Candidate Elimination Algorithm

data = [
    ["Red", "Small", "Round", "Yes"],
    ["Red", "Large", "Round", "Yes"],
    ["Blue", "Small", "Round", "No"],
    ["Red", "Small", "Square", "No"]
]

S = data[0][:-1]
G = ["?"] * len(S)

for sample in data:
    if sample[-1] == "Yes":
        for i in range(len(S)):
            if S[i] != sample[i]:
                S[i] = "?"
    else:
        for i in range(len(S)):
            if S[i] != sample[i]:
                G[i] = S[i]

print("Specific Hypothesis:")
print(S)

print("General Hypothesis:")
print(G)