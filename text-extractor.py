import PyPDF2

def extract_content(pdf_path, keyword):
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    num_pages = len(pdf_reader.pages)

    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        page_text = page.extract_text()

        if keyword.lower() in page_text.lower():
            print(f"Page {page_num + 1}:")
            print(page_text)
            print("=" * 50)

# Replace 'your_pdf_file.pdf' with your PDF file's path and 'Financial Statements' with your keyword
pdf_path = '/Users/kumarrohit/Desktop/NLP-Project/Annual-Report-Summarizer/PDFs/TechMahindra.pdf'
keyword = 'Independent Auditors'
extract_content(pdf_path, keyword)
