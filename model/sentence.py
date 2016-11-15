from model.word import Word


class Sentence:
    def __init__(self, sentence: str):
        self.sentence = sentence
        self.words = self.split()

    def split(self):
        # TODO: 15.9% - > 159 и добавить знаки препинания
        first_iter = self.sentence.split()
        second_iter = []
        for el in first_iter:
            without_bad = [c for c in el if c.lower().isalnum()]
            if without_bad:
                second_iter.append("".join(without_bad))
        return [Word(x) for x in second_iter]

    def __add__(self, other):
        self.sentence += ' ' + other.sentence
        self.words = self.split()

    def __repr__(self):
        return "sentence \"{}\" with words {} ".format(self.sentence, self.words)
