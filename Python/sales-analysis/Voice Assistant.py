#Importing the required libraries
import pyttsx4 as tts
import speech_recognition as sr
import datetime as dt
import os
import google.genai as genai

class VoiceAssistant:
    def __init__(self, name = "Ether"):
        self.name = name
        self.client = genai.Client(api_key=os.environ['Gemini API Key'])
        greet_message = "Hello, Good "
        current_hour = dt.datetime.now().hour
        if current_hour < 12:
            greet_message += "morning"
        elif current_hour < 18:
            greet_message += "afternoon"
        else:
            greet_message += "evening"
        greet_message += ", Sir"
        self.text_to_voice(greet_message)
        
    def text_to_voice(self, text):
        print(self.name, "said:", text)
        voice_engine = tts.init()
        voice_engine.say(text)
        voice_engine.runAndWait()
        
    def voice_to_text(self):
        r = sr.Recognizer()
        with sr.Microphone() as m:
            print(self.name, "is saying: I am listening, please say something")
            voice = r.listen(m)
        try:
            text = r.recognize_google(voice)
        except Exception:
            return None
        else:
            return text
        
    def get_answer(self, question):
        if question in ("what is your name", 'what is yor name', 
        "what's your name", "whats your name", "whats yor name"):
            answer = "My name is " + self.name + ", Sir"
        elif question in ('who are you', 'hu are you', 'hu r u'):
            answer = "I am your voice assistant, Sir"
        elif question in ('how are you', 'how r u'):
            answer = "I am fine thank you, Sir"
        elif question in ('who created you', 'hu created you',
        'who developed you', 'hu developed you'):
            answer = "I am developed by Praveen, Sir"
        elif 'what' in question or 'why' in question or 'when' in question or 'how' in question or 'tell' in question:
            answer = self.client.models.generate_content(model='gemini-2.5-flash', contents=question + " and keep it short")
            is_ai_genereted = True
            is_long_answer = False
            return answer, is_ai_genereted, is_long_answer
        elif 'create' in question or 'generate' in question or 'write' in question:
            answer = self.client.models.generate_content_stream(model='gemini-2.5-flash', contents=question + " and keep it in 100 words only")
            is_ai_genereted = True
            is_long_answer = True
            return answer, is_ai_genereted, is_long_answer
        else:
            answer = "I don't know about it, Sir"
        is_ai_genereted = False
        is_long_answer = False
        return answer, is_ai_genereted, is_long_answer

va = VoiceAssistant()
while True:
    question = va.voice_to_text()
    if question is not None:
        question = question.lower()
        if question in ('stop', 'exit', 'quit'):
            print("You said:", question)    
            break
        print("You asked:", question)
        answer, is_ai_genereted, is_long_answer = va.get_answer(question)
        if is_ai_genereted and is_long_answer:
            va.text_to_voice("Please wait, I am getting your answer, Sir")
            for line in answer:
                line = line.text
                if '*' in line:
                    line = line.replace("*", "")
                if '#' in line:
                    line = line.replace('#', '')
                print(line)
            va.text_to_voice("End of your answer, Sir")
        elif is_ai_genereted and not is_long_answer:
            answer = answer.text
            if '*' in answer:
                answer = answer.replace("*", "")
            if '#' in answer:
                answer = answer.replace('#', '')
            va.text_to_voice(answer)
        else:
            va.text_to_voice(answer)
    else:
        va.text_to_voice("I didn't understand what you said, Sir")
va.text_to_voice("Bye, I am leaving now, Sir")