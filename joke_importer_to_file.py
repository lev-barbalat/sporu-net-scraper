from sporuNetScraper import *
from jokeAnalyser import *
from datetime import timedelta, date

DATE_FORMAT = "%Y/%m/%d %H:%M:%S"

PATH_TO_JOKES_FILE = r"C:\PythonExperiments"
PATH_TO_LOG_FILE = r"C:\PythonExperiments"
JOKES_FILE = r"\Jokes"
JOKES_FILE_EXTENSION = ".txt"


class JokeFileExporter:
    jokes = []
    filename_for_extraction = None
    date_suffix_file_element = ""  # date of the file in filesystem
    date_of_extraction = datetime.datetime.now()

    def __init__(self):
        dateOfExtraction = datetime.datetime.now()
        self.date_suffix_file_element = self.date_of_extraction.strftime("%Y%m%d")

    @staticmethod
    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days)+1):
            yield start_date + timedelta(n)

    def extract_jokes(self, start_date, end_date):
        counter = 0
        for single_date in self.daterange(start_date, end_date):
            current_jokes = SporuNetScraper()
            current_jokes.defineDateByDate(single_date)
            current_jokes.scrapJokes()
            self.jokes = self.jokes + current_jokes.getJokes()
            print("Importing jokes for {0}".format(single_date.strftime("%Y-%m-%d")))

    def write_to_file(self):
        try:
            path = PATH_TO_JOKES_FILE + JOKES_FILE + self.date_suffix_file_element + JOKES_FILE_EXTENSION
            print(path)
            a = "-" * 100 + "\r\n"
            with open(path, "w", encoding="utf-8") as open_file:
                for joke in self.jokes:
                    open_file.write(a)
                    open_file.write(joke)
                    open_file.writelines("\r\n")

            print("{0} jokes were written sucessfully to {1}".format(len(self.jokes), path))
        except Exception as e:
            print("Exception occured: {0}".format(e))





exporter= JokeFileExporter()
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=7)
exporter.extract_jokes(start_date,end_date)
exporter.write_to_file()


