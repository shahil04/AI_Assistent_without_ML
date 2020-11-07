#text to speech

import pyttsx3 #pip install pyttsx3 for text to speech
import wikipedia #pip install wikipedia for use wikipedia search
import smtplib # already install in python for send mail 
import pyjokes #pip install pyjokes
import speech_recognition as sr # pip install speechrecognition for voice to text 
import datetime
#lession 12  chrome search
import webbrowser as wb #for  webbrowser search
# lession 13 logout,shutdown resart function
import os
import pyautogui #pip install pyauto gui for use screenshot 
import psutil #pip install psutil for ckeck cpu and battery status



engine = pyttsx3.init() #initialize the function
#lession 3  voice option and speak rate
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) #0 for female 1 for  anoter 2 for another so on...

new_voice_rate=170  
engine.setProperty('rate',new_voice_rate)

#lesson 2 speak functon or create as a function
def speak(words):
    engine.say(words)
    engine.runAndWait()

#call single speak function for check
#speak('this is function speak')

#lession 4 time functoin
def times():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)

#times()

#lession 5 date functon
def date():
    year = int(datetime.datetime.now().year)
    month= int(datetime.datetime.now().month)
    day  = int(datetime.datetime.now().day)
    speak('the current date is')
    speak(day)
    speak(month)
    speak(year)

#date()

#lession 6 greet us
def great():
    speak('welcome back sir!')
    times()
    date()
    speak('sha in your service, how can i help you ?')

#greet()

#lesson 7 wish me
def wishme():
    speak('welcome back sir!')
    # times()
    # date()
    hour=datetime.datetime.now().hour

    if hour >=6 and hour<12:
        speak('good morning')
    elif hour >= 12 and hour< 18:
        speak("good afternoon")
    elif hour >=18 and hour <24:
        speak("good evening")
    else:
        speak("good night")
#wishme()

#lesson 8 take command Function
#need internet connection must
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: #use microphone for capture voice 
        print("listening....")
        r.pause_threshold = 1 
        audio = r.listen(source)
    
    try:
        print("Recognizing'...")
        query = r.recognize_google(audio,'en-us') #by google voice change into text
        print(query)
    except Exception as e:  #if the try section not work then show this error
        print(e)
        speak("say that again please...")

        return "None"
    return query

#takecommand()

def sendmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587) #port no 587
    server.ehlo() 
    server.starttls() #pre define function
    server.login("example@gmail.com","123@123admin")
    server.sendmail("client@gmail.com",to,content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("ss.png")

def cpu():
    usage = str(psutil.cpu_times_percent())
    speak("cpu is at "+ usage)

    battery= psutil.sensors_battery
    speak("battery at ")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

#lession 9 Main function create while loop and add all function

if __name__ == "__main__":
    
    wishme()

    while True:
        query = takecommand().lower()
        print(query)

        if "time" in query:
            times()

        elif "date" in query:
            date()
        elif "offline" in query :
            quit()
        
        #lession 10 Wikipedia Search
        elif "wikipedia" in query:
            speak("Searching.......")
            query = query.replace("wikipedia","")
            result= wikipedia.summary(query,sentences = 2)
            speak(result)
        #lession 11 send mail
        elif "send email" in query:
            try:
                speak("what should I say")
                content = takecommand()
                to = "xyz@gmail.comm"
                sendemail(to, content)
                speak(content)

            except Exception as e:
                speak(e)
                speak("Unable to send email")
        elif "search in chrome" in query:
            speak("what you search")
            chromepath="find you chrome path and paste here"
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search +".com")

        elif "logout" in query:
            os.system("shutdown - l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart"in query:
            os.system("shutdown /r /t 1")

        #lession 14  play song
        elif "play songs" in query:
            song_dir= "path of music player"
            songs   = os.listdir(song_dir)
            os.startfile(os.path.join(song_dir,songs[0]))

        #lession 15 remember function
        elif "remember" in query:
            speak("waht should i remember .")
            data     = takecommand() 
            speak("you said me to rembember"+ data)
            remember = open('data.txt',"w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember = open("data.txt","r")
            speak(      "you said me to remember that"+ remember.read())
            remember.close()

        # lession 16 screenshot
        elif "screenshot" in query:
            screenshot()
            speak("screenshot capture")

        #lession 17 CPU &battery update

        elif "cpu" in query:
            cpu()

        #lession 18 jokes
        elif "joke"in query:
            jokes()
