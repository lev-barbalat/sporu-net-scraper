class JokeAnalyser:
    textOfJoke=""

    def __init__(self,text):
        self.textOfJoke=text

    def lenght_of_joke(self):
        return len(self.textOfJoke)

    def number_of_words(self):
        return len(self.textOfJoke.split())

