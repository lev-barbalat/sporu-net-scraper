from joke_importer_to_file import *
import xlsxwriter
import xlrd
from classification_rules import *
import timeit

PATH_TO_JOKES_FILE = r"C:\PythonExperiments"
PATH_TO_LOG_FILE = r"C:\PythonExperiments"
JOKES_FILE = r"\Jokes"
ANALYSED_JOKES_FILE = r"\AnalyzedJokes"
JOKES_FILE_EXTENSION = ".txt"
JOKES_FILE_EXTENSION_CSV = ".csv"
last_delimeter=r"Aнoнимнo"
JOKES_FILE_EXTENSION_XLSX = ".xlsx"

class JokesHandler():
    jokes=[]
    analysed_jokes=[]
    path=""
    analysed_path=""
    classification_rules=[]

    def __init__(self, rules):
        self.classification_rules=rules

    def set_path_origin(self, path_to_jokes_file):
        self.path = path_to_jokes_file

    def set_path_analysed(self, path_to_analysed_file):
        self.analysed_path=path_to_analysed_file

    def load_jokes_from_excel(self):
        workbook = xlrd.open_workbook(self.path, on_demand=True)
        worksheet = workbook.sheet_by_index(0)
        first_row = []  # The row where we stock the name of the column
        data = []
        counter=0
        for row in range(0, worksheet.nrows):
            self.jokes.append((worksheet.cell_value(row, 0), worksheet.cell_value(row, 1), (worksheet.cell_value(row, 2))))

    def analyse_jokes(self):
        for joke in self.jokes:
            current_joke=JokeAnalyser(joke[1],self.classification_rules)
            current_joke.classify_joke()
            self.analysed_jokes.append((joke[0], joke[1], joke[2], current_joke.lenght_of_joke(), current_joke.number_of_words(),current_joke.get_classification()))



    def write_analysed_to_excel(self):
        try:
            workbook = xlsxwriter.Workbook(self.analysed_path)
            worksheet = workbook.add_worksheet()

            # Widen the columns to make the text clearer.
            worksheet.set_column('A:A', 10)
            worksheet.set_column('B:B', 100)
            worksheet.set_column('C:C', 20)

            # Captions
            worksheet.write("A1", "ID")
            worksheet.write("B1", "Joke")
            worksheet.write("C1", "Date of Joke")
            worksheet.write("D1", "Lenght of joke")
            worksheet.write("E1", "Number of words")
            worksheet.write("F1", "Categories")

            counter = 1
            for joke in self.analysed_jokes:
                counter += 1
                location = "".join(["A", str(counter)])
                worksheet.write(location, str(joke[0]))
                location = "".join(["B", str(counter)])
                worksheet.write(location, joke[1])
                location = "".join(["C", str(counter)])
                worksheet.write(location, joke[2])
                location = "".join(["D", str(counter)])
                worksheet.write(location, joke[3])
                location = "".join(["E", str(counter)])
                worksheet.write(location, joke[4])
                location = "".join(["F", str(counter)])
                categories=", ".join(joke[5])
                worksheet.write(location, str(joke[5]))

            workbook.close()
            print("{0} analysed jokes were written sucessfully to Excel file: {1}".format(len(self.jokes), self.analysed_path))
        except Exception as e:
            print("Exception occured: {0}".format(e))




path = PATH_TO_JOKES_FILE + JOKES_FILE + JOKES_FILE_EXTENSION_XLSX
analysed_path = PATH_TO_JOKES_FILE + ANALYSED_JOKES_FILE + JOKES_FILE_EXTENSION_XLSX
startOfProcess  = datetime.datetime.now()

#Load rules
rules_manager = ClassificationRules()
rules=rules_manager.get_rules()

#Activate handler
handler=JokesHandler(rules)
handler.set_path_origin(path)
handler.set_path_analysed(analysed_path)
handler.load_jokes_from_excel()
handler.analyse_jokes()
handler.write_analysed_to_excel()
elapsed_time=(datetime.datetime.now()-startOfProcess).microseconds/1000
print("Elapsed time: {0} mili seconds".format(elapsed_time))


