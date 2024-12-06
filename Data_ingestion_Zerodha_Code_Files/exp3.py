import json
import os
import pandas as pd

# Directory where your JSON files are stored
json_folder =  r"c:\Users\dell\Desktop\Merge INFOSYS"


# List to store candle data from all JSON files
merged_data = []

# Loop through each file in the folder
for file_name in os.listdir(json_folder):
    if file_name.endswith(".json"):  # Process only JSON files
        file_path = os.path.join(json_folder, file_name)
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            # Extract "candles" data only
            candles = data.get("data", {}).get("candles", [])
            merged_data.extend(candles)  # Add candle data to the list

# Convert merged data to a DataFrame with specified columns
df = pd.DataFrame(merged_data, columns=["timestamp", "open", "high", "low", "close", "volume"])

# Convert 'timestamp' column to datetime for sorting
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Sort the DataFrame by 'timestamp' in ascending order
df = df.sort_values(by='timestamp')

# Remove timezone information and format the timestamp
df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Reset index after sorting (optional)
df = df.reset_index(drop=True)

# Output to CSV
output_csv = "merged_data_sorted(INFY).csv"
df.to_csv(output_csv, index=False)

print(f"Merged and sorted data has been saved to {output_csv}")
