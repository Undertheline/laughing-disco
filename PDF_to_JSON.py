import pypdf
from pypdf import PdfReader

reader = PdfReader("exemplo.pdf")
page = reader.pages[1]

print(page.extract_text(extraction_mode="plain"))