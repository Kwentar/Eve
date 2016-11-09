from model.word import Word


class Sentence:
    def __init__(self, sentence: str):
        self.sentence = sentence
        self.words = self.split()

    def split(self):
        return [Word(x) for x in self.sentence.split()]
