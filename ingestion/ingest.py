from extractors.pdf_extractor import extract_pdf_text
from chunker import make_chunks
from embedder import embed, search

text = extract_pdf_text(r"docs")

chunks = make_chunks(text)

embed(chunks)

query = "When was CU founded"

relevant_chunks = search(query)

