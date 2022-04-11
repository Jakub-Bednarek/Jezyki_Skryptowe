import sys
from timeit import default_timer as timer
from covid_parser import parse_data_from_file

All_dates, By_date, By_country = parse_data_from_file()
DEFAULT_COUNTRY = "Poland"
DEFAULT_YEAR = 2020
DEFAULT_MONTH = 1
DEFAULT_DAY = 1
RETURN_ONLY_TIME = False


def for_date_country_a(year, month, day, country):
    start = timer()
    deaths, cases = (0, 0)
    for record in All_dates:
        if (record[0], record[1], record[2], record[3]) == (country, year, month, day):
            deaths += record[4]
            cases += record[5]

    execution_time = (timer() - start) * 1000
    if not RETURN_ONLY_TIME:
        print("Czas wykonania dla for_date_country_a: %.2f" % execution_time + "ms")
        return (deaths, cases)
    else:
        return execution_time


def for_date_country_d(year, month, day, country):
    start = timer()
    deaths, cases = 0, 0
    for key, value in By_date.items():
        if key == (year, month, day):
            for record in value:
                if record[0] == country:
                    deaths += record[1]
                    cases += record[2]

    execution_time = (timer() - start) * 1000
    if not RETURN_ONLY_TIME:
        print("Czas wykonania dla for_date_country_d: %.2f" % execution_time + "ms")
        return (deaths, cases)
    else:
        return execution_time


def for_date_country_c(year, month, day, country):
    start = timer()
    deaths, cases = 0, 0
    for key, value in By_country.items():
        if key == country:
            for record in value:
                if (record[0], record[1], record[2]) == (year, month, day):
                    deaths += record[3]
                    cases += record[4]

    execution_time = (timer() - start) * 1000
    if not RETURN_ONLY_TIME:
        print("Czas wykonania dla for_date_country_c: %.2f" % execution_time + "ms")
        return (deaths, cases)
    else:
        return execution_time


def parse_args(args):
    try:
        return int(args[1]), int(args[2]), int(args[3]), args[4]
    except:
        print("Invalid arguments!")
        return DEFAULT_YEAR, DEFAULT_MONTH, DEFAULT_DAY, DEFAULT_COUNTRY


def main():
    year, month, day, country = parse_args(sys.argv)

    global RETURN_ONLY_TIME
    RETURN_ONLY_TIME = len(sys.argv) == 6 and sys.argv[5] == "True"

    res1 = for_date_country_a(year, month, day, country)
    res2 = for_date_country_d(year, month, day, country)
    res3 = for_date_country_c(year, month, day, country)

    if not RETURN_ONLY_TIME:
        print(str(res1) + "\n" + str(res2) + "\n" + str(res3))
    else:
        print(res1, res2, res3)


if __name__ == "__main__":
    main()
