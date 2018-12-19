class jokeAnalyser:
    textOfJoke=""

    def __init__(self,text):
        self.textOfJoke=text

    def lenOfJokes(self):
        return len(self.textOfJoke)

    def numberOfWords(self):
        return len(self.textOfJoke.split())

