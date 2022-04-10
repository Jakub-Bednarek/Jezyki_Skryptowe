from gc import get_count


DEFAULT_COVID_FILE_NAME = "Covid.txt"
DEFAULT_NAME_INDEX = 6
DEFAULT_DEATHS_INDEX = 5
DEFAULT_CASES_INDEX = 4
DEFAULT_YEAR_INDEX = 3
DEFAULT_MONTH_INDEX = 2
DEFAULT_DAY_INDEX = 1

def get_tuple_list_record(tokens_list):
    return (tokens_list[DEFAULT_NAME_INDEX], 
            tokens_list[DEFAULT_YEAR_INDEX], 
            tokens_list[DEFAULT_MONTH_INDEX], 
            tokens_list[DEFAULT_DAY_INDEX], 
            tokens_list[DEFAULT_DEATHS_INDEX], 
            tokens_list[DEFAULT_CASES_INDEX])
    
def get_date_dict_key_value(tokens_list):
    return ((tokens_list[DEFAULT_YEAR_INDEX], tokens_list[DEFAULT_MONTH_INDEX], tokens_list[DEFAULT_DAY_INDEX]),
            (tokens_list[DEFAULT_NAME_INDEX], tokens_list[DEFAULT_DEATHS_INDEX], tokens_list[DEFAULT_CASES_INDEX]))
    
def get_country_dict_key_value(tokens_list):
    return (tokens_list[DEFAULT_NAME_INDEX], 
            (tokens_list[DEFAULT_YEAR_INDEX], tokens_list[DEFAULT_MONTH_INDEX], tokens_list[DEFAULT_DAY_INDEX], tokens_list[DEFAULT_DEATHS_INDEX], tokens_list[DEFAULT_CASES_INDEX]))

def parse_data_from_file():
    all_cases = []
    by_date = {}
    by_country = {}
    
    with open(DEFAULT_COVID_FILE_NAME) as file:
        raw_text = file.readlines()
        i = 0
        for line in raw_text:
            tokens = line.split()
            all_cases.append(get_tuple_list_record(tokens))
            date_dict_record = get_date_dict_key_value(tokens)
            by_date[date_dict_record[0]] = date_dict_record[1]
            country_dict_record = get_country_dict_key_value(tokens)
            by_country[country_dict_record[0]] = country_dict_record[1]
    return (all_cases, by_date, by_country)
            

def main():
    all, by_date, by_country = parse_data_from_file()
    for elem in by_date:
        print(elem + by_date[elem])

if __name__ == "__main__":
    main()