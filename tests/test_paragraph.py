from unittest import TestCase
from model.paragraph import Paragraph


class TestParagraph(TestCase):
    def test_split(self):
        p = Paragraph('Как твои дела? Что нового? У меня все хорошо.')
        self.assertListEqual([x.sentence for x in p.sentences], ['Как твои дела?', 'Что нового?', 'У меня все хорошо.'])
        p = Paragraph('В. А. Уткин увеличил прибыль на 15.9%. Дал 5. Ударил Иванова А. Б.')
        self.assertListEqual([x.sentence for x in p.sentences], ['В. А. Уткин увеличил прибыль на 15.9%.',
                                                                 'Дал 5.', 'Ударил Иванова А. Б.'])
        p = Paragraph('В. Уткин заметил Кривого А.Н. рядом с Сильным М.')
        self.assertListEqual([x.sentence for x in p.sentences], ['В. Уткин заметил Кривого А.Н. рядом с Сильным М.'])

