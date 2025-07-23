import streamlit as st
import asyncio
from utils.file_parser import load_file
from utils.retrievers import get_hybrid_retriever
from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from configs.config import (
    PINECONE_API_KEY, GOOGLE_API_KEY,
    PINECONE_INDEX
)

# === Ensure ASYNCIO event loop exists (required by gRPC clients) ===
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# === CONFIGURE PINECONE + EMBEDDINGS + LLM ===
pc = Pinecone(api_key=PINECONE_API_KEY)

embedding = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GOOGLE_API_KEY
)

llm = GoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.7
)

# === SETUP RAG PIPELINE ===
def setup_rag(data_source, data_key):
    if data_key not in st.session_state:
        st.session_state[data_key] = data_source()

    if "vector_db" not in st.session_state and st.session_state[data_key]:
        st.session_state.vector_db = PineconeVectorStore.from_existing_index(
            index_name=PINECONE_INDEX,
            embedding=embedding
        )

    if "retriever_chain" not in st.session_state and st.session_state.get("vector_db"):
        st.session_state.retriever_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=get_hybrid_retriever(
                documents=st.session_state[data_key],
                pinecone_index_name=PINECONE_INDEX,
                embedding=embedding
            ),
            return_source_documents=True
        )

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

# === CHAT UI ===
def chat_interface():
    for msg_u, msg_r in st.session_state.get("chat_history", []):
        with st.chat_message("user"):
            st.write(msg_u)
        with st.chat_message("assistant"):
            st.write(msg_r)

    user_query = st.chat_input("Enter your question:")
    if user_query and st.session_state.get("retriever_chain"):
        result = st.session_state.retriever_chain.invoke({
            "query": user_query,
        })

        answer = result["result"]
        st.session_state.chat_history.append((user_query, answer))

        with st.chat_message("user"):
            st.write(user_query)
        with st.chat_message("assistant"):
            st.write(answer)

# === MAIN STREAMLIT APP ===

def main():
    st.set_page_config(page_title="Full RAG Project", page_icon="🚀", layout="wide")
    st.title("🚀 Full RAG Project")

    uploaded_file = st.sidebar.file_uploader(
        "Upload a document:", 
        type=["pdf", "docx", "pptx", "doc"], 
        accept_multiple_files=False
    )

    if uploaded_file:
        st.sidebar.success(f"Uploaded: {uploaded_file.name}")

        # Detect file change
        if "last_uploaded_file_name" not in st.session_state or st.session_state.last_uploaded_file_name != uploaded_file.name:
            # Reset session state
            st.session_state.clear()
            st.session_state.last_uploaded_file_name = uploaded_file.name

        # Setup pipeline and chat
        setup_rag(lambda: load_file(uploaded_file), "data")
        chat_interface()




if __name__ == "__main__":
    main()
