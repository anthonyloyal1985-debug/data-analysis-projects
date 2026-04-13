#Import the required libraries
import pyttsx4 as tts
import datetime as dt
import speech_recognition as sr

chat_bot_name = "Ether"

def text_to_voice(text):
    print(chat_bot_name, "said:", text)
    voice_engine = tts.init()
    voice_engine.say(text)
    voice_engine.runAndWait()

def voice_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as m:
        print(chat_bot_name, "saying: I am listening, please say something, Sir.")
        voice = r.listen(m)

    try:
        text = r.recognize_google(voice)
        return text
    except Exception:
        return None

def get_answer(question):
    if question in ('what is your name', 'what ise your name',
    "what's your name", "whats your name", 'what is yor name',
    "what's yor name", 'whats yor name'):
        answer = "My name is " + chat_bot_name + ", Sir."
    elif question in ('who are you', 'who r u', 'hu r u'):
        answer = "I am your chat bot, Sir."
    elif question in ('how are you', 'how r u'):
        answer = "I am fine thank you, Sir."
    elif question in ('who created you', 'hu created u',
    'who developed you', 'hu developed u'):
        answer = "I am created by INCAPP, Sir."
    else:
        answer = "I dont know about it, Sir"
    return answer

current_hour = dt.datetime.now().hour

if current_hour < 12:
    text = "Hello, Good morning, Sir"
elif current_hour < 18:
    text = "Hello, Good afternoon, Sir"
else:
    text = "Hello, Good evening, Sir"

text_to_voice(text)

while True:
    question = voice_to_text()

    if question is not None:
        if question == 'stop':
            print("You said:", question)
            break
        print("You asked:", question)
        answer = get_answer(question)
        text_to_voice(answer)  
    else:
        print("You asked:", question)
        text_to_voice("I did not understand what you said, Sir")

text_to_voice("Bye, I am stopping now, Sir")


















    

