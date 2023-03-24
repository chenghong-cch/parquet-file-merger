Parquet File Merger
===================

A Python tool for merging Parquet files into a single DataFrame and exporting it as a CSV file.

Features
--------

*   Merge multiple Parquet files in a specified folder
*   Automatically skip empty (0 byte) files
*   Show progress while reading files
*   Print the number of rows in each file and the merged DataFrame
*   Print the head of the merged DataFrame
*   Optional: Display summary statistics for the merged DataFrame
*   Optional: Print the number of missing values in the merged DataFrame
*   Optional: Define a suitable output filename based on current date and time
*   Optional: Export the merged DataFrame to a CSV file with an automatically generated filename based on the current date and time
*   NEW: Parquet First File Viewer - Read the first non-empty Parquet file in each subdirectory of a given directory and display the first 10 rows of the resulting DataFrame

Requirements
------------

*   Python 3.6 or higher
*   pandas
*   pyarrow

Installation
------------

1.  Clone the repository or download the `parquet_merger.py` and `parquet_first_viewer.py` files.
    
2.  Install the required packages:
    
    ```
    pip install pandas pyarrow
    ```
    

Usage
-----

1.  Open the `parquet_merger.py` or `parquet_first_viewer.py` file in a text editor and modify the `folder_path` variable with the actual path to the folder containing your Parquet files.
    
2.  Save and close the file.
    
3.  Run the script:
    
    ```
    python parquet_merger.py
    ```
    
    or
    
    ```
    python parquet_first_viewer.py
    ```
    
4.  For `parquet_merger.py`, the script will read and merge the Parquet files, print relevant information and statistics, and optionally export the merged DataFrame to a CSV file with an automatically generated filename based on the current date and time. Optional features such as displaying summary statistics and printing the number of missing values can be enabled by answering prompts in the console.
    
5.  For `parquet_first_viewer.py`, the script will read the first non-empty Parquet file in each subdirectory of the given directory and display the first 10 rows of the resulting DataFrame.
