from langchain_community.document_loaders import PyPDFDirectoryLoader

# TODO: move loader to document_loader
def extract_pdf_text(path):
    loader = PyPDFDirectoryLoader(path)

    documents = loader.load()

    text = ""

    for i, content in enumerate(documents):
        text += content.page_content + "\n"

    return text