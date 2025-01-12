import PyPDF2
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import time  # Importando o módulo time para medir o tempo

# Certifique-se de instalar as bibliotecas necessárias:
# pip install PyPDF2 pytesseract pdf2image pillow
# Além disso, instale o Tesseract OCR e configure o caminho para ele.

# Caminho para o executável do Tesseract OCR (ajuste conforme o local no seu sistema)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\kelvi\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def buscar_texto_em_pdf(caminho_pdf, texto_procurado):
    """
    Procura por um texto em um PDF, usando OCR para PDFs escaneados (baseados em imagens).

    :param caminho_pdf: Caminho para o arquivo PDF.
    :param texto_procurado: Texto a ser procurado.
    :return: Lista de páginas onde o texto foi encontrado.
    """
    paginas_com_texto = []
    tempo_inicial = time.time()  # Captura o tempo inicial

    try:
        # Tentar ler o PDF como texto normal usando PyPDF2
        with open(caminho_pdf, 'rb') as pdf_file:
            leitor_pdf = PyPDF2.PdfReader(pdf_file)
            
            for numero_pagina, pagina in enumerate(leitor_pdf.pages, start=1):
                conteudo_pagina = pagina.extract_text()
                if texto_procurado.lower() in conteudo_pagina.lower():
                    paginas_com_texto.append(numero_pagina)

        # Se nenhuma página tiver o texto, usar OCR
        if not paginas_com_texto:
            print("Tentando OCR, já que o PDF parece ser baseado em imagens...")
            imagens = convert_from_path(caminho_pdf)
            
            for numero_pagina, imagem in enumerate(imagens, start=1):
                # Converter imagem para texto com OCR
                texto_extraido = pytesseract.image_to_string(imagem)
                if texto_procurado.lower() in texto_extraido.lower():
                    paginas_com_texto.append(numero_pagina)

        # Calculando o tempo de execução
        tempo_final = time.time()
        tempo_total = tempo_final - tempo_inicial

        if paginas_com_texto:
            print(f"O texto '{texto_procurado}' foi encontrado nas páginas: {paginas_com_texto}")
        else:
            print(f"O texto '{texto_procurado}' não foi encontrado no PDF.")

        # Exibe o tempo total de execução
        print(f"Duração para encontrar o texto: {tempo_total:.2f} segundos")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_pdf}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")
    
    return paginas_com_texto

# Exemplo de uso
if __name__ == "__main__":
    caminho_pdf = input("Digite o caminho do arquivo PDF: ").strip()
    texto_procurado = input("Digite o texto que deseja buscar: ").strip()
    buscar_texto_em_pdf(caminho_pdf, texto_procurado)
