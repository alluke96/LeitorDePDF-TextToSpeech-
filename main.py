import pyttsx3
import PyPDF2

book = open('book.pdf', 'rb')  # Declare o nome do livro como book
pdfReader = PyPDF2.PdfFileReader(book)  # Inicializando o leitor de pdf
speaker = pyttsx3.init()  # Inicializando a voz que vai falar

pages = pdfReader.numPages  # Identificando quantas páginas o arquivo tem
initialPage = 0  # Pegando desde a primeira página (pode ser substituído)

for index in range(initialPage, pages):
    page = pdfReader.getPage(index)  # Pegar o conteúdo da página
    text = page.extractText()  # Extraindo o texto daquela página
    speaker.say(text)  # Falar o texto
    speaker.runAndWait()  # Falar o texto
