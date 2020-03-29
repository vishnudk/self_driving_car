import win32com.client as wincl
def speak_the_text(text):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(text)