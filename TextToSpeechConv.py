from gtts import gTTS
import os
text = input("Enter the text you want to convert to speech: ")
language = 'en'
desktop_folder = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = os.path.join(desktop_folder, "voice.mp3")
tts = gTTS(text=text, lang=language)
tts.save(file_path)
print("Text has been converted to speech and saved as 'voice.mp3' successfully!")
print("File location:", file_path)
