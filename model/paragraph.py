from model.sentence import Sentence


class Paragraph:
    def __init__(self, paragraph: str):
        self.paragraph = ' '.join(paragraph.split())
        self.sentences = self.split()

    def split(self):
        """
        Split the paragraph into sentences
        :return: list of sentences
        """
        sentences = []
        curr_sentence = ''
        for index, sym in enumerate(self.paragraph):
            curr_sentence += sym
            is_new = False
            if sym in '?!':
                is_new = True
            elif sym == '.':
                if index + 1 < len(self.paragraph) and self.paragraph[index+1].isdigit() and \
                                        index - 1 > 0 and self.paragraph[index - 1].isdigit():  # 5.5
                    continue
                if self.next_sym_is_upper_or_digit(index):
                    if self.has_family_left(index) and not self.has_initial_right(index) or not self.is_initial(index):
                        is_new = True  # Иванов А.В_._ Позже выяснилось, ...

            if index == len(self.paragraph) - 1:
                is_new = True
            if is_new:
                sentences.append(Sentence(curr_sentence.lstrip()))
                curr_sentence = ''
        return sentences

    def is_initial(self, index):
        """
        :param index: index of !dot!
        :return: True if self.paragraph[index-1] is initial
        """
        s = self.paragraph

        if index - 1 >= 0 and s[index - 1].isupper() and (index >= 2 and s[index - 2] in ' .' or index < 2):
            return True
        return False

    def has_family_left(self, index):
        """
        :param index: index of initial
        :return: True if this initial has family from left
        """
        count_upper = 0
        while index > 0:
            if self.paragraph[index].isupper():
                count_upper += 1
                word_size = self.get_word_size(index)
                if word_size > 1:
                    return True
                if count_upper > 2:
                    return False
            index -= 1
        return False

    def get_word_size(self, index):
        """
        :param index: index of upper letter
        :return: size of word
        """
        word_size = 1
        left = index - 1
        right = index + 1
        while self.paragraph[left].isalnum():
            left -= 1
            word_size += 1
        while self.paragraph[right].isalnum():
            right += 1
            word_size += 1
        return word_size

    def next_sym_is_upper_or_digit(self, index):
        """
        :param index: index of dot
        :return: true if next significant symbol is upper or digit otherwise false
        """
        index += 1
        while index < len(self.paragraph):
            if self.paragraph[index].isalnum():
                if self.paragraph[index].isupper() or self.paragraph[index].isdigit():
                    return True
                else:
                    return False
            index += 1
        return True

    def has_initial_right(self, index):
        """
        :param index: index of dot
        :return: true if has initial from right otherwise false
        """
        if index + 3 < len(self.paragraph) and self.paragraph[index + 1] == ' ' \
                and self.paragraph[index + 2].isupper() and self.paragraph[index + 3] == '.' or \
                index + 2 < len(self.paragraph) and self.paragraph[index + 1].isupper() \
                and self.paragraph[index + 2] == '.':
            return True
        return False
