import speech_recognition as sr
import pyttsx3
# Text-to-Speech Engine

engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)

            print(f"You: {command}")

            return command.lower()

        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""

        except sr.RequestError:
            print("Speech service unavailable")
            return ""

        except Exception as e:
            print("Error:", e)
            return ""
