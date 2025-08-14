import re
from langchain.text_splitter import CharacterTextSplitter
import json

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with single space
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    return text

def split_text(text, chunk_size=1000, chunk_overlap=200):
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_text(text)
    return texts

# Load extracted text from file
with open("data/extracted_text.txt", "r", encoding="utf-8") as f:
    pdf_text = f.read()

cleaned_text = clean_text(pdf_text)
chunks = split_text(cleaned_text)

# Save chunks to a JSON file
with open("data/chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=4)

print(f"✅ Saved {len(chunks)} text chunks to data/chunks.json")