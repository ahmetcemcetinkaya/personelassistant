import speech_recognition as sr

def voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            return r.recognize_google(audio)
        except LookupError:                           
                print "Could not understand audio"


