from enum import Enum
from typing import List
from logger import log_info, log_warn, log_error

DEFAULT_COUNTRY = "Poland"
DEFAULT_CONTINENT = "Europe"

test_country_set = set(["poland", "pfghanistan"])
test_continent_set = set(["asia", "europe", "africa", "america", "oceania"])


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


def parse_date(tokens, begin=True):
    if len(tokens) < 1:
        log_error("Invalid number of arguments in set date function!")
        return ([], None)

    tokens_to_skip = 1
    if begin:
        month_str, day_str = "month_begin", "day_begin"
    else:
        month_str, day_str = "month_end", "day_end"

    output_seq = None
    for month in Month:
        if month.name.lower() == tokens[0]:
            output_seq = [(month_str, month.value)]

    if len(tokens) > 1:
        try:
            day = int(tokens[1])
            tokens_to_skip = 2
            output_seq.append((day_str, day))
        except:
            pass

    return (tokens[tokens_to_skip:], output_seq)


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
    if tokens[0] in test_country_set:
        return (tokens[1:], ("country", tokens[0]))
    elif tokens[0] in test_continent_set:
        return (tokens[1:], ("continentExp", tokens[0]))

    log_error(f"Invalid argument for 'in' command: {tokens[0]}")
    return (tokens[1:], None)


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
}


class TaskRequest:
    def __init__(self):
        self.__execution_sequence: List[str] = []
        self.__execute_now = False
        self.__finished = False

    def get_execute_now(self) -> bool:
        return self.__execute_now

    def get_finish_now(self) -> bool:
        return self.__finished

    def get_execution_sequence(self):
        if not len(self.__execution_sequence):
            log_error("Execution_sequence is empty, add commands first!")
        else:
            return self.__execution_sequence

    #
    def add_cmd(self, cmd: str):
        log_info(f"Adding new cmd: {cmd}")
        tokens = [token.lower() for token in cmd.split()]
        single_command = None

        while len(tokens) > 0:
            if tokens[0] == "set":
                self.__execution_sequence = str_to_command["set"](tokens[1:])
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
