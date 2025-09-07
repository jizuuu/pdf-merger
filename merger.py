from PyPDF2 import PdfMerger
import os

output_file = "file-combined.pdf"

merger = PdfMerger()

pdf_files = [f for f in os.listdir(os.curdir) if f.endswith(".pdf")]

if not pdf_files:
  print("No PDF files found!")
else:
    for file in sorted(pdf_files):
        if file != output_file:
            merger.append(file)
    merger.write(output_file)
    merger.close()
    print(f"Merge Complete! Output: {output_file}")