from assistant import speak
import datetime

def process_command(command):

    if "hello" in command:
        speak("Hello, how can I help you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    elif "your name" in command:
        speak("My name is Nova Assistant")

    elif "how are you" in command:
        speak("I am fine and ready to help you")

    elif "exit" in command:
        speak("Goodbye")
        return False

    else:
        speak("Sorry, I don't understand that command")

    return True