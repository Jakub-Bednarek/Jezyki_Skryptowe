import sys
import random
import string
from First_name import load_data
from First_name import DEFAULT_NAMES_FILE_NAME

DEFAULT_TEST_DATA_FILE_NAME = "test_data.txt"
DEFAULT_TEST_DATA_COUNT = 100
DEFAULT_FEMALE_LAST_NAME_FILE = "nazw_zenskie.txt"
DEFAULT_MALE_LAST_NAME_FILE = "nazw_meskie.txt"

LETTERS = string.ascii_lowercase


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    OKYELLOW = "\033[33m"
    OKRED = "\033[31m"
    ENDC = "\033[0m"


def gen_delimiter():
    generated = random.randint(0, 2)

    if generated == 0:
        return " "
    elif generated == 1:
        return ";"
    else:
        return "\\"


def gen_name(names):
    if random.randint(0, 9) < 7:
        return names[random.randint(0, len(names) - 1)]
    else:
        return "".join(random.choice(LETTERS) for i in range(4, 10))


def gen_last(is_male, last_male, last_female):
    if random.randint(0, 9) < 2:
        return "".join(random.choice(LETTERS) for i in range(4, 12)).title()
    else:
        if is_male:
            return last_male[random.randint(0, len(last_male) - 1)].title()
        else:
            return last_female[random.randint(0, len(last_female) - 1)].title()


def gen_data(names, last_male, last_female):
    delimiter = gen_delimiter()
    name = gen_name(names)
    last_name = gen_last(name.endswith("a"), last_male, last_female)
    id_number = random.randint(1000000, 9999999)

    return name + delimiter + last_name + delimiter + str(id_number) + "\n"


def generate_data(path, file_name, count):
    names = load_data(DEFAULT_NAMES_FILE_NAME)
    last_female = load_data(path + DEFAULT_FEMALE_LAST_NAME_FILE)
    last_male = load_data(path + DEFAULT_MALE_LAST_NAME_FILE)
    output_string = ""

    print(f"{bcolors.OKYELLOW}Generating data with settings:{bcolors.ENDC}")
    print(f"\tCases to generate: {bcolors.OKGREEN}{count}{bcolors.ENDC}")
    print(f"\tNames file: {bcolors.OKGREEN}{DEFAULT_NAMES_FILE_NAME}{bcolors.ENDC}")
    print(
        f"\tFemale last names file: {bcolors.OKGREEN}{DEFAULT_FEMALE_LAST_NAME_FILE}{bcolors.ENDC}"
    )
    print(
        f"\tMale last names file: {bcolors.OKGREEN}{DEFAULT_MALE_LAST_NAME_FILE}{bcolors.ENDC}"
    )

    for i in range(0, count):
        output_string += gen_data(names, last_male, last_female)
        if (i / count) * 100 % 10 == 0 and i != 0:
            print(f"{bcolors.OKGREEN}{i * 100 / count:.2f}%{bcolors.ENDC}")

    print(f"{bcolors.OKGREEN}100%{bcolors.ENDC}")

    print(f"Writing data to file: {bcolors.OKGREEN}{file_name}{bcolors.ENDC}")
    with open(path + file_name, "w") as f:
        f.write(output_string)
    print(f"Finished")


def parse_args():
    args = sys.argv
    print(args)
    if len(args) < 4:
        return (" ", DEFAULT_TEST_DATA_FILE_NAME, DEFAULT_TEST_DATA_COUNT)
    else:
        try:
            return (args[1], args[2], int(args[3]))
        except:
            return (" ", args[2], DEFAULT_TEST_DATA_COUNT)


def main():
    path, file_name, count = parse_args()
    generate_data(path, file_name, count)


if __name__ == "__main__":
    main()
