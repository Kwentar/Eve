from unittest import TestCase
from model.paragraph import Paragraph


class TestParagraph(TestCase):
    def test_split(self):
        p = Paragraph('Как твои дела? Что нового? У меня все хорошо. Я купил пирожков, вотрушек и т.д.,все получилось.')
        self.assertListEqual([x.sentence for x in p.sentences], ['Как твои дела?', 'Что нового?', 'У меня все хорошо.',
                                                                 'Я купил пирожков, вотрушек и т.д.,все получилось.'])
        p = Paragraph('В. А.  Уткин увеличил прибыль на 15.9%. Дал 5.Ударил Иванова А. Б.')
        self.assertListEqual([x.sentence for x in p.sentences], ['В. А. Уткин увеличил прибыль на 15.9%.',
                                                                 'Дал 5.', 'Ударил Иванова А. Б.'])
        p = Paragraph('В. Уткин заметил Кривого А.Н. рядом с Сильным М.')
        self.assertListEqual([x.sentence for x in p.sentences], ['В. Уткин заметил Кривого А.Н. рядом с Сильным М.'])

    def test_get_word_size(self):
        p = Paragraph('В. А. Уткин увеличил прибыль на 15.9%. Дал 5. Ударил Иванова А.Б. Здравствуйте.')
        one = p.get_word_size(0)
        five = p.get_word_size(6)
        twelve = p.get_word_size(66)
        one_again = p.get_word_size(63)

        self.assertEqual(1, one)
        self.assertEqual(5, five)
        self.assertEqual(12, twelve)
        self.assertEqual(1, one_again)

    def test_has_family_left(self):
        p = Paragraph('В. А. Уткин увеличил прибыль на 15.9%. Дал 5. Ударил Иванова А.Б. Здравствуйте.')
        self.assertEqual(p.has_family_left(63), True)
        self.assertEqual(p.has_family_left(61), True)
        self.assertEqual(p.has_family_left(0), False)
        self.assertEqual(p.has_family_left(3), False)

    def test_is_abbr(self):
        p = Paragraph('В. А. Уткин увеличил прибыль на 15.9%. Дал 5. Ударил Иванова А.Б. Здравствуйте.')
        self.assertEqual(p.is_initial(1), True)
        self.assertEqual(p.is_initial(4), True)
        self.assertEqual(p.is_initial(64), True)
        self.assertEqual(p.is_initial(62), True)
        self.assertEqual(p.is_initial(34), False)
        self.assertEqual(p.is_initial(77), False)


