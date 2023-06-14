import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import os
# from googlesearch import search 

engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    #engine.say will speak audio string
    engine.runAndWait()
    #This function will make the speech audible in the system

def wishMe():
    hour=int(datetime.datetime.now().hour)
    #will return hour in range of 0-24 and we typecasted it into int
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!") 

    else:
        speak("Good Evening Sir!")               
 
    speak("How can i help you?")

def takeCommand():
    #it takes audio input by microphone from user and returns string output

    r=sr.Recognizer()
    #helps to recognise input audio
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        #written cuz if i take the gap of 1 sec the program doesnot assume that speeking is done that's why it is increased a bit
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #if there is error in recognizing by google like it can't understand and all then it will show say it again
        # print(e)    
        # speak("Say that again please...")
        print("Say that again please...")
        return "None"
        #returning none string
    return query


if __name__ == "__main__" :
    wishMe()
    #speak("Please say something")
    while True:
        query=takeCommand().lower()
    
    #Logic for executing tasks based on query
        if 'wikipedia' in query:
        #it will check whether a 'wikipedia' word is present in query    
            speak("Searching in wikipedia...")
            query=query.replace("wikipedia","")
            #means we are removing wikipedia word from query
            results = wikipedia.summary(query , sentences=1)
            #here results will come from wikipedia and will give me 2 sentences from wikipedia in string
            speak("According to wikipedia") 
            print(results) 
            speak(results) 

        elif 'youtube' in query and 'play' in query:
            query=query.replace("youtube","")
            query=query.replace("play","")
            webbrowser.open_new("https://www.youtube.com/results?search_query="+query) 

        elif 'open google' in query:
            webbrowser.open("google.com")  

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'search' in query or 'find' in query:
            query=query.replace("search","")
            query=query.replace("find","")
            webbrowser.open("https://www.google.com/search?q=" + query)    

        elif 'play series' in query:
            series_path="C:\\Users\\KIIT\\Videos\\ITS OKAY TO NOT BE OKAY"
            eps=os.listdir(series_path)
            os.startfile(os.path.join(series_path,eps[0]))

        elif 'wait' in query:
            speak("will wait for your next command")
            print("Waiting...")
            while True:
                query=takeCommand().lower()
                if 'listen' in query:
                    speak("What can I do for you?")
                    break

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/search/" + location )        

        # elif 'search in google':
        #      query=query.replace("search in google","")
        #      for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        #             print(j)

        elif 'bye' in query:
            speak("Goodbye Sir! have a good day")
            break       


  
