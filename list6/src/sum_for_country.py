import sys
from timeit import default_timer as timer
from covid_parser import parse_data_from_file

All_dates, By_date, By_country = parse_data_from_file()
DEFAULT_COUNTRY = "Poland"
RETURN_ONLY_TIME = False


def for_country_a(country):
    start = timer()
    deaths, cases = 0, 0
    for record in All_dates:
        if record[0] == country:
            deaths += record[4]
            cases += record[5]

    execution_time = (timer() - start) * 1000
    if not RETURN_ONLY_TIME:
        print("Czas wykonania dla for_country_a: %.2f" % execution_time + "ms")
        return (deaths, cases)
    else:
        return execution_time


def for_country_d(country):
    start = timer()
    deaths, cases = 0, 0
    for key, value in By_date.items():
        for record in value:
            if record[0] == country:
                deaths += record[1]
                cases += record[2]

    execution_time = (timer() - start) * 1000
    if not RETURN_ONLY_TIME:
        print("Czas wykonania dla for_country_d: %.2f" % execution_time + "ms")
        return (deaths, cases)
    else:
        return execution_time


def for_country_c(country):
    start = timer()
    deaths, cases = 0, 0
    for key, value in By_country.items():
        if key == country:
            for record in value:
                deaths += record[3]
                cases += record[4]

    execution_time = (timer() - start) * 1000
    if not RETURN_ONLY_TIME:
        print("Czas wykonania dla for_country_c: %.2f" % execution_time + "ms")
        return (deaths, cases)
    else:
        return execution_time


def main():
    if len(sys.argv) < 2:
        print("No argument provided for country!")
        country = DEFAULT_COUNTRY
    else:
        country = sys.argv[1]

    global RETURN_ONLY_TIME
    RETURN_ONLY_TIME = len(sys.argv) == 3 and sys.argv[2] == "True"

    res1 = for_country_a(country)
    res2 = for_country_d(country)
    res3 = for_country_c(country)
    if not RETURN_ONLY_TIME:
        print(str(res1) + "\n" + str(res2) + "\n" + str(res3))
    else:
        print(res1, res2, res3)


if __name__ == "__main__":
    main()
