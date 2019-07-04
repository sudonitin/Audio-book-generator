##SINGLE IMAGE SPEECH AND TXT##
######Tesseract code is here#########
from PIL import Image
import pytesseract
import warnings
warnings.simplefilter('ignore')
# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
content = pytesseract.image_to_string(Image.open('spoken text.PNG'))
######Tesseract ends HERE#########


##writing to file
file = open("test.txt", "w")
file.write(content)
file.close()
##writing ends here

##generating audio file
from gtts import gTTS
file = open("test.txt", "r")
txt = file.read()
tts = gTTS(text = txt, lang = 'en')
tts.save("read.mp3")
file.close()
