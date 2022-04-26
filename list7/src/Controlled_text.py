class Controlled_text:
    def __init__(self, text):
        self._text = text

    @property
    def text(self):
        return self._text

    @text.getter
    def text(self):
        return self._text

    @text.setter
    def text(self, new_text):
        if not new_text.isprintable() or " " in new_text:
            raise ValueError("Invalid argument provided!")
        else:
            self._text = new_text

    def __str__(self):
        return self._text

    def __lt__(self, other):
        return self._text < other._text

    def __gt__(self, other):
        return not self < other

    def __eq__(self, other):
        return self.text == other.text

    def __len__(self):
        return len(self._text)
