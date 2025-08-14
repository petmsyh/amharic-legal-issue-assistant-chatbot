from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import json

def create_vector_db():
    # Load the chunks from the JSON file
    with open("data/chunks.json", "r", encoding="utf-8") as f:
        chunks = json.load(f)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    vectorstore = FAISS.from_texts(chunks, embeddings)
    vectorstore.save_local("vector_db")
    print("✅ Vector store created and saved to vector_db")

if __name__ == "__main__":
    create_vector_db()