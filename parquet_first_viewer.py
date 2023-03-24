import pandas as pd
import os

# Replace with the path to your directory
dir_path = 'your_directory_path'

# Loop through each subdirectory
for subdir in os.listdir(dir_path):
    subdir_path = os.path.join(dir_path, subdir)
    
    # Check if the subdirectory exists and contains Parquet files
    if os.path.isdir(subdir_path) and any(file.endswith('.parquet') for file in os.listdir(subdir_path)):
        
        # Find the first Parquet file in the subdirectory
        parquet_files = [file for file in os.listdir(subdir_path) if file.endswith('.parquet')]
        sorted_parquet_files = sorted(parquet_files)
        first_parquet_file = sorted_parquet_files[0]
        parquet_file_path = os.path.join(subdir_path, first_parquet_file)
        
        # Check if the Parquet file is empty, and skip if it is
        if os.path.getsize(parquet_file_path) == 0:
            print(f"Skipped empty file '{parquet_file_path}'.")
            continue
        
        # Read the first non-empty Parquet file into a DataFrame and display the first 10 rows
        df = pd.read_parquet(parquet_file_path)
        print(f"First 10 rows of '{parquet_file_path}':")
        print(df.head(10))
