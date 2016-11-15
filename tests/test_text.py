import unittest
from model.text import Text


class TestText(unittest.TestCase):
    def test_split(self):
        text = '''Белеет парус одинокий
В тумане неба голубом.
Что ищет он в стране далекой?
Что кинул он в стране родной?'''
        t = Text(text)
        self.assertListEqual([x.paragraph for x in t.paragraphs],
                             ['Белеет парус одинокий', 'В тумане неба голубом.',
                              'Что ищет он в стране далекой?', 'Что кинул он в стране родной?'])
        text = '''Здравствуй!
Как твои дела? Что нового? У меня все хорошо.
Пишу тебе, потому что мне нужен этот тест.'''
        t = Text(text)
        self.assertListEqual([x.paragraph for x in t.paragraphs],
                             ['Здравствуй!', 'Как твои дела? Что нового? У меня все хорошо.',
                              'Пишу тебе, потому что мне нужен этот тест.'])
