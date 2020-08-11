#change 'email' to your email 'password' to your password to removw the error 
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyaudio
import os
import smtplib
import requests
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Robert Sir. Please tell me how may i help you")

def takeCommand():
    # It takes microphone input from the user and returs string output
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
        print("Say that again please...")
        return "None"    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email','password')
    server.sendmail('email', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #Logic for execute tasks based query
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Yash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to yash' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receiver_email"    
                sendEmail(to, content)
                speak("Email has been sent!")
            
            except Exception as e:
                print(e)
                speak("Sorry my friend yash. I am not able to send this email")  

        elif 'weather' in query:
            api_address='http://api.openweathermap.org/data/2.5/weather?appid=7c4bb4a0091ed04b260de4ee9e7433f7&q='
            speak('please tell city name')
            city = takeCommand()    #('City Name :')
            url = api_address + city
            json_data = requests.get(url).json()
            format_add = json_data['weather'][0]['description']   #['base']
            speak(format_add)

        elif 'news' in query:
            speak('news for today')
            url = 'http://newsapi.org/v2/everything?q=bitcoin&from=2020-06-17&sortBy=publishedAt&apiKey=f8d4e1c2134c44a1abcfe8a1916097e2'
            news = requests.get(url).text
            news_dict = json.loads(news)

            print(news_dict["articles"])
            arts = news_dict['articles']
            for article in arts:
                speak(article['title'])
                speak("Moving on to the next news..")

