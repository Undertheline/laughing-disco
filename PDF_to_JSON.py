from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar

def extract_bold_text(pdf_path):
    bold_texts = []

    for page_layout in extract_pages(pdf_path):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    line_text = ""
                    for character in text_line:
                        if isinstance(character, LTChar):
                            fontname = character.fontname.lower()
                            if "bold" in fontname or "black" in fontname:
                                line_text += character.get_text()
                    if line_text.strip():  # Se tiver conteúdo
                        bold_texts.append(line_text.strip())
    return bold_texts

# Uso
bold_text = extract_bold_text("exemplo.pdf")
for line in bold_text:
    print(line)
