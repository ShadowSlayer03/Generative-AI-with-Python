
from pathlib import Path

BASE_DIR = Path(__file__).parent
PDF_PATH = BASE_DIR / "bio.pdf"

QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "biology_docs"

EMBEDDING_MODEL = "text-embedding-3-large"
