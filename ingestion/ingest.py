from database.chroma import embed, search
from ingestion.chunker import make_chunks
from ingestion.extractors.pdf_extractor import extract_pdf_text

def ingest():
    text = extract_pdf_text(r"docs")

    chunks = make_chunks(text)

    embed(chunks)

    query = "When was CU founded"

    relevant_chunks = search(query)

    print(relevant_chunks)