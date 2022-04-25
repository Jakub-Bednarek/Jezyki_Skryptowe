from Controlled_text import Controlled_text

DEFAULT_NAMES_FILE_NAME = "PopularneImiona.txt"


def load_names(file_name):
    with open(file_name) as file:
        names = set([name.lower() for name in file.read().splitlines()])

    return names


class First_name(Controlled_text):
    def __init__(self, first_name):
        self.__names = load_names(DEFAULT_NAMES_FILE_NAME)
        self.name = first_name

    @property
    def name(self):
        return self._text

    @name.getter
    def name(self):
        return self._text

    @name.setter
    def name(self, new_name):
        self.__check_name(new_name.lower())
        self.text = new_name.title()

    def __check_name(self, new_name):
        if new_name not in self.__names:
            raise ValueError("Name doesn't exist in database")
        else:
            return True

    @staticmethod
    def female_name(name_to_check):
        return name_to_check.endswith("a")

    @staticmethod
    def male_name(name_to_check):
        return not First_name.female_name(name_to_check)

    def is_female(self):
        return self.female_name(self._text)

    def is_male(self):
        return not self.is_female()
