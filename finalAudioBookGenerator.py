import os
import tempfile
from pdf2image import convert_from_path
import warnings
from PIL import Image
import pytesseract
from gtts import gTTS

warnings.simplefilter('ignore') 
filename = 'test.pdf'
save_dir = os.path.join(os.path.dirname(os.path.realpath('finalAudioBookGenerator.py')),'auxillary') 


#this code creates a temporary image of ppm format
with tempfile.TemporaryDirectory() as path:
     images_from_path = convert_from_path(filename, output_folder=save_dir, last_page=2, first_page =0)
 
######Tesseract code is here#########
# If you don't have tesseract executable in your PATH, include the following: setting up tesseract
# linux users follow this tutorial https://www.linux.com/tutorials/using-tesseract-ubuntu/
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
######Tesseract ends HERE#########

file = open("test.txt", "w")
i = 1
for page in images_from_path:
    name = os.path.splitext(os.path.basename(filename))[0] + str(i) +'.JPG'
    page.save(os.path.join(save_dir, name), 'JPEG')
    i+=1
    file.write(pytesseract.image_to_string(Image.open(os.path.join(save_dir, name))))
file.close()


###Audio file generating###
file = open("test.txt", "r")
txt = file.read()
tts = gTTS(text = txt, lang = 'en')
tts.save("read.mp3")
file.close()