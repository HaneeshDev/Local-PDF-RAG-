# from langchain_communitBedrockEmbeddingsy.embeddings.bedrock import BedrockEmbeddings
from langchain_community.embeddings.ollama import OllamaEmbeddings

# If you want to use AWS BedRock embedding
# def get_embedding_function():
#     embeddings = BedrockEmbeddings(
#         credentials_profile_name="default", region_name="us-east-1"
#     )
#     return embeddings

def get_embedding_function():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings