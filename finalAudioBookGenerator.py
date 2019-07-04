import os
import tempfile
from pdf2image import convert_from_path
 
filename = 'test.pdf'
 
with tempfile.TemporaryDirectory() as path:
     images_from_path = convert_from_path(filename, output_folder='F:/python projects cv tts stt/speechrecog', last_page=2, first_page =0)
 
base_filename  =  os.path.splitext(os.path.basename(filename))[0] + '.JPG'     
 
save_dir = 'F:/python projects cv tts stt/speechrecog'
i=1

######Tesseract code is here#########
from PIL import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
######Tesseract ends HERE#########

file = open("test.txt", "w")
for page in images_from_path:
    name = os.path.splitext(os.path.basename(filename))[0] + str(i) +'.JPG'
    page.save(os.path.join(save_dir, name), 'JPEG')
    i+=1
    file.write(pytesseract.image_to_string(Image.open(name)))


file.close()

###Audio file generating###
from gtts import gTTS
file = open("test.txt", "r")
txt = file.read()
tts = gTTS(text = txt, lang = 'en')
tts.save("read.mp3")
file.close()











##last edited 5/7/19 Developed By Nitin Sahu github.com/globefire
