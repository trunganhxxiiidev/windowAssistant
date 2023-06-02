from gtts import gTTS
import playsound
import time
import os
#from Speechtotext import S


def text_speech(text):
    if (os.path.isfile('./output.mp3')):
        os.remove('./output.mp3')
    output = gTTS(text,lang="vi", slow=False)
    output.save('./output.mp3')
    time.sleep(7)
    playsound.playsound('./output.mp3')



