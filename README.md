
# 🚀 Full RAG Project

This is a **Retrieval-Augmented Generation (RAG)** chatbot built with [LangChain](https://www.langchain.com/), [Google Generative AI (Gemini)](https://ai.google.dev/), [Pinecone](https://www.pinecone.io/), and [Streamlit](https://streamlit.io/). It allows you to upload a document (PDF, DOCX, PPTX), preview it, and ask questions based on its content.

---

## 🗂️ Project Structure

```
RAG PROJECT/
├── configs/
│   └── config.py            # Environment variable bindings (API keys, index names)
├── utils/
│   ├── file_parser.py       # File loading logic (PDF, DOCX, PPTX)
│   └── retrievers.py        # Hybrid retriever using vector + keyword search
├── main.py                  # Main Streamlit app
├── .env                     # Local secrets (not committed)
├── .env.example             # Example environment template
├── requirements.txt         # Project dependencies
└── README.md                # Project overview
```

---

## ✅ Features

- 💾 Upload a single document (PDF, DOCX, PPTX)
- 🔍 Hybrid Retrieval: combines semantic + keyword retrieval
- 🧠 LLM-Powered QA using **Gemini 2.5 Flash**
- 💬 Persistent chat history using `st.session_state`
- 📄 Live preview for PDF and PPTX files
- 🌐 Pinecone vector store integration

---

## 🛠️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/Omar9965/RAG-project.git
cd rag-project
```

### 2. Create and activate a virtual environment
```bash
python -m venv rag-env
source rag-env/bin/activate  # On Windows: rag-env\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file based on `.env.example`:

```
GOOGLE_API_KEY=your_google_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX=your_index_name
```

---

## 🚀 Running the App

```bash
streamlit run main.py
```

---

## 📌 Notes

- **Only one file** is supported at a time. Uploading a new file resets the previous one.
- Poppler must be installed locally for PDF previewing (especially on Windows).
  - You can install it via: [https://blog.alivate.com.au/poppler-windows/](https://blog.alivate.com.au/poppler-windows/)

---

## 📚 Tech Stack

- [LangChain](https://python.langchain.com/)
- [Google Generative AI](https://ai.google.dev/)
- [Pinecone Vector DB](https://www.pinecone.io/)
- [Streamlit](https://streamlit.io/)

---

## 📃 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Omar Mohamed**  
Feel free to connect or contribute!
# RAG-project
