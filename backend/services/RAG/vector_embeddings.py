import json
import os
import numpy as np
import google.generativeai as genai
from sentence_transformers import SentenceTransformer, util
import faiss

from file_services import GetChunks, extract_text

storage_dir = "./vector_storage"

class RAGVectorStore:
    
    def __init__(self, user_id: int, embedding_dim: int = 384, model_path: str = "ibm-granite/granite-embedding-30m-english", storage_dir: str = storage_dir):
        self.model = SentenceTransformer(model_path)
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.metadata = []
        # Paths for FAISS index and metadata
        self.index_file = os.path.join(storage_dir, f"{user_id}_index.faiss")
        self.meta_file = os.path.join(storage_dir, f"{user_id}_metadata.json")

        # Load index if exists, otherwise create new
        if os.path.exists(self.index_file):
            self.index = faiss.read_index(self.index_file)
            with open(self.meta_file, "r", encoding="utf-8") as f:
                self.metadata = json.load(f)

    def get_embeddings(self, chunks: list):
        """Convert a list of text chunks into embeddings"""
        vectors = [self.model.encode(chunk) for chunk in chunks]
        return vectors

    def add_chunks(self, chunks: list):
        """
        Convert chunks to embeddings and store both in FAISS + metadata
        """
        vectors = self.get_embeddings(chunks)
        np_vectors = np.array(vectors).astype("float32")
        self.index.add(np_vectors)
        self.metadata.extend(chunks)
        print(f"Stored {len(chunks)} chunks. Total vectors: {self.index.ntotal}")
         # --- Save to disk ---
        faiss.write_index(self.index, self.index_file)

    def search(self, query: str, top_k=5):
        """Search for nearest neighbors for a query string"""
        query_vector = self.model.encode(query)
        query_vector = np.array([query_vector]).astype("float32")
        distances, indices = self.index.search(query_vector, top_k)
        results = [self.metadata[i] for i in indices[0] if i < len(self.metadata)]
        return results

user1 = RAGVectorStore(user_id=1)
x=extract_text(r"C:\Users\surendhar\Downloads\Website Testing.pptx")
chunks = GetChunks(x)
print(len(chunks))
user1.add_chunks(chunks)