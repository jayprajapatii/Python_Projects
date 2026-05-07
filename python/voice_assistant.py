import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext(): #speech to text print
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing....")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print(" Not Understand ")
            
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',120)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    
        if "jarvis" in  sptext().lower() :
                while True:
                    data1=sptext().lower()
                    
                    if "your name" in data1:
                        name=" my name is jay"
                        speechtx(name)
                    elif "old are you" in data1:
                        age = "i am twenty-two years old"
                        speechtx(age)
                    elif "time" in data1:
                        time = datetime.datetime.now().strftime("%I%M%p")
                        speechtx(time)
                    elif "youtube" in data1:
                        webbrowser.open("https://www.youtube.com/")
                    
                    elif "instagram" in data1:
                        webbrowser.open("https://www.instagram.com/")
                    
                    elif "play song" in data1:
                        add = "D:\jay\song"
                        listsong = os.listdir(add)
                        print(listsong)
                        os.startfile(os.path.join(add,listsong[0]))
                        
                    elif "exit" in data1:
                        speechtx("thank you")
                        break
                    
                    time.sleep(5)        
        else:
            print("thanks") 
        
            
    
    
    
    
    
    