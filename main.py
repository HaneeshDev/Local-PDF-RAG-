from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
# from langchain_communitBedrockEmbeddingsy.embeddings.bedrock import BedrockEmbeddings
from langchain_community.embeddings.ollama import OllamaEmbeddings
# from get_embedding_function import get_embedding_function
from langchain.vectorstores.chroma import Chroma

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



# If you want to use AWS BedRock embedding
# def get_embedding_function():
#     embeddings = BedrockEmbeddings(
#         credentials_profile_name="default", region_name="us-east-1"
#     )
#     return embeddings

def get_embedding_function():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings

def add_to_chroma(chunks: list[Document]):
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=get_embedding_function()
    )
    db.add_documents(new_chunks,ids=new_chunks_ids)
    db.persist