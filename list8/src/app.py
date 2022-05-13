from task_request import TaskRequest
from helpers.logger import msg_logger, log_info
from console import get_integer, get_string, print_choice_menu
from helpers.data_record import (
    DataRecord,
    Settings,
    sort_data_record_cases,
    sort_data_record_date,
    sort_data_record_deaths,
)
from helpers.file_parser import load_file
from gui import (
    set_check_actions_callback,
    set_load_file_callback,
    set_new_command_callback,
)
import gui

"""
Jezyk zapytan:
Mamy dostep do 4 podstawowych komend: set, reset, show, exit

-reset: resetuje sekwencje zapisanych polecen
-show: pokazuje rezultaty na podstawie wprowadzonych wczesniej polecen
-exit: konczy prace programu
-set: sluzy do wprowadzania ustawien, mozemy tutaj wpisac dowolna kombinacje komend z grupy set

Grupa komend set:
-from [miesiac] [dzien] lub [data] - ustawia dolne kryterium daty do sprawdzania (Przyklad: "set from july 15" lub "set from 15.06.2020")
-to [miesiac] [dzien] lub [data] - ustawia gorne kryterium daty (Przyklad: "set to august 15" lub "set from 15.09.2020")
-type [cases] lub [deaths]: ustawia typ sumowania danych na smierci lub przpadki (Przyklad: "set type cases")
-total [true] lub [false]: ustawia nam sumowanie podanych przez komende type danych (Przyklad: "set total true")
-in [kraj] lub [kontynent]: ustawia wyszukiwanie rekordow dla konkretnego kraju badz kontynenty (Przyklad: "set in poland")
-on [numer_dnia]: ustawia nam wyszukiwanie dla konkretnego, pojedynczego dnia, nie wyklucza komend from oraz to (Przyklad: "set on 20")
-sort [typ_danych_do_sortowania] [kolejnosc]: ustawia sortowanie danych wg kryterium (dostepne: date, deaths, cases), oraz kolejnosc sortowania (ascending, descending)
(Przyklad: "set sort cases ascending")
"""


class App:
    def __init__(self, show_gui=False):
        self.__request = TaskRequest()
        self.__file_data = []
        self.__should_terminate = False
        self.__settings = None
        self.__gui = gui.GUI() if show_gui else None
        msg_logger.init_logger("Test.log")

        set_new_command_callback(self.__request.add_cmd)
        set_load_file_callback(self.load_data)
        set_check_actions_callback(self.check_for_actions)

        log_info("Initialized app")

    def load_data(self, file_path):
        records, countries, continents = (
            load_file(file_path) if not None else None,
            None,
            None,
        )

    def set_continents(self, continents):
        self.__request.set_continents(continents)

    def set_countries(self, countries):
        self.__request.set_countries(countries)

    def run(self):
        if not self.__gui:
            while not self.__should_terminate:
                print_choice_menu()
                self.get_input()
        else:
            self.__gui.run()
            log_info("Terminating app")

    def get_input(self):
        choice = get_integer("Choice")
        if choice == 1:
            file_path = get_string("File path")
            self.load_data(file_path)
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

    def get_valid_records(self):
        sum = 0
        valid_records = []
        log_info("Beginning data analysis.")
        for record in self.__file_data:
            if record and record.is_valid(self.__settings):
                valid_records.append(record)
                if self.__settings.type == "deaths":
                    sum += record.get_deaths()
                else:
                    sum += record.get_cases()

        if self.__settings.sort_type:
            valid_records = self.sort_data(valid_records)
        return valid_records

    def show_data(self):
        valid_records = self.get_valid_records()
        for record in valid_records:
            log_info(str(record))
        if self.__settings.total:
            log_info(f"Total value for {self.__settings.type}: {sum}")
        if self.__gui:
            self.__gui.add_text_to_main_area(valid_records)

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
