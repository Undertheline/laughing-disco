from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar

npode = ("2. ASSUNTOS ADMINISTRATIVOS 1. JUSTIÇA 2. DISCIPLINA 4ª Parte JUSTIÇA E DISCIPLINA DIEGO DA SILVA AGOSTINI - Ten Cel")

def extract_text_with_bold(pdf_path):
    results = []

    for page_layout in extract_pages(pdf_path):
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    full_line = ""
                    bold_parts = ""
                    for character in text_line:
                        if isinstance(character, LTChar):
                            text = character.get_text()
                            full_line += text
                            fontname = character.fontname.lower()
                            if "bold" in fontname or "black" in fontname:
                                bold_parts += text
                    if full_line.strip():
                        results.append({
                            "full_line": full_line.strip(),
                            "bold_parts": bold_parts.strip()
                        })
    return results

# Uso
lines = extract_text_with_bold("exemplo.pdf")

for item in lines:
    if item["full_line"] not in npode:
        print("Linha completa:", item["full_line"])
        print("Partes em negrito:", item["bold_parts"])
        print("---")
