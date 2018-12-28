CLASSIFICATION_RULES = [
    ("Одесса", 'Одесса'),
    ("Одесса", 'Одессит'),
    ("Одесса", 'одесит'),
    ("Одесса", 'Одесситка'),
    ("Одесса", 'Дерибасовская'),
    ("Одесса", 'Дюк'),
    ("Одесса", 'Привоз'),
    ("Компьютер", 'Компьютер'),
    ("Компьютер", 'компьютер'),
    ("Программист", 'Программист'),
    ("Программист", 'программист'),
    ("Программист", 'програмимирование'),
    ("Программист", 'компилятор'),
    ("Евреи", 'Еврей'),
    ("Евреи", 'раввин'),
    ("Дети", 'ребенок'),
    ("Дети", 'дети'),

    ("Евреи", 'Рабинович'),
    ("Политика", 'Медведев'),
    ("Политика", 'Путин'),
    ("Политика", 'Путина'),
    ("Политика", 'Медеведева'),
    ("Политика", 'Путину'),
    ("Политика", 'Медеведеву')
]

JOKE = "Одесса. Еврейского мальчика лет шести приводят в школу на собеседование"
JOKE2 = " в школу на собеседование"

class JokeAnalyser:
    textOfJoke=""
    classifications=set()

    def __init__(self,text):
        self.textOfJoke=text
        self.classifications.clear()

    def lenght_of_joke(self):
        return len(self.textOfJoke)

    def number_of_words(self):
        return len(self.textOfJoke.split())

    def classify_joke(self):
        for rule in CLASSIFICATION_RULES:
            if (rule[1] in self.textOfJoke):
                self.classifications.add(rule[0])
                #print("joke: {0} rule: {1}".format(rule[1], self.textOfJoke))

    def get_classification(self):
        if len(self.classifications)>0:
            return ", ".join(self.classifications)
        else:
            return ""


"""
joke_analyser=JokeAnalyser(JOKE)
joke_analyser.classify_joke()
print(joke_analyser.get_classification())
joke_analyser2=JokeAnalyser(JOKE2)
joke_analyser2.classify_joke()
print(joke_analyser2.get_classification())
"""