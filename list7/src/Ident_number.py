from Controlled_text import Controlled_text


DEFAULT_NUMBER_TO_MODULO = 97


class Ident_number(Controlled_text):
    def __init__(self, ident_number):
        self.__check_ident_number(ident_number)
        self._text = self.__transform_new_ident_number(ident_number)

    @property
    def id_number(self):
        return self._text

    @id_number.getter
    def id_number(self):
        return self._text

    def __check_ident_number(self, new_ident_number):
        if len(new_ident_number) != 7 or not new_ident_number.isnumeric():
            raise ValueError("Invalid Ident Number provided!")

    def __transform_new_ident_number(self, new_ident_number):
        number = int(new_ident_number)
        rest = number % DEFAULT_NUMBER_TO_MODULO

        if rest < 10:
            rest = "0" + str(rest)

        return new_ident_number + str(rest)
