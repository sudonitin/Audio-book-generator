import PyPDF2
file = open("test.txt", "w")
pdfFile = open('test.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
for i in range(30,33):#use pdfReader.numPages to get the audio for full book
    pageObj = pdfReader.getPage(i)
    file.write(pageObj.extractText())
    
file.close()



from gtts import gTTS
file = open("test.txt", "r")
txt = file.read()
tts = gTTS(text = txt, lang = 'en')
tts.save("read.mp3")
file.close()
