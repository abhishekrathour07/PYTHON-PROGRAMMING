import speech_recognition as sr


recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening for a command...")
    audio = recognizer.listen(source)

    try:
      
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        
     
        if "hello" in command.lower():
            print("Hello! How can I help you?")
        elif "goodbye" in command.lower():
            print("Goodbye!")
        else:
            print("Sorry, I don't understand that command.")

    except sr.UnknownValueError:
        print("Sorry, I could not understand your command.")
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
 