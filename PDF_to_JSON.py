from pdfminer.high_level import extract_pages  # Importa a função para extrair páginas do PDF
from pdfminer.layout import LTTextContainer, LTChar  # Importa classes para identificar blocos de texto e caracteres
import numpy as np  # Importa o numpy (embora não esteja sendo usado no código)

def extract_bold_text(pdf_path):
    bold_texts = []  # Inicializa uma lista para armazenar os textos em negrito encontrados

    # Itera sobre o layout de cada página do arquivo PDF
    for page_layout in extract_pages(pdf_path):
        # Itera sobre cada elemento da página (blocos de texto, imagens, etc)
        for element in page_layout:
            # Verifica se o elemento é um contêiner de texto (LTTextContainer)
            if isinstance(element, LTTextContainer):
                # Itera sobre cada linha de texto dentro do contêiner
                for text_line in element:
                    line_text = ""  # Inicializa string para armazenar o texto em negrito da linha
                    # Itera sobre cada caractere na linha de texto
                    for character in text_line:
                        # Verifica se o objeto é um caractere (LTChar)
                        if isinstance(character, LTChar):
                            fontname = character.fontname.lower()  # Obtém o nome da fonte em letras minúsculas
                            # Verifica se o nome da fonte contém "bold" ou "black" (indicação de negrito)
                            if "bold" in fontname or "black" in fontname:
                                line_text += character.get_text()  # Adiciona o caractere ao texto da linha
                    # Se a linha possui texto em negrito (após remover espaços)
                    if line_text.strip():
                        bold_texts.append(line_text.strip())  # Adiciona a linha à lista de textos em negrito

    return bold_texts  # Retorna a lista completa de textos em negrito encontrados no PDF

# Uso da função
bold_text = extract_bold_text("exemplo.pdf")  # Extrai textos em negrito do arquivo "exemplo.pdf"

# Para cada linha de texto em negrito extraída
for line in bold_text:
  with open("texto.txt", "w") as f:
    for line in bold_text:
        f.write("*" + line + "*" + "\n")
