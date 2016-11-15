from unittest import TestCase
from model.sentence import Sentence
from model.word import Word


class TestSentence(TestCase):
    def test_split(self):
        text = "Каждый раз, когда я вижу тебя, я понимаю - не все потеряно"
        s = Sentence(text)
        self.assertListEqual([w.text_form for w in s.words],
                             [Word(x).text_form for x in ["Каждый", "раз", "когда", "я", "вижу", "тебя",
                                                "я", "понимаю", "не", "все", "потеряно"]])
