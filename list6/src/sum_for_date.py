import sys
from timeit import default_timer as timer
from covid_parser import parse_data_from_file

All_dates, By_date, By_country = parse_data_from_file()
DEFAULT_YEAR = 2020
DEFAULT_MONTH = 1
DEFAULT_DAY = 1
RETURN_ONLY_TIME = False


def for_date_a(year, month, day):
    start = timer()
    deaths, cases = 0, 0
    for date in All_dates:
        if year == date[1] and month == date[2] and day == date[3]:
            deaths += date[4]
            cases += date[5]

    execution_time = (timer() - start) * 1000
    if not RETURN_ONLY_TIME:
        print("Czas wykonania dla for_date_a: %.2f" % execution_time + "ms")
        return (deaths, cases)
    else:
        return execution_time


def for_date_d(year, month, day):
    start = timer()
    deaths, cases = 0, 0
    for key, value in By_date.items():
        if key[0] == year and key[1] == month and key[2] == day:
            for record in value:
                deaths += record[1]
                cases += record[2]

    execution_time = (timer() - start) * 1000
    if not RETURN_ONLY_TIME:
        print("Czas wykonania dla for_date_d: %.2f" % execution_time + "ms")
        return (deaths, cases)
    else:
        return execution_time


def for_date_c(year, month, day):
    start = timer()
    deaths, cases = 0, 0
    for key, value in By_country.items():
        for record in value:
            if record[0] == year and record[1] == month and record[2] == day:
                deaths += record[3]
                cases += record[4]

    execution_time = (timer() - start) * 1000
    if not RETURN_ONLY_TIME:
        print("Czas wykonania dla for_date_c: %.2f" % execution_time + "ms")
        return (deaths, cases)
    else:
        return execution_time


def measure_date_time(year, month, day):
    start = timer()


def main():
    args = sys.argv

    try:
        year, month, day = int(args[1]), int(args[2]), int(args[3])
    except:
        print("Invalid arguments!")
        year, month, day = DEFAULT_YEAR, DEFAULT_MONTH, DEFAULT_DAY

    global RETURN_ONLY_TIME
    RETURN_ONLY_TIME = len(sys.argv) == 5 and sys.argv[4] == "True"

    res1 = for_date_a(year, month, day)
    res2 = for_date_d(year, month, day)
    res3 = for_date_c(year, month, day)

    if not RETURN_ONLY_TIME:
        print(str(res1) + "\n" + str(res2) + "\n" + str(res3))
    else:
        print(res1, res2, res3)


if __name__ == "__main__":
    main()
