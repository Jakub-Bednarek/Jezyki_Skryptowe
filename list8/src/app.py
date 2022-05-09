from task_request import TaskRequest
from logger import msg_logger, log_error, log_info
from console import get_integer, get_string
import datetime

DEFAULT_DATE_INDEX = 0
DEFAULT_DAY_INDEX = 1
DEFAULT_MONTH_INDEX = 2
DEFAULT_YEAR_INDEX = 3
DEFAULT_CASES_INDEX = 4
DEFAULT_DEATHS_INDEX = 5
DEFAULT_COUNTRY_INDEX = 6
DEFAULT_CONTINENT_INDEX = 10


class Settings:
    def __init__(self):
        self.date_begin = None
        self.date_end = None
        self.day = None
        self.country = None
        self.continent = None
        self.type = "deaths"
        self.total = False
        self.sort_type = None
        self.sort_order = "ascending"

    def add_new_config(self, config):
        if len(config) == 1:
            log_error("No valid settings provided")
            return False

        for conf in config:
            if conf[0] == "date_begin":
                self.date_begin = conf[1]
            elif conf[0] == "date_end":
                self.date_end = conf[1]
            elif conf[0] == "day":
                self.day = conf[1]
            elif conf[0] == "country":
                self.country = conf[1]
            elif conf[0] == "continent":
                self.continent = conf[1]
            elif conf[0] == "type":
                self.type = conf[1]
            elif conf[0] == "total":
                self.total = conf[1]
            elif conf[0] == "sort_type":
                self.sort_type = conf[1]
            elif conf[0] == "sort_order":
                self.sort_order = conf[1]

        return True


class DataRecord:
    settings = None

    def add_settings(self, settings):
        DataRecord.settings = settings

    def add_date(self, day, month):
        self.date = datetime.datetime.strptime(f"{day}-{month}-2020", "%d-%m-%Y")
        return self

    def add_day(self, day):
        try:
            self.day = int(day)
        except:
            self.day = None
        return self

    def add_deaths(self, deaths):
        try:
            self.deaths = int(deaths)
        except:
            self.deaths = 0
        return self

    def add_cases(self, cases):
        try:
            self.cases = int(cases)
        except:
            self.cases = 0
        return self

    def add_country(self, country):
        self.country = country
        return self

    def add_continent(self, continent):
        self.continent = continent
        return self

    def get_cases(self):
        try:
            return int(self.cases)
        except:
            log_error(f"Failed to cast cases value to int: {self.deaths}")
            return 0

    def get_deaths(self):
        try:
            return int(self.deaths)
        except:
            log_error(f"Failed to cast deaths value to int: {self.deaths}")
            return 0

    def is_date_valid(self, date_begin, date_end, day):
        result = True
        if date_begin:
            result = result and self.date >= date_begin
        if date_end:
            result = result and self.date <= date_end
        if day:
            result = result or self.day == day

        return result

    def is_valid(self, settings):
        if not settings:
            log_error("Failed to gather data, no settings provided!")
            return False

        if not self.is_date_valid(settings.date_begin, settings.date_end, settings.day):
            return False
        if settings.country and self.country.lower() != settings.country:
            return False
        if settings.continent and self.continent.lower() != settings.continent:
            return False

        return True

    def __str__(self):
        return (
            f"Date: {self.date} | Deaths: {self.deaths} | Cases: {self.cases} "
            f"| Country: {self.country} | Continent: {self.continent}"
        )


def sort_data_record_date(data_record):
    return data_record.date


def sort_data_record_cases(data_record):
    return data_record.cases


def sort_data_record_deaths(data_record):
    return data_record.deaths


class App:
    def __init__(self):
        self.__request = TaskRequest()
        self.__file_data = []
        self.__should_terminate = False
        self.__settings = None
        msg_logger.init_logger("Test.log")

        log_info("Initialized app")

    def load_data(self, file_name, skip=0):
        available_continents = set()
        available_countries = set()
        try:
            with open(file_name, "r") as file:
                for line in file.readlines()[skip:]:
                    tokens = line.split()
                    record = self.__parse_data_tokens(tokens)

                    if record:
                        self.__file_data.append(record)
                        available_countries.add(tokens[DEFAULT_COUNTRY_INDEX].lower())
                        available_continents.add(
                            tokens[DEFAULT_CONTINENT_INDEX].lower()
                        )
        except:
            log_error(f"Failed to load file: {file_name}")
            return

        self.set_continents(available_continents)
        self.set_countries(available_countries)
        log_info(f"Loaded file: {file_name}")

    def set_continents(self, continents):
        self.__request.set_continents(continents)

    def set_countries(self, countries):
        self.__request.set_countries(countries)

    def get_input(self):
        choice = get_integer("Choice")
        if choice == 1:
            file_path = get_string("File path")
            self.load_data(file_path, 1)
        elif choice == 2:
            file_path = get_string("File path")
            msg_logger.set_logger_file(file_path)
        elif choice == 3:
            query_str = get_string("Query string")
            self.__request.add_cmd(query_str)
        elif choice == 4:
            print(self.__request.get_execution_sequence())

        self.check_for_actions()

    def terminate(self):
        log_info("Terminating application.")
        msg_logger.cleanup_logger()
        self.__should_terminate = True

    def parse_settings(self):
        queries = self.__request.get_execution_sequence()
        self.__settings = Settings()

        if not self.__settings.add_new_config(queries):
            return False

        return True

    def show_data(self):
        sum = 0
        valid_records = []
        log_info("\nBeginning data analysis.")
        for record in self.__file_data:
            if record.is_valid(self.__settings):
                valid_records.append(record)
                if self.__settings.type == "deaths":
                    sum += record.get_deaths()
                else:
                    sum += record.get_cases()

        if self.__settings.sort_type:
            valid_records = self.sort_data(valid_records)

        for record in valid_records:
            log_info(str(record))
        if self.__settings.total:
            log_info(f"Total value for {self.__settings.type}: {sum}")

    def sort_data(self, data):
        reverse = False if self.__settings.sort_order == "ascending" else True
        if self.__settings.sort_type:
            if self.__settings.sort_type == "date":
                return sorted(data, key=sort_data_record_date, reverse=reverse)
            if self.__settings.sort_type == "cases":
                return sorted(data, key=sort_data_record_cases, reverse=reverse)
            if self.__settings.sort_type == "deaths":
                return sorted(data, key=sort_data_record_deaths, reverse=reverse)

    def check_for_actions(self):
        if not self.__request.get_execution_sequence():
            return

        last_query = self.__request.get_execution_sequence()[-1]
        if last_query == "exit":
            self.terminate()
        elif last_query == "reset":
            self.__request.reset_sequence()
            self.__request.remove_last_query()
        elif last_query == "show":
            if self.parse_settings():
                self.show_data()
            self.__request.remove_last_query()

    def should_terminate(self):
        return self.__should_terminate

    def __parse_data_tokens(self, tokens):
        record = DataRecord()
        if len(tokens) < 11:
            return None

        return (
            record.add_date(tokens[DEFAULT_DAY_INDEX], tokens[DEFAULT_MONTH_INDEX])
            .add_day(tokens[DEFAULT_DAY_INDEX])
            .add_cases(tokens[DEFAULT_CASES_INDEX])
            .add_deaths(tokens[DEFAULT_DEATHS_INDEX])
            .add_country(tokens[DEFAULT_COUNTRY_INDEX])
            .add_continent(tokens[DEFAULT_CONTINENT_INDEX])
        )
