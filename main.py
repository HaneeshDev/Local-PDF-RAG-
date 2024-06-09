from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from get_embedding_function import get_embedding_function
from langchain_community.vectorstores import Chroma


CHROMA_PATH = "chroma"
DATA_PATH = ".\\Data"

def load_document():
    document_loader = PyPDFDirectoryLoader(CHROMA_PATH)
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

chunks = split_document(documents)
# print(chunks[0])



def add_to_chroma(chunks: list[Document]):
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=get_embedding_function()
    )
    db.add_documents(new_chunks,ids=new_chunks_ids)
    db.persist

last_page_id = None
current_chunk_index = 0

for chunk in chunks:
    source = chunk.metadata.get("source")
    page = chunk.metadata.get("page")
    current_page_id = f"{source}:{page}"

    if current_page_id == last_page_id:
        current_chunk_index += 1
    else:
        current_chunk_index = 0
    

