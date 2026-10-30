from langchain_community.document_loaders import PyPDFDirectoryLoader

def extract_pdf_text(path):
    loader = PyPDFDirectoryLoader(path)

    documents = loader.load()

    text = ""

    for i, content in enumerate(documents):
        text += content.page_content + "\n"

    return text

print(extract_pdf_text(r"docs"))