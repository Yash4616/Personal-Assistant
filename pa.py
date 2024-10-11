import time
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import pyautogui
import numpy as np
from scipy.signal import butter, lfilter
import random

GREETINGS = ["i am ready sir","your wish my command", "how can i help you sir?", "i am online and ready sir",
             "I'm at your service, sir","How may I assist you today, sir?","Ready and waiting for your command sir.",
             "Standing by for your instructions, sir.","I'm here and prepared to help, sir.",
             "Your request is my priority, sir.","Ready to assist at your convenience, sir.",
             "I'm online and eager to help, sir.","Here to serve and support, sir.",
             "Starting all systems applications","Installing and checking all drivers" ,
            "Calibrating and examining all the core processors" ,
            "Wait a moment sir" ,"All drivers are up and running" ,"All systems have been activated" ,
            "Now I am online" ]

REPLY = ["At your service, as always","Ready to assist, as per your command",
         "How may I be of service today","Here to help, as always","Prepared to help, as always",
         "Standing by to serve","At your beck and call", "On hand for any needs"]

GOING = ["Session terminated. Should you require any further assistance, please contact me at your convenience",
         "This session has concluded. For additional support or inquiries, do not hesitate to reach out.",
         "Concluding this session. Should further support or information be required, please initiate communication as needed."
         ,"I am formally ending this session. If you require further support or have additional inquiries, please contact me as needed.",
         "This interaction has been formally terminated. Should there be a need for further assistance or if additional questions arise, please make contact at your convenience."
         ]

engine = pyttsx3.init( )
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    strTime = datetime.datetime.now().strftime(" %I:%M %p")
    speak(f"Currently it is {strTime}")
    greeting = random.choice(GREETINGS)
    speak(greeting)
    print(greeting)

def takeCommand():
        # Use Google Speech Recognition
        recognizer = sr.Recognizer() 
        with sr.Microphone() as source:
            recognizer.energy_threshold = 1000  # Lower value increases sensitivity
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            recognizer.pause_threshold = 0.5
            try:
                audio = recognizer.listen(source)
                print("Initiating Command...")
                query = recognizer.recognize_google(audio, language='en-in')
                print(f"User said: {query}\n")
                return query
            except sr.UnknownValueError:
                print("Could you repeat that sir")
                return "None"
            except sr.RequestError:
                print("Sorry sir, my speech services are offline")
                speak("Sorry sir, my speech services are offline")
                return "None"

    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'stop' in query or 'play' in query:
            if time.sleep(0.5):
                pyautogui.press('space')
                speak("Spotify control initiated")
            else:
                speak("Spotify not found at the specified path.")

        elif 'good' in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                reply = random.choice(REPLY)
                speak("Good Morning sir")
                speak(reply)
            elif hour >= 12 and hour < 18:
                reply = random.choice(REPLY)
                speak("Good Afternoon sir")
                speak(reply)
            elif hour >= 18 :
                reply = random.choice(REPLY)
                speak("Good Evening sir")
                speak(reply)
            else:
                reply = random.choice(REPLY)
                speak("Good Night sir")
                speak(reply)

        elif 'chat gpt' in query:
            webbrowser.get('windows-default').open("https://chatgpt.com/")
            speak("program Initiated")

        elif 'google' in query:
            webbrowser.get('windows-default').open("https://google.com/")
            speak("program Initiated")

        elif 'Jarvis' in query:
            reply = random.choice(REPLY)
            speak('yes sir')
            speak(reply)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%d %m %Y - %I:%M %p")
            speak(f"Currently its {strTime}")
            print(strTime)

        elif 'opera' in query:
            codePath = "C:\\Users\\"User name"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Opera GX Browser.lnk"
            if os.path.exists(codePath):
                os.startfile(codePath)
                speak("program Initiated")
            else:
                speak("opera not found at the specified path.")

        elif 'pc manager' in query:
                    pyautogui.hotkey('win', 's') 
                    time.sleep(0.5)
                    pyautogui.write('pc manager')
                    pyautogui.press('enter')

        elif 'mail' in query:
            codePath = "C:\\Users\\"User name"\\AppData\\Local\\Microsoft\\WindowsApps\\olk.exe"
            if os.path.exists(codePath):
                os.startfile(codePath)
                speak("program Initiated")
            else:
                speak("Mail not found at the specified path.")

        elif 'task manager' in query:
            codePath = "C:\\Windows\\System32\\Taskmgr.exe"
            if os.path.exists(codePath):
                os.startfile(codePath)
                speak("program Initiated")
            else:
                speak("task manager not found at the specified path.")

        elif 'obsidian' in query:
            codePath = "C:\\Users\\"User name"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Obsidian.lnk"
            if os.path.exists(codePath):
                os.startfile(codePath)
                speak("program Initiated")
            else:
                speak("obsidian not found at the specified path.")

        elif 'notepad' in query:
            codePath = "C:\\Users\\"User name"\\AppData\\Local\\Microsoft\\WindowsApps\\notepad.exe"
            if os.path.exists(codePath):
                os.startfile(codePath)
                speak("program Initiated")
            else:
                speak("Notepad not found at the specified path.")

        elif 'notes' in query:
            codePath = "C:\\Users\\"User name"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps\\Google Keep.lnk"
            if os.path.exists(codePath):
                os.startfile(codePath)
                speak("program Initiated")
            else:
                speak("Notes not found at the specified path.")

        elif 'armoury crate' in query:
            codePath = "C:\\Users\\"User name"\\AppData\\Local\\Microsoft\\WindowsApps\\ArmouryCrate.exe"
            if os.path.exists(codePath):
                os.startfile(codePath)
                speak("program Initiated")
            else:
                speak("Armoury Crate not found at the specified path.")

        elif 'nvidia app' in query:
            codePath = "C:\\Program Files\\NVIDIA Corporation\\NVIDIA app\\CEF\\NVIDIA app.exe"
            if os.path.exists(codePath):
                os.startfile(codePath)
                speak("program Initiated")
            else:
                speak("nvidia app not found at the specified path.")

        elif 'overlay' in query:
            pyautogui.hotkey('altleft', 'r')
        
        elif 'close' in query:
            if query.startswith("close"):
                pyautogui.hotkey('altleft', 'tab')  
                time.sleep(1)
                pyautogui.hotkey('altleft', 'f4')

        elif 'run search' in query or 'open' in query:
                speak("What are you looking for")
                search_query = takeCommand().lower()
                if search_query and search_query !='none':
                    pyautogui.hotkey('win', 's') 
                    time.sleep(0.5)
                    pyautogui.write(search_query)
                    time.sleep(0.5)
                    pyautogui.press('enter')
                    speak("Access Granted")
                else:
                    speak("I didn't catch that.Please try again later .") 

        elif 'file explorer' in query:
            codePath = "C:\\Windows\\explorer.exe"
            if os.path.exists(codePath):
                os.startfile(codePath)
                speak("program Initiated")
            else:
                speak("explorer not found at the specified path.")

        elif 'github' in query:
            codePath = "C:\\Users\\"User name"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps\\GitHub.lnk"
            if os.path.exists(codePath):
                os.startfile(codePath)
                speak("program Initiated")
            else:
                speak("github not found at the specified path.")

        elif 'terminal' in query:
            codePath = "C:\\Users\\"User name"\\AppData\\Local\\Microsoft\\WindowsApps\\wt.exe"
            if os.path.exists(codePath):
                os.startfile(codePath)
                speak("program Initiated")
            else:
                speak("Terminal not found at the specified path.")

        elif 'quit' in query:
            going = random.choice(GOING)
            speak(going)
            os._exit(0)
        elif 'exit' in query:
            if query.startswith("exit"): 
                pyautogui.hotkey('altleft', 'f4')
                speak('closing app')
        elif 'leave' in query:
            going = random.choice(GOING)
            speak(going)
            os._exit(0)
        elif 'bye' in query:
            going = random.choice(GOING)
            speak(going)
            os._exit(0)

        elif 'search on chrome' in query:
            speak('What do you want to search ')
            search_query = takeCommand().lower()
            if search_query and search_query != "none":
                codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe "
                if os.path.exists(codePath):
                    os.startfile(codePath)
                search_url = (f"https://www.google.com/search?q={search_query}")
                time.sleep(0.5)
                pyautogui.write(search_url)
                pyautogui.press("enter")
                speak(f"Searching Google for {search_query}")
            else:
                speak("I didn't catch that.Please try again later .")

        elif 'search on brave' in query:
            speak('What do you want to search on brave')
            search_query = takeCommand().lower()
            if search_query and search_query != "none":
                # Construct the search URL
                search_url = f'https://search.brave.com/search?q={search_query}'
                webbrowser.open(search_url)
            else:
                speak("I didn't catch that. Please try again.")

        elif 'type' in query or 'note down' in query:
            speak('What do you want to write')
            search_query = takeCommand().lower()
            if search_query and search_query != "none":
                # Construct the search URL
                pyautogui.write(search_query)
                pyautogui.press("enter")
            else:
                speak("I didn't catch that. Please try again.")

        elif 'search on youtube' in query:
            speak('What do you want to search on youtube, sir?')
            search_query = takeCommand().lower()
            if search_query and search_query != "none":
                # Construct the search URL
                search_url = f'https://www.youtube.com/search?q={search_query}'
                webbrowser.open(search_url)
            else:
                speak("I didn't catch that. Please try again.")

        elif 'start ai' in query:
            codePath = "C:\\Users\\"User name"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Ollama.lnk"
            if os.path.exists(codePath):
                os.startfile(codePath)
                time.sleep(2)
            codePath = "C:\\Users\\"User name"\\AppData\\Local\\Microsoft\\WindowsApps\\wt.exe"
            if os.path.exists(codePath):
                os.startfile(codePath)
                time.sleep(2)
                pyautogui.write('ollama run llama3.1')
                time.sleep(2)
                pyautogui.press('enter')
                speak("Offline artificial intelligence protocol initiated")
            else:
                speak("artificial intelligence not found at the specified path.") 
