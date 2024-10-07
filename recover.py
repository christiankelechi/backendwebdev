import os
import shutil
from datetime import datetime
from PyPDF2 import PdfReader

# Path to the directory containing the recovered files from PhotoRec
recovered_files_directory = "C:/Users/HP PC/Downloads/testdisk-7.2.win64/testdisk-7.2/recup_dir.10"
# Path to the directory where the organized files will be moved
organized_files_directory = "C:/Users/HP PC/Downloads/testdisk-7.2.win64/testdisk-7.2/organized"

def extract_pdf_title(file_path):
    """Extract the title from the first page of a PDF."""
    try:
        with open(file_path, "rb") as f:
            reader = PdfReader(f)
            # Get the first page's text
            first_page = reader.pages[0]
            text = first_page.extract_text()
            # Assuming the title is the first line of the text
            if text:
                title = text.split('\n')[0]  # Get the first line as title
                title = title.strip().replace(' ', '_')  # Format title by replacing spaces with underscores
                return title[:50]  # Limit title length to 50 characters
    except Exception as e:
        print(f"Error reading PDF {file_path}: {e}")
    return None

def organize_and_rename_pdfs_by_date(recovered_dir, target_dir, use_modification_date=False):
    # Ensure the target directory exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Traverse through the recovered files directory
    for root, dirs, files in os.walk(recovered_dir):
        for file in files:
            # Only process PDF files
            if file.lower().endswith(".pdf"):
                file_path = os.path.join(root, file)
                
                # Get file creation or modification time
                if use_modification_date:
                    file_time = os.path.getmtime(file_path)  # Modification date
                else:
                    file_time = os.path.getctime(file_path)  # Creation date
                
                # Convert timestamp to a human-readable format (Year/Month)
                file_date = datetime.fromtimestamp(file_time)
                year = file_date.strftime('%Y')
                month = file_date.strftime('%m')

                # Create new directory based on the file date
                target_subdir = os.path.join(target_dir, year, month)
                os.makedirs(target_subdir, exist_ok=True)
                
                # Extract the title from the first page of the PDF
                title = extract_pdf_title(file_path)
                if title:
                    new_filename = f"{title}.pdf"
                else:
                    new_filename = file  # Fallback to the original name if title extraction fails

                # Move and rename the file to the new directory
                new_file_path = os.path.join(target_subdir, new_filename)
                shutil.move(file_path, new_file_path)
                print(f"Moved and renamed {file} to {new_file_path}")

if __name__ == "__main__":
    organize_and_rename_pdfs_by_date(recovered_files_directory, organized_files_directory, use_modification_date=False)
