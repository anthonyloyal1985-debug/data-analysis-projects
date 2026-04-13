import speech_recognition as sr #Importing the speech recognition library

while True:

    r = sr.Recognizer()

    with sr.Microphone() as m:
        print("Please say something, I am listening")

        voice = r.listen(m)


    try:
        text = r.recognize_google(voice)
        if text == 'stop':
            print(text)
            break
        print(text)
    except Exception:
        print("I did not understand what you said")
        
