import pypdf
import gtts
from pypdf import PdfReader

#reader = PdfReader("day 4 tasks completed.pdf")



from gtts import gTTS
tts = gTTS('hello welcome to pythonlife', lang='en')
tts.save('hello.mp3')