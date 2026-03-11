import pandas as pd
import os

file_path = "dataset.csv"

if not os.path.exists(file_path):
    print(f"Error: {file_path} not found!")
else:
    df = pd.read_csv(file_path)
    
    # TRICK: Remove any hidden spaces from column names
    df.columns = df.columns.str.strip()
    
    print(f"Cleaned columns: {df.columns.tolist()}")

    if 'name' in df.columns:
        # TRICK: Also handle the data itself just in case
        df['name'] = df['name'].astype(str).str.strip().str.upper()
        
        df.to_csv("processed_data.csv", index=False)
        print("Success! processed_data.csv created.")
    else:
        print("Error: 'name' column still not found. Check the file content.")