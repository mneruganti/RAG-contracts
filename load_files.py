import os
from pypdf import PdfReader

# declare the file_path
DATA_PATH = 'contracts/'

# list to store parsed docs
documents = []

# function to load documents that are .txt
def load_txt(path, filename):
    
    # guarntees that file will be closed after opening (using with keyword)
    # open() uses path, read mode, and encoding as parameters
    
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return {"text: ", text, "source: ", filename}

# function to load documents that are .pdf
def load_pdf(path, filename):
    
    # Init PdfReader object
    reader = PdfReader(path)
    text = ""
    
    # iterate through each page in the PDF
    for page in reader.pages:
        
        # append text from each page to the string of metadata with a new line character
        text += page.extract_text() + "\n"
    return {"text: ", text, "source: ", filename}

for filename in os.listdir(DATA_PATH):
    path = os.path.join(DATA_PATH, filename)
    
    if filename.endswith(".txt"):
        documents.append(load_txt(path, filename))
    elif filename.endswith(".pdf"):
        documents.append(load_pdf(path, filename))
    else:
        print("ERROR: Not PDF or TXT")

print(f"Loaded {len(documents)} documents")