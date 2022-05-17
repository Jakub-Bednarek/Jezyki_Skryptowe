from helpers.logger import log_error
from tkinter import messagebox
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


def sort_data_record_date(data_record):
    return data_record.date


def sort_data_record_cases(data_record):
    return data_record.cases


def sort_data_record_deaths(data_record):
    return data_record.deaths


def sort_data(settings, data):
    reverse = False if settings.sort_order == "ascending" else True
    if settings.sort_type:
        if settings.sort_type == "date":
            return sorted(data, key=sort_data_record_date, reverse=reverse)
        if settings.sort_type == "cases":
            return sorted(data, key=sort_data_record_cases, reverse=reverse)
        if settings.sort_type == "deaths":
            return sorted(data, key=sort_data_record_deaths, reverse=reverse)


def get_all_valid_records(records, settings):
    sum = 0
    all_valid_records = []
    for record in records:
        valid_record = record.is_valid(settings)

        if valid_record:
            all_valid_records.append(record)
            if settings.total:
                if settings.type == "deaths":
                    sum += record.get_deaths()
                else:
                    sum += record.get_cases()

    if settings.sort_type:
        all_valid_records = sort_data(settings, all_valid_records)

    return all_valid_records, sum


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
            messagebox.showerror("Error", "Brak ustawien w pliku!")
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
