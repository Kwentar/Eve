from model.sentence import Sentence
from model.word import Word


class Paragraph:
    def __init__(self, paragraph: str):
        self.paragraph = paragraph
        self.sentences = self.split()
        self.post_process_sentences()

    def split(self):
        # TODO: с инициалами фича следующая: если мы видим большую букву с точкой - то фамилия либо слева и справа -
        # конец предложения (справа начало предложения с большой буквы). Если слева нет - то фамилия справа
        # TODO: добавить всякие т.д. т.п.
        sentences = []
        curr_sentence = ''
        for index, sym in enumerate(self.paragraph):
            curr_sentence += sym
            is_new = False
            if sym in '?!':
                is_new = True
            elif sym == '.':
                is_new = True
                if index < len(self.paragraph) - 1 and self.paragraph[index + 1].isdigit():
                    is_new = False
            if index == len(self.paragraph) - 1:
                is_new = True
            if is_new:
                sentences.append(Sentence(curr_sentence.lstrip()))
                curr_sentence = ''
        return sentences

    def post_process_sentences(self):

        last_word = None
        index = 0
        while index < len(self.sentences) - 1:
            if last_word:
                first_word = self.sentences[index].words[0]
                if first_word.text_form.isupper() and len(first_word.text_form) == 1 and \
                        last_word.text_form.isupper() and len(last_word.text_form) == 1:
                    self.sentences[index-1] += self.sentences[index]
                    self.sentences.remove(self.sentences[index])
                    index -= 1
            index += 1
            last_word = self.sentences[index].words[-1]
