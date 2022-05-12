from enum import Enum
from typing import List
import datetime
import calendar

from logger import log_info, log_warn, log_error

DEFAULT_COUNTRY = "Poland"
DEFAULT_CONTINENT = "Europe"


class Command(Enum):
    SET = 0
    SHOW = 1
    RESET = 2
    EXIT = 3
    FROM = 4
    TO = 5


class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


def parse_set_command(tokens):
    commands_sequence = []
    while len(tokens) > 0:
        if tokens[0] in set_to_command:
            if tokens[0] == "to":
                tokens, single_command = set_to_command[tokens[0]](tokens[1:], False)
            else:
                tokens, single_command = set_to_command[tokens[0]](tokens[1:])

            if single_command:
                commands_sequence.extend(single_command)
                log_info(f"Adding parsed_command: {single_command}")
        else:
            log_error(f"Invalid argument for set command: {tokens[0]}")
            tokens = tokens[1:]

    return commands_sequence


def get_show_command():
    return "show"


def get_reset_command():
    return "reset"


def get_exit_command():
    return "exit"


def check_if_ready_date(token):
    try:
        return datetime.datetime.strptime(token, "%d.%m.%Y")
    except:
        return None


def convert_date(output_day, output_month, begin):
    date_out = None
    try:
        date_out = datetime.datetime.strptime(
            f"{output_day}-{output_month}-2020", "%d-%m-%Y"
        )
    except:
        if begin:
            date_out = datetime.datetime.strptime(f"1-{output_month}-2020", "%d-%m-%Y")
        else:
            date_out = datetime.datetime.strptime(
                f"{calendar.monthrange(2020, output_month)[1]}-{output_month}-2020",
                "%d-%m-%Y",
            )

    return date_out


def parse_date(tokens, begin=True):
    if len(tokens) < 1:
        log_error("Invalid number of arguments in set date function!")
        return ([], None)

    tokens_to_skip = 1
    if begin:
        date_str = "date_begin"
    else:
        date_str = "date_end"

    date_out = check_if_ready_date(tokens[0])
    if date_out:
        return (tokens[1:], [(date_str, date_out)])

    output_month = "1"
    output_day = None
    for month in Month:
        if month.name.lower() == tokens[0]:
            output_month = month.value

    if len(tokens) > 1:
        try:
            output_day = int(tokens[1])
            tokens_to_skip = 2
        except:
            pass

    date_out = convert_date(output_day, output_month, begin)

    return (tokens[tokens_to_skip:], [(date_str, date_out)])


def parse_request_type(tokens):
    if len(tokens) < 1 or (tokens[0] != "cases" and tokens[0] != "deaths"):
        log_warn(f"Invalid argument for request type: {tokens}")
        return (tokens, ("type", "cases"))

    return (tokens[1:], [("type", tokens[0])])


def parse_total_setting(tokens):
    if len(tokens) < 1:
        log_error("Invalid number of arguments for set total command!")
        return ([], ("total", False))

    if tokens[0] != "true" and tokens[0] != "false":
        return (tokens[1:], [("total", False)])

    return (tokens[1:], [("total", tokens[0])])


def parse_country_or_continent(tokens):
    if len(TaskRequest.countries) == 0 and len(TaskRequest.continents) == 0:
        log_error(
            f"Failed to find country or continent: {tokens[0]}, load data file first!"
        )
        return (tokens[1:], None)

    if tokens[0] in TaskRequest.countries:
        return (tokens[1:], [("country", tokens[0])])
    elif tokens[0] in TaskRequest.continents:
        return (tokens[1:], [("continent", tokens[0])])

    log_error(f"Invalid argument for 'in' command: {tokens[0]}")
    return (tokens[1:], None)


def parse_single_day(tokens):
    try:
        return (tokens[1:], [("day", int(tokens[0]))])
    except:
        return (tokens[1:], [("day"), None])


def parse_sort(tokens):
    order = None
    data_type = None
    tokens_to_skip = 1

    if len(tokens) > 0:
        if tokens[0] == "date" or tokens[0] == "deaths" or tokens[0] == "cases":
            data_type = tokens[0]

    if len(tokens) > 1:
        if tokens[1] == "ascending" or tokens[1] == "descending":
            order = tokens[1]
            tokens_to_skip = 2

    return (tokens[tokens_to_skip:], [("sort_type", data_type), ("sort_order", order)])


str_to_command = {
    "set": parse_set_command,
    "show": get_show_command,
    "reset": get_reset_command,
    "exit": get_exit_command,
}

set_to_command = {
    "from": parse_date,
    "to": parse_date,
    "type": parse_request_type,
    "total": parse_total_setting,
    "in": parse_country_or_continent,
    "on": parse_single_day,
    "sort": parse_sort,
}


class TaskRequest:
    countries = set()
    continents = set()

    def __init__(self):
        self.__execution_sequence: List[str] = []

    def reset_sequence(self):
        self.__execution_sequence = []

    def set_continents(self, continents):
        TaskRequest.continents = continents

    def set_countries(self, countries):
        TaskRequest.countries = countries

    def get_execution_sequence(self):
        if self.__execution_sequence:
            return self.__execution_sequence

    def remove_last_query(self):
        if len(self.__execution_sequence) > 0:
            self.__execution_sequence = self.__execution_sequence[:-1]

    def add_cmd(self, cmd: str):
        if not cmd:
            log_warn("Added command is empty!")
            return
            
        log_info(f"Adding new cmd: {cmd}")
        tokens = [token.lower() for token in cmd.split()]
        single_command = None

        while len(tokens) > 0:
            if tokens[0] == "set":
                self.__execution_sequence.extend(str_to_command["set"](tokens[1:]))
                return
            elif tokens[0] in str_to_command:
                single_command = str_to_command[tokens[0]]()
                tokens = []
            else:
                log_error(f"Invalid command: {tokens}")
                return

            if single_command:
                log_info(f"Adding parsed command: {single_command}")
                self.__execution_sequence.append(single_command)
