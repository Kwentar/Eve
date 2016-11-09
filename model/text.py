from model.paragraph import Paragraph


class Text:
    def __init__(self, text: str):
        self.text = text
        self.paragraphs = [Paragraph(x) for x in text.split('\n')]
