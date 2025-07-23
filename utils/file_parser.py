from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    UnstructuredPowerPointLoader,
)

import tempfile
import os

def load_file(file):
    file_suffix = os.path.splitext(file.name)[1]

    # Save uploaded file to a temporary path
    with tempfile.NamedTemporaryFile(delete=False, suffix=file_suffix) as tmp_file:
        tmp_file.write(file.read())
        tmp_file_path = tmp_file.name

    # Choose loader based on file type
    if file.name.endswith(".pdf"):
        loader = PyPDFLoader(tmp_file_path)
    elif file.name.endswith(".docx") or file.name.endswith(".doc"):
        loader = Docx2txtLoader(tmp_file_path)
    elif file.name.endswith(".pptx"):
        loader = UnstructuredPowerPointLoader(tmp_file_path)
    else:
        os.remove(tmp_file_path)
        return []

    documents = loader.load()

    # Clean up temp file
    os.remove(tmp_file_path)

    return documents
