import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import os
import sys
import winsound
import time

# ----------------- Setup -----------------
engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def talk(text):
    print("🎙️ RAM:", text)
    engine.say(text)
    engine.runAndWait() 

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening... Say 'Ram' to activate.")
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("🗣️ You said:", command)
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        talk("Network issue with Google service.")
        return ""
    return command

# ----------------- Alarm Function -----------------
def set_alarm(alarm_time):
    talk(f"Alarm set for {alarm_time} ⏰")
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == alarm_time:
            talk("Wake up! ⏰ Time’s up!")
            winsound.Beep(2000, 1000)  # beep 1 second
            break
        time.sleep(20)  # check every 20 seconds

# ----------------- Core Commands -----------------
def run_ram(command):
    if "play" in command:
        song = command.replace("play", "").strip()
        talk("Playing on YouTube 🎶")
        pywhatkit.playonyt(song)

    elif "open youtube" in command:
        talk("Opening YouTube 🌐")
        os.system("start https://www.youtube.com")

    elif "open chrome" in command:
        try:
            talk("Opening Chrome 🚀")
            os.system("start chrome")
        except:
            talk("Chrome not found 😬")

    elif "open code" in command or "open vs code" in command:
        talk("Opening VS Code 💻")
        os.system("code")

    elif "open explorer" in command:
        talk("Opening File Explorer 🗂️")
        os.system("explorer")

    elif "time" in command:
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"It’s {time_now} ⏰")

    elif "date" in command:
        today = datetime.datetime.now().strftime("%A, %d %B %Y")
        talk(f"Today is {today} 📅")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "search" in command:
        topic = command.replace("search", "").strip()
        if topic:
            talk(f"Searching Google for {topic} 🌐")
            pywhatkit.search(topic)
        else:
            talk("Please say the topic to search for.")

    elif "set alarm" in command:
        time_str = command.replace("set alarm", "").strip()
        if time_str:
            set_alarm(time_str)
        else:
            talk("Please tell me the time for the alarm in HH:MM format, e.g., Ram set alarm 07:30")

    else:
        talk("I heard you, but I don’t understand that yet 😅")

# ----------------- Main Loop -----------------
talk("Guess who’s here? It’s Ram – smarter than Siri, cooler than Alexa 😅")
while True:
    command = take_command()

    if "stop" in command or "exit" in command:
        talk("Shutting down… but remember, I’ll miss you 😜")
        sys.exit()

    elif "ram" in command:
        winsound.Beep(1000, 300)  # confirmation beep
        command = command.replace("ram", "").strip()
        if command != "":
            run_ram(command)
        else:
            talk("Yes? What can I do for you?")
