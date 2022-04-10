import sys
from timeit import default_timer as timer
from covid_parser import parse_data_from_file

All_dates, By_date, By_country = parse_data_from_file()
DEFAULT_COUNTRY = "Poland"
DEFAULT_YEAR = 2020
DEFAULT_MONTH = 1
DEFAULT_DAY = 1


def for_country_a(year, month, day, country):
    start = timer()
    deaths, cases = 0, 0
    for record in All_dates:
        if record[0] == country and record[1] == year and record[2] == month and record[3] == day:
            deaths += record[4]
            cases += record[5]
            
    return (deaths, cases)


def for_country_d(year, month, day, country):
    start = timer()
    deaths, cases = 0, 0
    for key, value in By_date.items():
        if key == (year, month, day):
            for record in value:
                if record[0] == country:
                    deaths += record[1]
                    cases += record[2]
    return (deaths, cases)


def for_country_c(year, month, day, country):
    start = timer()
    deaths, cases = 0, 0
    for key, value in By_country.items():
        if key == country: 
            for record in value:
                if(record[0], record[1], record[2]) == (year, month, day):
                    deaths += record[3]
                    cases += record[4]
    return (deaths, cases)


def parse_args(args):
    try:
        return int(args[1]), int(args[2]), int(args[3]), args[4]
    except:
        print("Invalid arguments!")
        return DEFAULT_YEAR, DEFAULT_MONTH, DEFAULT_DAY, DEFAULT_COUNTRY


def main():
    year, month, day, country = parse_args(sys.argv)
    
    print(for_country_a(year, month, day, country))
    print(for_country_d(year, month, day, country))
    print(for_country_c(year, month, day, country))


if __name__ == "__main__":
    main()