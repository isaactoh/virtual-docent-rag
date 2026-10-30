'''
Main ingestion coordinator

1. load file and use appropriate extractor

2. chunk text

3. embed text with chroma
'''
from extractors.pdf_extractor import extract_pdf_text
from chunker import make_chunks

text = extract_pdf_text(r"docs")

for i, chunk in enumerate(make_chunks(text)):
    print(i, chunk)
    print('\n')