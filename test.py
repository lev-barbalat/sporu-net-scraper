import csv
import codecs
PATH_TO_JOKES_FILE = r"C:\PythonExperiments"
PATH_TO_LOG_FILE = r"C:\PythonExperiments"
JOKES_FILE = r"\Jokes"
JOKES_FILE_EXTENSION = ".txt"
JOKES_FILE_EXTENSION_CSV = ".csv"
last_delimeter=r"Aнoнимнo"
JOKES_FILE_EXTENSION_XLSX = ".xlsx"

path = PATH_TO_JOKES_FILE + JOKES_FILE + JOKES_FILE_EXTENSION_XLSX


import xlrd

workbook = xlrd.open_workbook(path, on_demand = True)
worksheet = workbook.sheet_by_index(0)
first_row = [] # The row where we stock the name of the column
for col in range(worksheet.ncols):
    first_row.append( worksheet.cell_value(0,col) )
# transform the workbook to a list of dictionaries
data =[]
for row in range(1, worksheet.nrows):
    elm = {}
    for col in range(worksheet.ncols):
        elm[first_row[col]]=worksheet.cell_value(row,col)
    data.append(elm)
print (data)
