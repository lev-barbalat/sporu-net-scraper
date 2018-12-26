from sporuNetScraper import *
from jokeAnalyser import *
from datetime import timedelta, date
import csv
import xlsxwriter


DATE_FORMAT = "%Y/%m/%d %H:%M:%S"
SHORT_DATE_FORMAT = "%Y/%m/%d"

PATH_TO_JOKES_FILE = r"C:\PythonExperiments"
PATH_TO_LOG_FILE = r"C:\PythonExperiments"
JOKES_FILE = r"\Jokes"
JOKES_FILE_EXTENSION = ".txt"
JOKES_FILE_EXTENSION_CSV = ".csv"
JOKES_FILE_EXTENSION_XLSX = ".xlsx"

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

            temp_jokes=current_jokes.getJokes()
            for joke in temp_jokes:
                counter += 1
                date_to_write=single_date.strftime(SHORT_DATE_FORMAT)
                self.jokes.append((counter,joke,date_to_write))
#            self.jokes = self.jokes + current_jokes.getJokes()
            print("Importing jokes for {0}".format(single_date.strftime("%Y-%m-%d")))

    def write_to_file(self):
        try:
            path = PATH_TO_JOKES_FILE + JOKES_FILE + self.date_suffix_file_element + JOKES_FILE_EXTENSION
            print(path)
            a = "-" * 100 + "\r\n"
            with open(path, "w", encoding="utf-8") as open_file:
                for joke in self.jokes:
                    open_file.write(a)
                    open_file.write(str(joke[0]))
                    open_file.writelines("\r\n")
                    open_file.write(joke[1])
                    open_file.writelines("\r\n")
                    open_file.write(joke[2])
                    open_file.writelines("\r\n")

            print("{0} jokes were written sucessfully to {1}".format(len(self.jokes), path))
        except Exception as e:
            print("Exception occured: {0}".format(e))


    def write_to_csv_file(self):
        try:
            path = PATH_TO_JOKES_FILE + JOKES_FILE + self.date_suffix_file_element + JOKES_FILE_EXTENSION_CSV
#            print(path)
#            a = "-" * 100 + "\r\n"
            with open(path, 'w',encoding="utf-8") as open_file:
                jokes_writer = csv.writer(open_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, dialect="excel")
                for joke in self.jokes:
                    print (joke)
                    print(str(joke[1]).encode("utf-8").decode("utf-8"))
                    jokes_writer.writerow([joke[0],str(joke[1]).encode("utf-8").decode("utf-8") ,joke[2]])
            print("{0} jokes were written sucessfully to {1}".format(len(self.jokes), path))
        except Exception as e:
            print("Exception occured: {0}".format(e))

    def write_to_file_excel(self):
        try:
            path = PATH_TO_JOKES_FILE + JOKES_FILE + self.date_suffix_file_element + JOKES_FILE_EXTENSION_XLSX
            #            print(path)
            #            a = "-" * 100 + "\r\n"

            workbook = xlsxwriter.Workbook(path)
            worksheet = workbook.add_worksheet()

            # Widen the first column to make the text clearer.
            worksheet.set_column('A:A', 20)

            # Add a bold format to use to highlight cells.
            bold = workbook.add_format({'bold': True})

            # Write some simple text.
            counter=0
            for joke in self.jokes:
                print(joke)
                counter+=1
                location = "".join(["A", str(counter)])
                worksheet.write(location, joke[1])

            workbook.close()
            print("{0} jokes were written sucessfully to {1}".format(len(self.jokes), path))
        except Exception as e:
            print("Exception occured: {0}".format(e))


exporter= JokeFileExporter()
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=7)
exporter.extract_jokes(start_date,end_date)
#exporter.write_to_file()
#exporter.write_to_csv_file()
exporter.write_to_file_excel()


