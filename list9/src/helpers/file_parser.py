from typing import List
from helpers.data_record import DataRecord
from helpers.logger import log_info, log_error, log_warn
from tkinter import messagebox


class InvalidFileFormatException(Exception):
    pass


class InvalidRecordException(Exception):
    pass


HEADER_TOKENS = [
    "dateRep",
    "day",
    "month",
    "year",
    "cases",
    "deaths",
    "countriesAndTerritories",
    "geoId",
    "countryterritoryCode",
    "popData2019",
    "continentExp",
    "Cumulative_number_for_14_days_of_COVID-19_cases_per_100000",
]

HEADER_TOKENS_LEN = len(HEADER_TOKENS)

DEFAULT_DATE_INDEX = 0
DEFAULT_DAY_INDEX = 1
DEFAULT_MONTH_INDEX = 2
DEFAULT_YEAR_INDEX = 3
DEFAULT_CASES_INDEX = 4
DEFAULT_DEATHS_INDEX = 5
DEFAULT_COUNTRY_INDEX = 6
DEFAULT_CONTINENT_INDEX = 10


def check_header_line(line: str, file_path: str) -> bool:
    line_tokens = line.split()

    if len(line_tokens) != len(HEADER_TOKENS):
        raise InvalidFileFormatException(
            f"Header line in file: {file_path} doesn't contains wrong number of columns"
        )

    for i in range(0, HEADER_TOKENS_LEN):
        if line_tokens[i] != HEADER_TOKENS[i]:
            messagebox.showerror("Blad", f"Niepoprawny format pliku: {file_path}")
            raise InvalidFileFormatException(
                f"In file: {file_path} header line is malformed, check correctness."
            )


def read_line_to_data_record(line: str, file_path: str) -> DataRecord:
    tokens = line.split()

    if len(tokens) != HEADER_TOKENS_LEN:
        raise InvalidRecordException(
            f"Failed reading line from file {file_path}, not enough tokens! Line: {line}"
        )

    try:
        record = DataRecord()
        return (
            record.add_date(tokens[DEFAULT_DAY_INDEX], tokens[DEFAULT_MONTH_INDEX])
            .add_day(tokens[DEFAULT_DAY_INDEX])
            .add_cases(tokens[DEFAULT_CASES_INDEX])
            .add_deaths(tokens[DEFAULT_DEATHS_INDEX])
            .add_country(tokens[DEFAULT_COUNTRY_INDEX])
            .add_continent(tokens[DEFAULT_CONTINENT_INDEX])
        )
    except Exception as e:
        log_error(f"Failed to read line: {line}Error: {e}")
        return None


def load_file(file_path: str) -> List[DataRecord]:
    log_info(f"Loading file: {file_path}")

    valid_records = []
    valid_countries = set()
    valid_continents = set()
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            lines = file.readlines()
            check_header_line(lines[0], file_path)

            for line in lines[1:]:
                try:
                    record = read_line_to_data_record(line, file_path)
                except InvalidRecordException as e:
                    log_warn(str(e))

                if record:
                    valid_records.append(record)
                    valid_countries.add(record.country)
                    valid_continents.add(record.continent)
    except Exception as e:
        messagebox.showerror(
            "Blad",
            f"Niepowodzenie podczas ladowania pliku: {file_path}, plik nie istnieje.",
        )
        return None

    log_info(f"Success reading file: {file_path}")
    return valid_records, valid_countries, valid_continents
