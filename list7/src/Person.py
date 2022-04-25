from First_name import First_name
from Last_name import Last_name
from Ident_number import Ident_number
import re


class Person:
    def __init__(
        self, first_name: First_name, last_name: Last_name, ident_number: Ident_number
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.ident_number = ident_number

    @staticmethod
    def fromString(person_string):
        person_data = re.split(" |;|/", person_string)
        if len(person_data) != 3:
            raise ValueError("Invalid data for person!")

        return Person(
            First_name(person_data[0]),
            Last_name(person_data[1]),
            Ident_number(person_data[2]),
        )

    def __str__(self):
        return (
            "["
            + str(self.first_name)
            + "; "
            + str(self.last_name)
            + "; "
            + str(self.ident_number)
            + "]"
        )

    def __eq__(self, other):
        return (
            self.first_name == other.first_name
            and self.last_name == other.last_name
            and self.ident_number == other.ident_number
        )
