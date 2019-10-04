import speech_recognition as SR
import pyttsx3
engine = pyttsx3.init()
speed = engine.getProperty('rate')
engine.setProperty('rate', speed-50)

def read_email():
    email = 'Hello, this is a test'
    engine.say(email)
    engine.runAndWait()
def write_email():
    rec = SR.Recognizer()
    engine.say("Please tell the content of your mail.")
    engine.runAndWait()
    with SR.Microphone() as source:
        audio = rec.listen(source)
        try:
            text = rec.recognize_google(audio)

            engine.say("You said: " + text)
            engine.runAndWait()

            print("Success: " + text)
            return text
        except:
            engine.say("Could not recognize what you said.")
            engine.runAndWait()
            print('Error')
    a = 0
def check_inbox():
    oyee = 0
    return oyee

def main():
    engine.say("Welcome to Voice to Email.")
    engine.runAndWait()
    rec = SR.Recognizer()
    option = ' '
    while option != 'quit':
        option = ' '
        with SR.Microphone() as source:
            engine.say("Now you can choose, read new mails, check inbox, write a new mail, and quit.")
            engine.say("Please make a choice")
            engine.runAndWait()
            audio = rec.listen(source)
            try:
                option = rec.recognize_google(audio)
                print("Success: " + option)
            except:
                engine.say("Could not recognize what you said.")
                engine.runAndWait()
                print('Error')
        if option == 'read email' or option == 'read emails' or option == 'read new email' or option == 'read new emails':
            read_email()
        elif option == 'write a new mail' or option == 'write new mail' or option == 'write a mail' or option == 'write mail' or option == 'write mails' or option == 'write new mails':
            write_email()
    if option == 'quit':
        engine.say("Goodbye")
        engine.runAndWait()
    option = ' '

main()
