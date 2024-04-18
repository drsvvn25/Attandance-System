# import the following libraries
import pytesseract
from PIL import Image
import pyttsx3
from googletrans import Translator

# opening an image from the source path
img = Image.open('text1.png')

# describes image format in the output
# print(img)
# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)

# write text in a text file and save it to source path
with open('abc.txt', mode='w') as file:
    file.write(result)
    print(result)

p = Translator()

# translates the text into english language
translation = p.translate(result, dest='en')
# Take only the first line of the translated text
translated_text = translation.text.split('\n')[0::]
print(translated_text)

# Initiate the text-to-speech engine
engine = pyttsx3.init()

# An audio will be played which speaks the text if pyttsx3 recognizes it
engine.say(translated_text)
engine.runAndWait()
