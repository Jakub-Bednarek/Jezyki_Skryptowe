import sys
from timeit import default_timer as timer
from covid_parser import parse_data_from_file

All_dates, By_date, By_country = parse_data_from_file()


def for_date_a(year, month, day):
    start = timer()
    deaths, cases = 0, 0
    for date in All_dates:
        if year == date[1] and month == date[2] and day == date[3]:
            deaths += date[4]
            cases += date[5]
            
    execution_time = (timer() - start) * 1000
    print("Czas wykonania dla for_date_a: %.2f" % execution_time + "ms")
    return (deaths, cases)


def for_date_d(year, month, day):
    start = timer()
    deaths, cases = 0, 0
    for key, value in By_date.items():
        if key[0] == year and key[1] == month and key[2] == day:
            for record in value:
                deaths += record[1]
                cases += record[2]
                
    execution_time = (timer() - start) * 1000
    print("Czas wykonania dla for_date_d %.2f" % execution_time + "ms")
    return (deaths, cases)


def for_date_c(year, month, day):
    start = timer()
    deaths, cases = 0, 0
    for key, value in By_country.items():
        for record in value:
            if record[0] == year and record[1] == month and record[2] == day:
                deaths += record[3]
                cases += record[4]
    
    execution_time = (timer() - start) * 1000
    print("Czas wykonania dla for_date_c: %.2f" % execution_time + "ms")
    return (deaths, cases)
        

def main():
    print(for_date_a(2020, 3, 21))
    print(for_date_d(2020, 3, 21))
    print(for_date_c(2020, 3, 21))
    
    
if __name__ == "__main__":
    main()