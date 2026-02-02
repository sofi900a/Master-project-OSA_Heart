import os
import pandas as pd

base_dir = "/Users/sofiehultengren/Desktop/Kandidat speciale /Slicer analysis /Pig_1"

tsv_data = {}  # key = file path, value = DataFrame

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.lower().endswith(".tsv"):
            file_path = os.path.join(root, file)
            try:
                df = pd.read_csv(file_path, sep="\t")
                tsv_data[file_path] = df
                print(f"Loaded: {file_path}")
            except Exception as e:
                print(f"Failed to load {file_path}: {e}")

print(f"\nTotal TSV files loaded: {len(tsv_data)}")
# Example: Accessing a specific DataFrame
# for path, dataframe in tsv_data.items():
#     print(f"Data from {path}:")
#     print(dataframe.head())   


import os
import pandas as pd

base_dir = "/Users/sofiehultengren/Desktop/Kandidat speciale /Slicer analysis /Pig_1"

dfs = []

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.lower().endswith(".tsv"):
            file_path = os.path.join(root, file)
            df = pd.read_csv(file_path, sep="\t")
            df["source_file"] = file_path  # keep provenance
            dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)

print(combined_df.head())
print("Total rows:", len(combined_df))
