
from http import client
from mimetypes import init
from unicodedata import category, name
import pyttsx3
import requests, json
from newsapi import NewsApiClient



newsapi = NewsApiClient(api_key='7f1e9ee566ae490da0e36450fcbf08e8')
headlines = newsapi.get_top_headlines ( category='health',q='brain',country='in')
pynews = json.dumps(headlines)




engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak(pynews)
    
