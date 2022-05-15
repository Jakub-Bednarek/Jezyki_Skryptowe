import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk, simpledialog
from helpers.file_parser import load_file
from helpers.logger import msg_logger

DEFAULT_TITLE = "list9"


def create_popup_window(title, prompt):
    return simpledialog.askstring(title=title, prompt=prompt)


class App:
    def __init__(self):
        msg_logger.init_logger()

        self.__records = []
        self.__countries = []
        self.__continents = []
        self.create_main_window()

    def __del__(self):
        msg_logger.cleanup_logger()

    def run(self):
        self.__root.mainloop()

    def load_file(self):
        file_path = create_popup_window("Zaladuj plik z danymi", "Nazwa")
        self.__records, self.__countries, self.__continents = (
            load_file(file_path) if not None else None,
            None,
            None,
        )

    def set_log_file(self):
        file_path = create_popup_window("Ustaw plik loggera", "Nazwa")
        msg_logger.set_logger_file(file_path)

    def toggle_country_switch(self):
        self.__country_switch = not self.__country_switch
        if "Country" in self.__comboboxes:
            self.__comboboxes["Country"]["state"] = (
                "readonly" if self.__country_switch else "disabled"
            )

    def toggle_continent_switch(self):
        self.__continent_switch = not self.__continent_switch
        if "Continent" in self.__comboboxes:
            self.__comboboxes["Continent"]["state"] = (
                "readonly" if self.__continent_switch else "disabled"
            )

    def create_main_window(self, title=DEFAULT_TITLE):
        self.__root = tk.Tk()
        self.__root.title(title)
        self.__comboboxes = {}
        self.__buttons_frame = ttk.Frame(self.__root)
        self.__buttons_frame.grid(column=0, row=0)
        self.__buttons_frame["borderwidth"] = 2
        self.__buttons_frame["padding"] = 5
        self.__buttons_frame["relief"] = "groove"
        self.__ui_frame = ttk.Frame(self.__root)
        self.__ui_frame.grid(column=0, row=1)
        self.add_all_buttons(self.__buttons_frame)
        self.add_all_date_pickers(self.__ui_frame)
        self.add_all_comboboxes(self.__ui_frame)

    def add_all_date_pickers(self, parent):
        self.add_date_picker_widget(parent, "Date begin")
        self.add_date_picker_widget(parent, "Date end", column=0, row=1)

    def add_all_comboboxes(self, parent):
        self.__country_switch = False
        self.add_dropdown_list_widget_with_checkbox(
            parent,
            "Country",
            self.toggle_country_switch,
            self.__countries,
            column=2,
            row=0,
        )

        self.__continent_switch = False
        self.add_dropdown_list_widget_with_checkbox(
            parent,
            "Continent",
            self.toggle_continent_switch,
            self.__continents,
            column=2,
            row=1,
        )

    def add_all_buttons(self, parent):
        button_load_file = tk.Button(parent, text="Load file", command=self.load_file)
        button_load_file.grid(column=0, row=0)

        button_set_log_file = tk.Button(
            parent, text="Set log file", command=self.set_log_file
        )
        button_set_log_file.grid(column=1, row=0)

    def add_date_picker_widget(self, parent, title, column=0, row=0):
        labelText = tk.StringVar()
        labelText.set(title)
        label = tk.Label(parent, textvariable=labelText, height=1)
        label.grid(column=column, row=row)
        cal = DateEntry(parent, width=10, bg="darkblue", fg="white", year=2020)
        cal.grid(column=column + 1, row=row)

    def add_dropdown_list_widget_with_checkbox(
        self, parent, title, command, values, column=0, row=0
    ):
        checkbutton = tk.Checkbutton(
            parent,
            text=title,
            command=command,
        )
        checkbutton.grid(column=column, row=row)

        current_var = tk.StringVar()
        combobox = ttk.Combobox(parent, textvariable=current_var)
        combobox["values"] = values
        combobox["state"] = "disabled"
        combobox.grid(column=column + 1, row=row)
        self.__comboboxes[title] = combobox
