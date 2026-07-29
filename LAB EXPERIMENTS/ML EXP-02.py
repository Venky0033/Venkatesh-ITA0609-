import pandas as pd

# Load Dataset
data = pd.read_csv("training_data.csv")

print("Training Dataset:\n")
print(data)

# Separate Features and Target
concepts = data.iloc[:, :-1].values
target = data.iloc[:, -1].values

# Candidate Elimination Algorithm
def candidate_elimination(concepts, target):

    specific_h = concepts[0].copy()

    general_h = [["?" for _ in range(len(specific_h))]
                 for _ in range(len(specific_h))]

    print("\nInitial Specific Hypothesis:")
    print(specific_h)

    print("\nInitial General Hypothesis:")
    print(general_h)

    for i, h in enumerate(concepts):

        if target[i] == "Yes":

            for x in range(len(specific_h)):

                if h[x] != specific_h[x]:
                    specific_h[x] = "?"
                    general_h[x][x] = "?"

        if target[i] == "No":

            for x in range(len(specific_h)):

                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = "?"

        print("\nAfter Example", i + 1)

        print("Specific Hypothesis:")
        print(specific_h)

        print("General Hypothesis:")
        print(general_h)

    # Remove redundant hypotheses
    general_h = [g for g in general_h if g != ["?"] * len(specific_h)]

    return specific_h, general_h


s_final, g_final = candidate_elimination(concepts, target)

print("\nFinal Specific Hypothesis:")
print(s_final)

print("\nFinal General Hypothesis:")
for g in g_final:
    print(g)