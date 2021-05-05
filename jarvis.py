import pyttsx3
import random
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Jarvis. Please tell me how may I help you ")
def takeCommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sid18throttlerz@gmail.com', 'Siddharth8604')
    server.sendmail('sid18throttlerz@gmail.com', to, content)
    server.close()
if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            try:
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences = 1)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                print("Cannot search...")
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open flipkart' in query:
            webbrowser.open('flipkart.com')
        elif 'play music' in query:
            music_dir = 'C:\\Music'
            songs = os.listdir(music_dir)
            no = random.randint(0,7)
            os.startfile(os.path.join(music_dir, songs[no]))
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is: {strTime}")
        elif "how are you" in query:
            speak("I am great Sir. How are you!!")
        elif "open chrome" in query:
            chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)
        elif "open whatsapp" in query:
            whatsapp_path = "C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(whatsapp_path)
        elif "send mail" in query:
            try:
                speak("What should i say")
                content = takeCommand()
                to = "sid864harth@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry.. I am not able to send this email")
        elif "my name" in query:
            speak("Your name is Siddharth")
        elif "my phone number" in query:
            speak("Your phone number is 8389046987")
        elif "my age" in query:
            speak("Your age is 17")
        elif "stop" in query:
            speak("Ok Sir")
            exit()