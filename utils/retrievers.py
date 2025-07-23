from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever
from langchain.embeddings.base import Embeddings

def get_hybrid_retriever(documents, pinecone_index_name: str, embedding: Embeddings):
    """
    Returns an EnsembleRetriever that combines BM25 and Pinecone vector retrieval.

    Args:
        documents (List[Document]): Parsed and chunked documents.
        pinecone_index_name (str): Name of the Pinecone index.
        embedding (Embeddings): Embedding model instance.

    Returns:
        EnsembleRetriever
    """
    # BM25 retriever (local, lexical)
    bm25 = BM25Retriever.from_documents(documents)

    # Pinecone retriever (semantic vector)
    pinecone_retriever = PineconeVectorStore.from_existing_index(
        index_name=pinecone_index_name,
        embedding=embedding
    ).as_retriever()

    # Combine both with equal weights (tweak if needed)
    hybrid_retriever = EnsembleRetriever(
        retrievers=[bm25, pinecone_retriever],
        weights=[0.5, 0.5]
    )

    return hybrid_retriever
