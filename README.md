Parquet File Merger
===================

A simple Python tool for merging Parquet files into a single DataFrame and exporting it as a CSV file.

Features
--------

*   Merge multiple Parquet files in a specified folder
*   Automatically skip empty (0 byte) files
*   Show progress while reading files
*   Print the number of rows in each file and the merged DataFrame
*   Print the head of the merged DataFrame
*   Display summary statistics for the merged DataFrame
*   Export the merged DataFrame to a CSV file with an automatically generated filename based on the current date and time

Requirements
------------

*   Python 3.6 or higher
*   pandas
*   pyarrow

Installation
------------

1.  Clone the repository or download the `parquet_merger.py` file.
    
2.  Install the required packages:
    
    ```
    pip install pandas pyarrow
    ```
    

Usage
-----

1.  Open the `parquet_merger.py` file in a text editor and modify the `folder_path` variable with the actual path to the folder containing your Parquet files.
    
2.  Save and close the file.
    
3.  Run the script:
    
    ```
    python parquet_merger.py
    ```
    
4.  The script will read and merge the Parquet files, print relevant information and statistics, and export the merged DataFrame to a CSV file.
