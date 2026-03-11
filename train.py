# train.py
import pandas as pd
import json
import random

# Load the PROCESSED data (not the raw one!)
df = pd.read_csv("processed_data.csv")

# Count how many rows we have
num_rows = len(df)

# Simulate a "Model Accuracy" score based on data size
# (In a real project, this is where your Scikit-Learn code goes)
accuracy = 0.85 + (num_rows * 0.01) 

# Save the metric to a JSON file
metrics = {"accuracy": round(accuracy, 4), "rows": num_rows}

with open("metrics.json", "w") as f:
    json.dump(metrics, f)

print(f"Training complete. Accuracy: {accuracy}")