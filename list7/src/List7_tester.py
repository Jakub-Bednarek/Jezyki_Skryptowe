import sys
import re
from Person import Person
from First_name import load_data
from Test_data_generator import DEFAULT_TEST_DATA_FILE_NAME, bcolors


def print_test_specs(test_data_file_name):
    print(
        f"\n\n{bcolors.OKYELLOW}Starting test scenario with parameters:{bcolors.ENDC}"
    )
    print(
        f"\tTest data file name: {bcolors.OKGREEN}{test_data_file_name}{bcolors.ENDC}"
    )


def run_test(path, test_data_file_name):
    success = 0
    failure = 0
    test_data = load_data(path + test_data_file_name, False)

    print_test_specs(test_data_file_name)

    for line in test_data:
        try:
            person = Person.fromString(line)
            print(
                f"{bcolors.OKGREEN}Success creating Person with parameters: {bcolors.ENDC}"
            )
            success += 1
        except:
            print(
                f"{bcolors.OKRED}Failure creating Person with parameters: {bcolors.ENDC}"
            )
            failure += 1
        print("\t" + line + "\n")

    print("\nFinished running test scenario, results:")
    print(f"{bcolors.OKGREEN}Success{bcolors.ENDC}: {success}")
    print(f"{bcolors.OKRED}Failure{bcolors.ENDC}: {failure}")


def parse_args():
    args = sys.argv
    if len(args) < 3:
        return DEFAULT_TEST_DATA_FILE_NAME
    else:
        return args[1], args[2]


def main():
    path, test_data_file_name = parse_args()
    run_test(path, test_data_file_name)


if __name__ == "__main__":
    main()
