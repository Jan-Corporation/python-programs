import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from googlesearch import search
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('I am your Arctic Assistant')
engine.say('What can I do for you')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'arctic' in command:
                command = command.replace('arctic', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Currently it is ' + time)
    elif 'tell me about' in command:
        about = command.replace('tell me about', '')
        info = wikipedia.summary(about, 20)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())      
    if 'play the video' in command:
        video = command.replace('play the video', '')
        talk('playing the video ' + video)
        pywhatkit.playonyt(video)
    if "i'm bored" in command:
        talk('I will tell you a joke to cheer you up')
        talk(pyjokes.get_joke())
    if 'what can you do' in command:
        talk('I can play videos, music, tell you the time and there is much more fun stuff to explore')
    if 'search the web for' in command:
        search_term = command.split("for")[-1]
        search_term = command.replace('search the web for', '')
        url = f"https://duckduckgo.com/?q={search_term}"
        webbrowser.get().open(url)
        talk(f'Here is what I found for {search_term} on duckduckgo')
    if 'open discord' in command:
        webbrowser.open("https://discord.com")
        talk('Opening Discord')
    if 'open youtube' in command:
        webbrowser.open("https://youtube.com")
        talk('Opening Youtube')
    if 'open gmail' in command:
        webbrowser.open("https://gmail.com")
        talk('Opening Gmail')
        
run_alexa()

