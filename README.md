# RamAssistant

**RamAssistant** is a Python-based voice assistant that responds to voice commands to perform tasks like opening applications, playing YouTube videos, telling jokes, telling time/date, setting alarms, and searching online. It’s designed to be simple, interactive, and fun.  

---

## **Features**

- Plays songs on YouTube  
- Opens Chrome, VS Code, File Explorer, and YouTube  
- Tells current time and date  
- Tells jokes  
- Sets alarms  
- Searches Google  
- Custom wake word: "Ram"  
- Friendly, fun responses  

---

## **Libraries Used**

| **Library**               | **Purpose / Functionality**                                                    |
| --------------------      | ------------------------------------------------------------------------------ |
| **speech_recognition**    | Captures microphone input and converts spoken words into text.                 |
| **pyttsx3**               | Converts text to speech so Ram can “talk” back to the user.                    |
| **pywhatkit**             | Plays YouTube videos, searches topics online, and automates certain tasks.     |
| **datetime**              | Provides functions for date, time, and alarm checking.                         |
| **pyjokes**               | Generates random jokes to make interactions fun.                               |
| **os**                    | Opens applications (Chrome, VS Code, File Explorer) and web URLs.              |
| **sys**                   | Allows the program to exit gracefully when “stop” or “exit” is commanded.      |
| **winsound**              | Plays beep sounds on Windows for wake word confirmation or alarm notification. |
| **time**                  | Provides delays (sleep) for repeatedly checking alarm time.                    |

---

## **How It Works**

**1. Wake Word Detection:**
        Ram listens for the word "Ram". A short beep confirms it has detected the wake word.

**2. Speech Recognition:**
        Converts your voice input into text using speech_recognition.

**3. Command Processing:**
        The assistant checks your command against predefined tasks and executes the appropriate action.
 
**4. Text-to-Speech:**
        Ram responds using pyttsx3.

**5. Additional Features:**
       Can play YouTube videos, open apps, tell jokes, give time/date, and set alarms.
