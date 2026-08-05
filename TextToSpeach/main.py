# pip install gTTS

from gtts import gTTS
text = "Hello Fatima, i wish u all the best. " \
"You will be accepted from KAIST, just dont give up."

tts = gTTS(text = text, lang="en")
tts.save("voice.mp3")
print("audio saved successfully")

