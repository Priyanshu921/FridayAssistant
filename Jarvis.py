import pyttsx3,datetime,os
import speech_recognition as sr
import webbrowser,wikipedia
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)                           
engine.setProperty('rate',140)
lang=engine.setProperty("language",'hindi')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Sir!")
    elif hour>=13 and hour<=16:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("Friday Connecting......")
    speak("Friday Connected")
    speak("How May I help you sir?")
def takeCommand():
    ''' taking the input as speech and returning as string'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User Said {query}\n")
    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"
    return query
if __name__=='__main__':
    wishme()
    query=takeCommand().lower()
    firefoxpath="C:/Program Files/Mozilla Firefox/firefox.exe %s"
    if 'open google' in query:
        speak("opening google in firefox")
        webbrowser.get(firefoxpath).open_new_tab('google.co.in')
    elif 'open youtube' in query:
        speak("opening youtube in firefox")
        webbrowser.get(firefoxpath).open_new_tab('youtube.com')
    elif 'wikipedia' in query:
        wiki = query.replace('wikipedia','')
        wik=wikipedia.summary(wiki, sentences=2)
        speak(f"Searching for {wiki} on wikipedia.")
        speak(f"according to wikipedia {wik}")
    elif 'open code' in query:
        speak("opening VS Code")
        codepath = "C:\\Users\\Priyanshu Patidar\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
        os.startfile(codepath)
    elif 'time' in query:
        tim=datetime.datetime.now().strftime("%H:%M:%S")
        speak("The time is "+tim)
    elif 'current news' in query:
        speak("opening current news")
        webbrowser.get(firefoxpath).open_new_tab('google.com/news')
    else:
        speak("Sorry Sir,,I am not a fully functional program. Currently I am in my development phase. Please try contacting Priyanshu Patidar")