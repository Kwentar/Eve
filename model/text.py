from model.paragraph import Paragraph


class Text:
    def __init__(self, text: str):
        self.text = text
        self.paragraphs = self.split()

    def split(self):
        first_iter = self.text.replace('\r', '\n')
        return [Paragraph(x) for x in first_iter.split('\n') if x]
