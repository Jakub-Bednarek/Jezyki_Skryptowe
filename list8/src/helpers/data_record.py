from logger import log_error
import datetime


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
        self.day = int(day)
        return self

    def add_deaths(self, deaths):
        self.deaths = int(deaths)
        return self

    def add_cases(self, cases):
        self.cases = int(cases)
        return self

    def add_country(self, country):
        self.country = country
        return self

    def add_continent(self, continent):
        self.continent = continent
        return self

    def get_cases(self):
        return self.cases

    def get_deaths(self):
        return self.deaths

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
