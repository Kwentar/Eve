from model.sentence import Sentence


class Paragraph:
    def __init__(self, paragraph: str):
        self.paragraph = paragraph
        self.sentences = self.split()

    def split(self):
        sentences = []
        curr_sentence = ''
        for index, sym in enumerate(self.paragraph):
            curr_sentence += sym
            if sym in '.?!' and index and \
                    self.paragraph[index-1].isupper() or self.paragraph[index-1].isdigit():
                sentences.append(curr_sentence.lstrip())
                curr_sentence = ''
        first_iter = self.paragraph.replace('!', '.').replace('?', '.')
        return [Sentence(x) for x in first_iter.split('.') if x]
