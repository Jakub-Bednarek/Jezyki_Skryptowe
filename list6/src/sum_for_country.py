import sys
from timeit import default_timer as timer
from covid_parser import parse_data_from_file

All_dates, By_date, By_country = parse_data_from_file()
DEFAULT_COUNTRY = "Poland"


def for_country_a(country):
    start = timer()
    deaths, cases = 0, 0
    for record in All_dates:
        if record[0] == country:
            deaths += record[4]
            cases += record[5]
            
    execution_time = (timer() - start) * 1000
    print("Czas wykonania dla for_country_a: %.2f" % execution_time + "ms")
    return (deaths, cases)


def for_country_d(country):
    start = timer()
    deaths, cases = 0, 0
    for key, value in By_date.items():
        for record in value:
            if record[0] == country:
                deaths += record[1]
                cases += record[2]
                
    execution_time = (timer() - start) * 1000
    print("Czas wykonania dla for_country_d: %.2f" % execution_time + "ms")
    return (deaths, cases)


def for_country_c(country):
    start = timer()
    deaths, cases = 0, 0
    for key, value in By_country.items():
        if key == country:
            for record in value:
                deaths += record[3]
                cases += record[4]
                
    execution_time = (timer() - start) * 1000
    print("Czas wykonania dla for_country_c: %.2f" % execution_time + "ms")
    return (deaths, cases)


def main():
    if len(sys.argv) < 2:
        print("No argument provided for country!")
        country = DEFAULT_COUNTRY
    else:
        country = sys.argv[1]
    
    print(for_country_a(country))
    print(for_country_d(country))
    print(for_country_c(country))


if __name__ == "__main__":
    main()