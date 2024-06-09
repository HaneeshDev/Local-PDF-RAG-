from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document

def load_document():
    document_loader = PyPDFDirectoryLoader(".\\Data")
    return  document_loader.load()

documents = load_document()
# print(documents[0])

def split_document(documents: list[Document]):
    test_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 800,
        chunk_overlap = 80,
        length_function = len,
        is_separator_regex=False,
    )
    return test_splitter.split_documents(documents)

chuncks = split_document(documents)
print(chuncks[0])

