import PyPDF2
import pytesseract
from tkinter import *
from tkinter import filedialog, messagebox
from pdf2image import convert_from_path
from PIL import Image
import time  

def buscar_texto_em_pdf(caminho_pdf, texto_procurado):
    """
    Procura por um texto em um PDF, usando OCR para PDFs baseados em imagens.

    :param caminho_pdf: Caminho para o arquivo PDF.
    :param texto_procurado: Texto a ser procurado.
    :return: Lista de páginas onde o texto foi encontrado.
    """
    paginas_com_texto = []
    tempo_inicial = time.time()

    try:
        with open(caminho_pdf, 'rb') as pdf_file:
            leitor_pdf = PyPDF2.PdfReader(pdf_file)
            
            for numero_pagina, pagina in enumerate(leitor_pdf.pages, start=1):
                conteudo_pagina = pagina.extract_text()
                if texto_procurado.lower() in conteudo_pagina.lower():
                    paginas_com_texto.append(numero_pagina)

        if not paginas_com_texto:
            imagens = convert_from_path(caminho_pdf)
            
            for numero_pagina, imagem in enumerate(imagens, start=1):
                
                texto_extraido = pytesseract.image_to_string(imagem)
                if texto_procurado.lower() in texto_extraido.lower():
                    paginas_com_texto.append(numero_pagina)

        tempo_final = time.time()
        tempo_total = tempo_final - tempo_inicial

        if paginas_com_texto:
            resultado = f"O texto '{texto_procurado}' foi encontrado nas páginas: {paginas_com_texto}"
        else:
            resultado = f"O texto '{texto_procurado}' não foi encontrado no PDF."

        return f"{resultado}\nDuração para encontrar o texto: {tempo_total:.2f} segundos"

    except FileNotFoundError:
        return f"Erro: O arquivo '{caminho_pdf}' não foi encontrado."
    except Exception as e:
        return f"Erro ao processar o PDF: {e}"

def selecionar_arquivo():
    """
    Abre uma janela para o usuário selecionar um arquivo PDF.
    """
    caminho_pdf = filedialog.askopenfilename(
        title="Selecione o arquivo PDF",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )
    entrada_caminho.delete(0, END)
    entrada_caminho.insert(0, caminho_pdf)

def executar_busca():
    """
    Executa a busca pelo texto no PDF selecionado.
    """
    caminho_pdf = entrada_caminho.get().strip()
    texto_procurado = entrada_texto.get().strip()

    if not caminho_pdf or not texto_procurado:
        messagebox.showwarning("Atenção", "Por favor, selecione um arquivo e insira o texto a ser procurado.")
        return

    resultado = buscar_texto_em_pdf(caminho_pdf, texto_procurado)
    messagebox.showinfo("Resultado da Busca", resultado)

janela = Tk()
janela.title("SearchInPDF")
janela.geometry("600x300")

Label(janela, text="Caminho do PDF:").grid(row=0, column=0, padx=10, pady=10, sticky=W)
entrada_caminho = Entry(janela, width=50)
entrada_caminho.grid(row=0, column=1, padx=10, pady=10)

botao_selecionar = Button(janela, text="Procurar", command=selecionar_arquivo)
botao_selecionar.grid(row=0, column=2, padx=10, pady=10)

Label(janela, text="Texto a buscar:").grid(row=1, column=0, padx=10, pady=10, sticky=W)
entrada_texto = Entry(janela, width=50)
entrada_texto.grid(row=1, column=1, padx=10, pady=10)

botao_buscar = Button(janela, text="Buscar Texto", command=executar_busca)
botao_buscar.grid(row=2, column=1, padx=10, pady=20)

janela.mainloop()
