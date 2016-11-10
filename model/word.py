from model.morphy import Morphy


class Word:

    def __init__(self, text_form: str):
        self.morphy = Morphy()
        self.parse_res = self.morphy.parse(text_form)
        self.normal_form = self.parse_res[0].normal_form
        self.text_form = text_form
        self.tag = self.parse_res[0].tag

    def __repr__(self):
        return self.text_form
