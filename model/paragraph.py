from model.sentence import Sentence


class Paragraph:
    def __init__(self, paragraph: str):
        self.paragraph = paragraph
        self.sentences = self.split()

    def split(self):
        return [Sentence(x) for x in self.paragraph.split('.')]
