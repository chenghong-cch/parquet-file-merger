import pandas as pd
import pyarrow.parquet as pq
import os
import datetime

folder_path = 'your_folder_path'  # Replace with your actual folder path
parquet_files = [f for f in os.listdir(folder_path) if f.endswith('.parquet')]

# Sort files by name
sorted_parquet_files = sorted(parquet_files)

dfs = []
total_files = len(sorted_parquet_files)

for index, file in enumerate(sorted_parquet_files):
    file_path = os.path.join(folder_path, file)
    
    # Check file size, skip files with size 0
    if os.path.getsize(file_path) == 0:
        print(f"Skipped empty file '{file[:10]}...' at index {index}.")
        continue
    
    df = pd.read_parquet(file_path)
    dfs.append(df)

    # Print successfully read message, number of rows in the file, and progress percentage
    progress_percentage = (index + 1) / total_files * 100
    print(f"Read file '{file[:10]}...' at index {index}, {df.shape[0]} rows, progress: {progress_percentage:.2f}%.")

merged_df = pd.concat(dfs, ignore_index=True)

# Print the number of rows in the merged dataframe
print(f"Total rows in merged dataframe: {merged_df.shape[0]}")

# Print the head of the merged dataframe
print("\nHead of merged dataframe:")
print(merged_df.head())

# Optional: Print summary statistics of the merged dataframe
# print("\nSummary statistics of merged dataframe:")
# print(merged_df.describe())

# Optional: Print the number of missing values in the merged dataframe
# print("\nNumber of missing values in merged dataframe:")
# print(merged_df.isnull().sum())

# Optional: Define a suitable output filename based on current date and time
# output_filename = f"merged_dataframe_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

# Optional: Export the merged dataframe to a CSV file
# merged_df.to_csv(output_filename, index=False)
# print(f"\nMerged dataframe saved as '{output_filename}'.")
