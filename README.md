# 📑 PDF Merger  

![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)  
![License](https://img.shields.io/badge/license-MIT-green.svg)  
![PyPI - PyPDF2](https://img.shields.io/badge/dependency-PyPDF2-orange.svg)  

A simple Python automation script to merge multiple PDF files into a single file.

## 🚀 Features
- Scans the current folder for `.pdf` files  
- Merges them into a single output file (`file-combined.pdf` by default)  
- Skips the output file on subsequent runs  
- Prints a message if no PDF files are found  

## 🛠 Requirements
- Python 3.7+  
- [PyPDF2](https://pypi.org/project/pypdf2/)  

## 📦 Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/pdf-merger.git
    ```

2. Navigate into the project folder:
    ```bash
    cd pdf-merger
    ```

3. Install the required dependency:
    ```bash
    pip install PyPDF2
    ```

4. Run the program:
    ```bash
    python merger.py
    ```

## ✨ Custom Output File
By default, the merged file will be saved as: file-combined.pdf

If you want a different name, edit the `output_file` variable inside **merger.py**:
```python
output_file = "my_merged_file.pdf"