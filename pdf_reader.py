import PyPDF2
import pyttsx3
from tkinter.filedialog import *

book= askopenfilenames()
pdfreader=PyPDF2.PdfFileReader(book)
pages= pdfreader.numPages

for num in range(0, pages):
    page=pdfreader.getPage(num)
    text=page.extractText()
    player= pyttsx3.init()
    player.say(text)
    player.runAndWait()
