from pathlib import Path

from constants import (
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    PDF_PATH,
    QDRANT_URL,
)
from dotenv import load_dotenv
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

loader = PyMuPDFLoader(str(PDF_PATH))
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(docs)

embeddings = OpenAIEmbeddings(
    model = EMBEDDING_MODEL
)

vector_store = QdrantVectorStore.from_documents(
    documents=texts,
    embedding=embeddings,
    url=QDRANT_URL,
    collection_name=COLLECTION_NAME,
    force_recreate=True,
)

print(f"Loaded {len(docs)} pages")
print(f"Created {len(texts)} chunks")

print(texts[12])
print("\n\n")
print(texts)
