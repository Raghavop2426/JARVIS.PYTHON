import speech_recognition as sr
import webbrowser as wr
import pyttsx3
import musiclibrary
import requests

recognizer = sr.Recognizer() # used to recognize the text

ttsx = pyttsx3.init()
newsapi = "pub_d5bc9a2bc7474822842ba27ac3594878"
def speak(word):              # for speaking the text we give 
    ttsx.say(word)
    ttsx.runAndWait()
 
def processcmd(c):
    if "open google" in c.lower():
        wr.open("https://www.google.com")
    elif "open facebook" in c.lower():
        wr.open("https://www.facebook.com")
    elif "open linkdin" in c.lower():
        wr.open("https://www.linkdin.com")
    elif "open youtube" in c.lower():
        wr.open("https://www.youtube.com")
    elif "open chatgpt" in c.lower():
        wr.open("https://www.chatgpt.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        wr.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # speak the headlines
            for article in articles:
                speak(article['title'])
if __name__ == "__main__":

    speak("Activating jarvis.....")
    while True:
         r = sr.Recognizer()

         print("recognizing...")
         
         try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)

            if(word.lower() == "raghav"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcmd(command)


         except Exception as e:
            print("Error; {0}".format(e))
