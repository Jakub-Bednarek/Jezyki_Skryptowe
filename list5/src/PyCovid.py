from argparse import ArgumentError
import sys

DEFAULT_COVID_FILENAME  = "Covid.txt"
DEFAULT_COUNTRY         = "Poland"
DEFAULT_MONTH           = "3"
DEFAULT_COUNTRY_INDEX   = 6
DEFAULT_MONTH_INDEX     = 2
DEFAULT_CASES_INDEX     = 4
EXPECTED_MINIMUM_TOKENS_IN_LINE = 11
EXPECTED_ARGUMENTS_SIZE = 3

def extract_cases(line: str, month: str, country: str) -> int:
    tokens = line.split()
    
    if len(tokens) < EXPECTED_MINIMUM_TOKENS_IN_LINE:
        return 0
    
    cases = 0
    if tokens[DEFAULT_MONTH_INDEX] == month and tokens[DEFAULT_COUNTRY_INDEX] == country:
        try:
            cases = int(tokens[DEFAULT_CASES_INDEX])
        except ValueError:
            pass
    
    return cases

def get_all_cases(month: str, country: str):
    total_cases = 0
    with open(DEFAULT_COVID_FILENAME) as f:
        all_lines = f.readlines()
        
        for line in all_lines:
            total_cases += extract_cases(line, month, country)
            
    return total_cases
            

def parse_arguments():
    arguments = sys.argv
    if len(arguments) == 1:
        return DEFAULT_MONTH, DEFAULT_COUNTRY
    
    if arguments[1].isnumeric():
        return arguments[1], arguments[2]
    else:
        return arguments[2], arguments[1]

def main():
    month, country = parse_arguments()
    print(f"{month}, {country}")
    print(get_all_cases(month, country))
    

if __name__ == "__main__":
    main()