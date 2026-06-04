from PyPDF2 import PdfReader
def extract_text_from_pdf(uploaded_file):
    pdf=PdfReader(uploaded_file)
    text=""
    for page in pdf.pages:
        text+=page.extract_text()
    return text

