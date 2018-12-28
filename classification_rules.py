import xlrd

CLASSIFICATION_RULES= r"C:\PythonExperiments\ClassificationRules.xlsx"

class ClassificationRules:
    rules=[]
    path=""
    def __init__(self):
        self.path = CLASSIFICATION_RULES
        self.load_rules_from_excel()

    def load_rules_from_excel(self):

        workbook = xlrd.open_workbook(self.path, on_demand=True)
        worksheet = workbook.sheet_by_index(0)
        counter = 0
        for row in range(0, worksheet.nrows):
            rule = (worksheet.cell_value(row, 0), worksheet.cell_value(row, 1))
            self.rules.append(rule)

        workbook.release_resources()

    def get_rules(self):
        return self.rules


"""
rulesManager=ClassificationRules()
print(rulesManager.get_rules())
"""