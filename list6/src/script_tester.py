from subprocess import Popen, PIPE
import os
import sys
import operator
import random
from unittest.mock import DEFAULT

SUM_FOR_COUNTRY_SCRIPT_NAME = "sum_for_country.py"
SUM_FOR_DATE_SCRIPT_NAME = "sum_for_date.py"
SUM_FOR_DATE_COUNTRY_SCRIPT_NAME = "sum_for_date_country.py"
DEFAULT_TEST_RUNS = 100
DEFAULT_COUNTRY_NAME_INDEX = 6
YEAR_FOR_TEST_GENERATOR = "2020"
MIN_MONTH_FOR_GENERATOR = 1
MAX_MONTH_FOR_GENERATOR = 13
MIN_DAY_FOR_GENERATOR = 1
MAX_DAY_FOR_GENERATOR = 32


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    OKYELLOW = "\033[33m"
    ENDC = "\033[0m"


class ResultsHolder:
    def __init__(self):
        self.country_res_sum = (0.0, 0.0, 0.0)
        self.date_res_sum = (0.0, 0.0, 0.0)
        self.date_country_res_sum = (0.0, 0.0, 0.0)
        self.lowest_highest_for_country = (
            (99999.0, 0.0),
            (99999.0, 0.0),
            (99999.0, 0.0),
        )
        self.lowest_highest_for_date = ((99999.0, 0.0), (99999.0, 0.0), (99999.0, 0.0))
        self.lowest_highest_for_date_country = (
            (99999.0, 0.0),
            (99999.0, 0.0),
            (99999.0, 0.0),
        )

    def sum_triple_tuple(self, lhs, rhs):
        return (lhs[0] + rhs[0], lhs[1] + rhs[1], lhs[2] + rhs[2])

    def calculate_new_lowest_highest_single(self, lhs, rhs):
        return (
            (min(lhs[0][0], rhs[0]), max(lhs[0][1], rhs[0])),
            (min(lhs[1][0], rhs[1]), max(lhs[1][1], rhs[1])),
            (min(lhs[2][0], rhs[2]), max(lhs[2][1], rhs[2])),
        )

    def calculate_new_lowest_highest(self, case_res):
        self.lowest_highest_for_country = self.calculate_new_lowest_highest_single(
            self.lowest_highest_for_country, case_res[0]
        )
        self.lowest_highest_for_date = self.calculate_new_lowest_highest_single(
            self.lowest_highest_for_date, case_res[1]
        )
        self.lowest_highest_for_date_country = self.calculate_new_lowest_highest_single(
            self.lowest_highest_for_date_country, case_res[2]
        )

    def add_new_case_result(self, case_res):
        self.country_res_sum = self.sum_triple_tuple(self.country_res_sum, case_res[0])
        self.date_res_sum = self.sum_triple_tuple(self.date_res_sum, case_res[1])
        self.date_country_res_sum = self.sum_triple_tuple(
            self.date_country_res_sum, case_res[2]
        )

        self.calculate_new_lowest_highest(case_res)

    def get_lowest_value_from_tuple_of_tuples(self, t):
        low = 99999.0
        for single_tuple in t:
            for val in single_tuple:
                low = min(low, val)
        return low

    def get_highest_value_from_tuple_of_tuples(self, t):
        high = 0.0
        for single_tuple in t:
            for val in single_tuple:
                high = max(high, val)
        return high

    def get_total_lowest_highest(self):
        low = self.get_lowest_value_from_tuple_of_tuples(
            self.lowest_highest_for_country
        )
        low = min(
            low,
            self.get_lowest_value_from_tuple_of_tuples(self.lowest_highest_for_date),
        )
        low = min(
            low,
            self.get_lowest_value_from_tuple_of_tuples(
                self.lowest_highest_for_date_country
            ),
        )

        high = self.get_highest_value_from_tuple_of_tuples(
            self.lowest_highest_for_country
        )
        high = max(
            high,
            self.get_highest_value_from_tuple_of_tuples(self.lowest_highest_for_date),
        )
        high = max(
            high,
            self.get_highest_value_from_tuple_of_tuples(
                self.lowest_highest_for_date_country
            ),
        )

        return (low, high)


def pull_all_countries_from_file(filename):
    country_names = set()
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            tokens = line.split()
            country_names.add(tokens[DEFAULT_COUNTRY_NAME_INDEX])

    return country_names


def gen_random_test_data(country_names):
    country_names_size = len(country_names)
    return (
        YEAR_FOR_TEST_GENERATOR,
        str(random.randrange(MIN_MONTH_FOR_GENERATOR, MAX_MONTH_FOR_GENERATOR)),
        str(random.randrange(MIN_DAY_FOR_GENERATOR, MAX_DAY_FOR_GENERATOR)),
        list(country_names)[random.randrange(0, country_names_size)],
    )


def cleanup_tuple(string):
    tuple_tokens = string.replace("\\n", "").replace("b'", "").replace("'", "").split()
    return (float(tuple_tokens[0]), float(tuple_tokens[1]), float(tuple_tokens[2]))


def run_country_test(country):
    p = Popen(
        ["python3", SUM_FOR_COUNTRY_SCRIPT_NAME, country, "True"],
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
    )

    output, err = p.communicate()
    return cleanup_tuple(str(output))


def run_date_test(year, month, day):
    p = Popen(
        ["python3", SUM_FOR_DATE_SCRIPT_NAME, year, month, day, "True"],
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
    )

    output, err = p.communicate()
    return cleanup_tuple(str(output))


def run_date_country_test(year, month, day, country):
    p = Popen(
        [
            "python3",
            SUM_FOR_DATE_COUNTRY_SCRIPT_NAME,
            year,
            month,
            day,
            country,
            "True",
        ],
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
    )

    output, err = p.communicate()
    return cleanup_tuple(str(output))


def run_test_case(country_names):
    test_data = gen_random_test_data(country_names)
    country_res = run_country_test(test_data[3])
    date_res = run_date_test(test_data[0], test_data[1], test_data[2])

    print(
        "Running test with generated data: %s(%s, %s, %s, %s)%s"
        % (
            bcolors.OKYELLOW,
            test_data[0],
            test_data[1],
            test_data[2],
            test_data[3],
            bcolors.ENDC,
        )
    )
    date_country_res = run_date_country_test(
        test_data[0], test_data[1], test_data[2], test_data[3]
    )

    return (country_res, date_res, date_country_res)


def print_single_scripts_results(
    script_results, script_name, func_name, n_cases, lowest_highest
):
    func_suffixes = ["a", "d", "c"]

    print("\nResult for script %s%s%s" % (bcolors.OKBLUE, script_name, bcolors.ENDC))
    for i in range(0, 3):
        print(
            f"\tFunction: %s%s_%s%s\n\t\tTotal time: %s%.2f ms%s\n\t\tAverage time: %s%.2fms%s\n\t\tBest time: %s%.2fms%s\n\t\tWorst time: %s%.2fms%s"
            % (
                bcolors.OKYELLOW,
                func_name,
                func_suffixes[i],
                bcolors.ENDC,
                bcolors.OKGREEN,
                script_results[i],
                bcolors.ENDC,
                bcolors.OKGREEN,
                script_results[i] / n_cases,
                bcolors.ENDC,
                bcolors.OKGREEN,
                lowest_highest[i][1],
                bcolors.ENDC,
                bcolors.OKGREEN,
                lowest_highest[i][0],
                bcolors.ENDC,
            )
        )


def output_pretty_results(scenario_results, n_cases):
    print_single_scripts_results(
        scenario_results.country_res_sum,
        "sum_for_country.py",
        "for_country",
        n_cases,
        scenario_results.lowest_highest_for_country,
    )
    print_single_scripts_results(
        scenario_results.date_res_sum,
        "sum_for_date.py",
        "for_date",
        n_cases,
        scenario_results.lowest_highest_for_date,
    )
    print_single_scripts_results(
        scenario_results.date_country_res_sum,
        "sum_for_date_country.py",
        "for_date_country",
        n_cases,
        scenario_results.lowest_highest_for_date_country,
    )


def run_test_scenario(cases):
    print(
        "Starting test scenario for %s%d%s cases"
        % (bcolors.OKGREEN, cases, bcolors.ENDC)
    )

    holder = ResultsHolder()
    country_names = pull_all_countries_from_file("Covid.txt")
    for i in range(0, cases):
        case_res = run_test_case(country_names)
        holder.add_new_case_result(case_res)

    print("%sAll test finished.%s" % (bcolors.OKGREEN, bcolors.ENDC))

    output_pretty_results(holder, cases)


def main():
    try:
        scenario_cases = int(sys.argv[1])
    except:
        scenario_cases = DEFAULT_TEST_RUNS

    if not scenario_cases:
        scenario_cases = DEFAULT_TEST_RUNS

    run_test_scenario(scenario_cases)


if __name__ == "__main__":
    main()
