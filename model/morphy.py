import pymorphy2


class Morphy:
    instance = None
    morphy = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super(Morphy, cls).__new__(cls)
            cls.morphy = pymorphy2.MorphAnalyzer()
        return cls.instance

    @classmethod
    def parse(cls, word):
        return cls.morphy.parse(word)
