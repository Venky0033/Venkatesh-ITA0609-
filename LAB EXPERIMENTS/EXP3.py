# Simple ID3 Decision Tree

data = [
    ["Hot", "High", "No"],
    ["Hot", "Normal", "Yes"],
    ["Cold", "High", "No"],
    ["Cold", "Normal", "Yes"]
]

def predict(temp, humidity):
    if humidity == "Normal":
        return "Yes"
    else:
        return "No"

print("Prediction:", predict("Hot", "Normal"))