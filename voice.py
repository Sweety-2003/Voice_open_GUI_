import speech_recognition as sr

def recognize_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for the command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"Recognized command: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError:
        print("Could not request results from the recognition service.")
        return None

if __name__ == "__main__":
    while True:
        command = recognize_voice()
        if command:
            if "exit" in command:
                print("Exiting...")
                break
            elif "hello" in command:
                print("Hello! How can I help you?")
            else:
                print(f"Command not recognized: {command}")
