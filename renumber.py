import PyPDF2
import os
import csv

def analyze_pdfs(directory):
    """Analyzes PDF documents recursively, assigns UIDs (incrementing by page count),
    counts pages, renames files, prints formatted output to console and a text file with a header,
    and logs file names to a CSV file."""

    uid = 981  # Start UID at 0981
    csv_path = os.path.join(directory, "renamed_files.csv")
    txt_path = os.path.join(directory, "loadfile.txt")

    with open(csv_path, 'w', newline='') as csvfile, open(txt_path, 'w') as txtfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Original File Name', 'New File Name'])

        # Write header to text file
        txtfile.write("BeginBates, NumPages\n")

        for root, _, files in os.walk(directory):
            for filename in files:
                if filename.endswith(".pdf"):
                    filepath = os.path.join(root, filename)

                    try:
                        with open(filepath, 'rb') as pdf_file:
                            pdf_reader = PyPDF2.PdfReader(pdf_file)
                            num_pages = len(pdf_reader.pages)

                            # Format UID with leading zeros
                            uid_str = f"{uid:04d}"
                            fileuid = f"DOE{uid_str}"

                            # Print formatted output to console and text file
                            print(fileuid + ", " + str(num_pages))
                            txtfile.write(fileuid + ", " + str(num_pages) + "\n")

                            # Rename the PDF file
                            new_filepath = os.path.join(root, fileuid + ".pdf")
                            os.rename(filepath, new_filepath)

                            # Write file names to CSV
                            csv_writer.writerow([filename, fileuid + ".pdf"])

                            # Increment UID
                            uid += num_pages

                    except Exception as e:
                        print(f"Error processing {filepath}: {e}")

# Specify the directory containing the PDFs
pdf_directory = "/path/to/directory"  # Replace with the actual path

analyze_pdfs(pdf_directory)