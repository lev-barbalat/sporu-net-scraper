import requests
from bs4 import BeautifulSoup
from ScraperExceptions import *
import re
import datetime

#string constants
end_of_joke_delimeter=r"Анонимно"
last_delimeter=r"Aнoнимнo"
beginningOfUrl = r"http://sporu.net/"
suffixOfUrl=".htm"
pathOfLocalFile=r"C:\PythonExperiments"

class SporuNetScraper:
    urlToScrape=""
    jokes=[]
    dateSuffixUrlElement=""    #date of url of sporu.net
    dateSuffixFileElement=""   #date of the file in filesystem
    dateOfJokes=datetime.datetime.now()
    def __init__(self):
        self.dateOfJokes=datetime.datetime.now()
        self.updateDateElements()
        urlelements = [beginningOfUrl,self.dateSuffixUrlElement ,suffixOfUrl ]
        self.urlToScrape = "".join(urlelements)

    def updateDateElements(self):
        self.dateSuffixUrlElement=self.dateOfJokes.strftime("%m%y/%m%d%y")
        self.dateSuffixFileElement=self.dateOfJokes.strftime("%Y%m%d")
        urlelements = [beginningOfUrl, self.dateSuffixUrlElement, suffixOfUrl]
        self.urlToScrape = "".join(urlelements)

    def defineDate(self,year,month,day):

        self.dateOfJokes=datetime.datetime(year,month,day)
        self.updateDateElements()

    def defineDateByDate(self,date):
        self.dateOfJokes=date
        self.updateDateElements()

    def scrapJokes(self):
        try:
            self.jokes=[]
            html = requests.get(self.urlToScrape)
            if html.status_code != 200:
                reason_code = "Bad response from the server"
                raise InvalidResponse

            soup = BeautifulSoup(html.text, "html.parser")
            tableID = 0
            #extract jokes
            for div in soup.find_all("div", {"class": "item"}):
                childID = 0
                for child in div:
                    childID += 1
                    if childID == 3:
                        joke=str(child.text)[4:(str(child.text)).find(end_of_joke_delimeter)].strip()
                        self.jokes.append(joke)
                tableID += 1

                #handling the last joke that has different separator
                lastIndex=len(self.jokes)-1
                self.jokes[lastIndex]=str(self.jokes[lastIndex])[:str(self.jokes[lastIndex]).find(last_delimeter)].strip()

        except InvalidResponse:
            print("Proper response from the server was not received")
        except  Exception as e:
            print("Something did not worked")
            print("Details of exceptions: {0}".format(e))



    def printJokes(self):
        for joke in self.jokes:
            print("-" * 100)
            print(joke)

    def serialise(self):
        try:

            path=pathOfLocalFile+r"\Jokes"+self.dateSuffixFileElement+".txt"
            a="-"*100+"\r\n"
            with open(path,"w",encoding="utf-8")  as open_file:
                for joke in self.jokes:
                    open_file.write(a)
                    open_file.write(joke)
                    open_file.writelines("\r\n")

            print("{0} jokes were written sucessfully to {1}".format(len(self.jokes),path))
        except Exception as e:
            print("Exception occured: {0}".format(e))

    def getJokes(self):
        return self.jokes