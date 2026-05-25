from assistant import listen, speak
from commands import process_command

def main():
    speak("Voice Assistant Started")

    running = True

    while running:
        command = listen()

        if command:
            running = process_command(command)

if __name__ == "__main__":
    main()