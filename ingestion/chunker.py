from langchain_text_splitters import RecursiveCharacterTextSplitter

def make_chunks(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=0,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = splitter.split_text(text)

    return chunks