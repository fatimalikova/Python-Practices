# pip install openai-whisper

import whisper
model = whisper.load_model("base") # base = small with good accuracy
result = model.transcribe("voice.mp3")

print(result["text"])