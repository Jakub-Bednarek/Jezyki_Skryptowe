from Controlled_text import Controlled_text


class Last_name(Controlled_text):
    def __init__(self, last_name):
        self.lname = last_name

    @property
    def lname(self):
        return self._text

    @lname.getter
    def lname(self):
        return self._text

    @lname.setter
    def lname(self, new_lname):
        self.__check_last_name(new_lname)
        self._text = new_lname

    def __check_last_name(self, last_name):
        if not last_name.istitle():
            raise ValueError("Invalid argument for last name!")
