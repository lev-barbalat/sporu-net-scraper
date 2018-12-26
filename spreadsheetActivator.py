from sporuNetScraper import *
from jokeAnalyser import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import timedelta, date
dateFormat="%Y/%m/%d %H:%M:%S"

class googleSheetExporter:
    client = None
    sheetJokes=None
    sheetLog=None
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
        creds=ServiceAccountCredentials.from_json_keyfile_name("client_secret.json",scope)
        self.client = gspread.authorize(creds)
        print("Connection initialised")
        self.sheetJokes = self.client.open("Jokes").sheet1
        self.sheetLog=self.client.open("Jokes").worksheet("Log")


    def writeJokesForDate(self,dateOfJokes):
        todaysJokes=SporuNetScraper()
        todaysJokes.defineDateByDate(dateOfJokes)
        todaysJokes.scrapJokes()
        jokes=todaysJokes.getJokes()

        i=self.getCounterForSheet(self.sheetJokes)+1
        for joke in jokes:
            self.sheetJokes.update_cell(i,1,i-1)
            self.sheetJokes.update_cell(i, 2, joke)
            currentJoke=JokeAnalyser(joke)
            self.sheetJokes.update_cell(i, 3, currentJoke.lenght_of_joke())
            self.sheetJokes.update_cell(i, 4, currentJoke.number_of_words())
            self.sheetJokes.update_cell(i, 5, dateOfJokes.strftime("%Y-%m-%d"))
            i+=1

        #self.addLogRecord(len(jokes))

    def getCounterForSheet(self,sheetName):
        counter=0
        while (len(sheetName.cell(1+counter,1).value)>0):
            counter+=1
        return counter

    def addLogRecord(self,NumberOfJokes):
        rowToWrite=self.getCounterForSheet(self.sheetLog)
        rowValue=[rowToWrite,datetime.datetime.now().strftime(dateFormat),NumberOfJokes]
        self.sheetLog.insert_row(rowValue,rowToWrite+1)


    @staticmethod
    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days)+1):
            yield start_date + timedelta(n)


    def getlastDateForJokes(self):
        lastRow=self.getCounterForSheet(self.sheetLog)
        return datetime.datetime.strptime(str(self.sheetLog.cell(lastRow,2).value),dateFormat)



    def fillHistoricalJokes(self):
        start_date = self.getlastDateForJokes()
        end_date = datetime.datetime.now()
        counter=0

        for single_date in self.daterange(start_date, end_date):
            self.writeJokesForDate(single_date)
            counter+=1
            print("Importing jokes for {0}".format(single_date.strftime("%Y-%m-%d")))

        self.addLogRecord(counter*10)

exporter=googleSheetExporter()
#exporter.writeJokesForDate(datetime.datetime.now())
exporter.fillHistoricalJokes()
print ("Process completed")


#print(exporter.getCounterForSheet(exporter.sheetLog))



#scraper=SporuNetScraper()
#scraper.scrapJokes()
#scraper.serialise()
#scraper.defineDate(2018,12,12)
#scraper.scrapJokes()
#scraper.serialise()
#localJokes=[]
#localJokes=scraper.getJokes()
#print(localJokes)


#        cell_list=self.sheetJokes.range("B1:B10")
#       i=0
#        for cell in cell_list:
#            cell.value=jokes[i]
#            i+=1

#        self.sheetJokes.update_cells(cell_list)


