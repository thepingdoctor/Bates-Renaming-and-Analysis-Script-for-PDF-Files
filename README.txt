
# Bates Renaming and Analysis Script for PDF Files

This repository contains a Python script designed to ingest PDF files, analyze them, and rename them using a proper Bates numbering format. It is particularly useful for preparing documents for upload to Everlaw's Storybuilder Application.

## Features

- **Recursive PDF Analysis**: The script processes PDF files in a specified directory and its subdirectories.
- **Bates Numbering**: Each PDF is renamed using an incremented Bates number format.
- **Page Count Logging**: Logs the number of pages for each PDF to a text file and prints the result to the console.
- **CSV Output**: Original and new file names are logged to a CSV file.
- **Error Handling**: Captures and logs errors encountered during file processing.

## Prerequisites

- Python 3.x
- `PyPDF2` library

## Installation

1. Clone this repository to your local machine:

2. Navigate to the project directory:
  
3. Install the required Python package:
   ```bash
   pip install PyPDF2
   ```

## Usage

1. Place all the PDF files you want to process in a designated directory.
2. Modify the `pdf_directory` variable in the script to point to the path of your PDF files.

   ```python
   pdf_directory = "/path/to/directory"  # Replace with the actual path
   ```

   **Important**: Ensure that the `pdf_directory` variable accurately reflects the path to the directory where your PDF files are located. Failure to do so will result in the script not being able to locate and process your files.

3. **Important**: Before running the script, adjust the following variables to meet your specific requirements:
   - `uid`: This variable controls the starting point for Bates numbering. It's currently set to `981` (corresponding to "DOE0981").
   - `fileuid`: This variable is used to construct the new file name. It's currently set as `fileuid = f"DOE{uid_str}"`. If you need a different prefix, modify `"DOE"` to your desired string.

4. Run the script:
   ```bash
   python analyze_pdfs.py
   ```

5. The script will:
   - Rename each PDF file using a Bates numbering format.
   - Log the original and new file names to `renamed_files.csv`.
   - Log the Bates number and page count to `loadfile.txt`.

## Example Output

- **Console Output**:
  ```
  DOE0981, 3
  DOE0984, 2
  ...
  ```

- **CSV File (`renamed_files.csv`)**:
  ```
  Original File Name, New File Name
  document1.pdf, DOE0981.pdf
  document2.pdf, DOE0984.pdf
  ...
  ```

- **Text File (`loadfile.txt`)**:
  ```
  BeginBates, NumPages
  DOE0981, 3
  DOE0984, 2
  ...
  ```

## Notes

- The script starts the Bates numbering at `0981`. You can modify this by changing the initial `uid` variable in the script.
- The script will create or overwrite the `renamed_files.csv` and `loadfile.txt` files in the specified directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
