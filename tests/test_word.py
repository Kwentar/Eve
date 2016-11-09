import unittest
from model.word import Word


class TestWord(unittest.TestCase):
    def test_normal_form(self):
        w = Word("Делали")
        self.assertEqual(w.normal_form, "делать", "нормальная форма")
        w = Word("СТЕНОЙ")
        self.assertEqual(w.normal_form, "стена", "нормальная форма")
        w = Word("странный")
        self.assertEqual(w.normal_form, "странный", "нормальная форма")


