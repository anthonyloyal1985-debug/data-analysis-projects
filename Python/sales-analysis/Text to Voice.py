import pyttsx4 as tts #This line will import text to speech python library
import datetime as dt #This line will import date time library

#Defining the function to convert text into voice
def text_to_voice():
    print(text) #This statement will print message given to it
    voice_engine = tts.init() #This statement will create a voice engine
    voice_engine.say(text) #This statement is giving the text to voice engine
    voice_engine.runAndWait() #This statement will say to speak the text and wait till it finish

current_date_time = dt.datetime.now()
#print(current_date_time)

current_hour = current_date_time.hour
#print(current_hour)

if current_hour < 12:
    text = "Hello, Good morning, Sir"
elif current_hour < 18:
    text = "Hello, Good afternoon, Sir"
else:
    text = "Hello, Good evening, Sir"

#Calling the function text_to_voice
text_to_voice()

while True:
    text = input("Enter the text that you want to convert into voice(Enter s to stop): ")

    if text == 's':
        break

    #Calling the function text_to_voice
    text_to_voice()

text = "Bye, I am leaving now, Sir"
#Calling the function text_to_voice
text_to_voice()













