<h3>Implementing speech synthesis(📖 to 🗣) on eBooks</h3>

Bored of writing notes in a lecture? How about we convert the notes dictated by the lecturer into text?
Use the **speechtotext.py** script to get the text format of spoken notes, which saves the text in a .txt file.
<br>
Too lazy to read a novel? Get an Ebook version of the novel and run the **ebook_reader.py** script. It will generate an mp3(audio) format of the book. Enjoy book listening :)
<br><br>
An **example** of each of the script is shown, the text from **_spoken text.PNG_** was delivered by me, observe the **s2txt.txt** it is the output (accurate to a great extent if you have a decent english speaking accent)<br>
Listen to the **read.mp3** and observe the page numbers which are spoken from the pdf file. (eg of ebook reader) 

### Prerequisite

**For Windows Users***
- Install tesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki).
- Add tesseract to your environment variable. (Add this path C:\Program Files (x86)\Tesseract-OCR)
- Type 'tesseract' in cmd you wil get a lot of options like this. 
- (**_Optional:_ This step should be done only if you get an error which gives the below error** )Add a new variable in environment variable **TESSDATA_PREFIX** and give it _C:\Program Files (x86)\Tesseract-OCR\tessdata_ this value.
```
Please make sure the TESSDATA_PREFIX environment variable is set to the parent directory of your "tessdata" directory.
```

**For Linux Users**


<h3>How to run:</h3>
Run these commands in cmd/terminal of a directory.<br>
**NOTE: You need to complete the steps mentioned in Prerequisite**
```git
git clone https://github.com/globefire/speech-recognition-Ebook-Reader.git
cd speech-recognition-Ebook-Reader
pip install -r requirements.txt
python speechtotext.py
python ebook_reader.py
```

### Features to add:
- [ ] Web Interface (It allows user to upload a pdf file and provide a audio file for the same). (@sladyn98)

- [X] use tesseract to extract text from files. (@globefire)