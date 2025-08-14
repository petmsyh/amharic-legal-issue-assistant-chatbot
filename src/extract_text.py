import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

# Save extracted text to a file
if __name__ == "__main__":
    pdf_text = extract_text_from_pdf("data/amh-constitution.pdf")
    with open("data/extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(pdf_text)
    print("✅ Text saved to data/extracted_text.txt")