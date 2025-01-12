Guia para Instalação das Dependências do Sistema

Para que o sistema funcione corretamente, é necessário instalar algumas dependências. Siga os passos abaixo:

1. Instalar o Tesseract OCR

O Tesseract é um software OCR utilizado pelo sistema para extrair texto de imagens.

Passos:

Acesse o link de download do instalador:
Download Tesseract OCR

Baixe e execute o arquivo tesseract-ocr-w64-setup-5.5.0.20241111.exe.

Durante a instalação:

Certifique-se de selecionar a opção para adicionar o Tesseract ao PATH do sistema, caso essa opção esteja disponível.

Após a instalação, verifique se o executável do Tesseract está funcionando:

Abra o Prompt de Comando (CMD).

Digite o comando tesseract -v.

Você deve ver a versão do Tesseract instalada.

2. Instalar o Poppler

O Poppler é necessário para converter PDFs em imagens para uso posterior no OCR.

Passos:

Baixe o Poppler apropriado para o seu sistema operacional (Windows).

O Poppler pode ser encontrado em repositórios confiáveis ou sites oficiais.

Extraia os arquivos do Poppler para um diretório, como C:\Program Files\Poppler.

Adicione o diretório do executável do Poppler ao PATH do sistema:

Abra o Explorador de Arquivos e copie o caminho completo para a pasta bin dentro do diretório do Poppler (ex.: C:\Program Files\Poppler\bin).

Clique com o botão direito em Este Computador ou Meu Computador e selecione Propriedades.

Clique em Configurações Avançadas do Sistema.

Na aba Avançado, clique em Variáveis de Ambiente.

Encontre a variável Path na seção Variáveis do Sistema e clique em Editar.

Adicione o caminho para a pasta bin do Poppler e clique em OK.

Verifique se o Poppler está funcionando:

Abra o Prompt de Comando (CMD).

Digite o comando pdfimages -v.

Você deve ver informações sobre a versão do Poppler instalada.

3. Instalar Bibliotecas Python

Para executar o sistema, é necessário instalar as seguintes bibliotecas Python:

PyPDF2

pytesseract

pdf2image

Pillow

Passos:

Abra o terminal ou Prompt de Comando.

Execute os seguintes comandos para instalar as dependências:

pip install PyPDF2 pytesseract pdf2image pillow tk

Certifique-se de que todas as bibliotecas foram instaladas corretamente:

Execute pip list e verifique se os pacotes aparecem na lista.

Com essas etapas concluídas, o sistema estará pronto para ser executado corretamente!

