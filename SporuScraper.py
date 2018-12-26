import requests
from bs4 import BeautifulSoup
from ScraperExceptions import *
import re
end_of_joke_delimeter="Aнoнимнo"
import datetime
from sporuNetScraper import *


def extrackSporuNetJoke(text):
    joke_with_ending = text[4:]
    substrStart=joke_with_ending.find(END_OF_JOKE_DELIMITER)
    joke_without_ending=joke_with_ending
    joke_without_ending=joke_with_ending[:substrStart]
    return str(joke_without_ending).strip()

reason_code=""
url="http://sporu.net/1218/120718.htm"
urlelements=[r"http://sporu.net/",datetime.datetime.now().strftime("%m%y/%m%d%y"),".htm"]

todayUrl="".join(urlelements)

try:
    html= requests.get(todayUrl)
    if html.status_code!=200:
        reason_code="Bad response from the server"
        raise InvalidResponse

    soup = BeautifulSoup(html.text,"html.parser")
    tableID=0
    for div in soup.find_all("div",{"class":"item"}):
        print("-"*100)
        childID=0
        for child in div:

           childID += 1
           if childID==3:
                joke=extrackSporuNetJoke(child.text)
                print(joke)
        tableID+=1

except InvalidResponse:
    print("Proper response from the server was not received")
except  Exception as e:
    print("Something did not worked")
    print("Details of exceptions: {0}".format(e))


