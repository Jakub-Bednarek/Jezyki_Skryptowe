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
        self.__total_switch = False
        self.__total_container = []
        self.__sorting_switch = False
        self.__sorting_container = []
        self.__sorting_order_container = []
        self.create_main_window()

    def __del__(self):
        msg_logger.cleanup_logger()

    def run(self):
        self.__root.mainloop()

    def load_file(self):
        file_path = create_popup_window("Zaladuj plik z danymi", "Nazwa")
        return_tuple = load_file(file_path)

        if return_tuple:
            self.__records = return_tuple[0]
            self.__countries = return_tuple[1]
            self.__continents = return_tuple[2]
            self.update_comboboxes_values()

    def update_comboboxes_values(self):
        self.__comboboxes["Country"]["values"] = sorted(list(self.__countries))
        self.__comboboxes["Country"].set(next(iter(self.__countries)))
        self.__comboboxes["Continent"]["values"] = sorted(list(self.__continents))
        self.__comboboxes["Continent"].set(next(iter(self.__continents)))

    def set_log_file(self):
        file_path = create_popup_window("Ustaw plik loggera", "Nazwa")
        msg_logger.set_logger_file(file_path)

    def show_valid_data(self):
        print("SHOWING DATA")

    def toggle_total_switch(self):
        self.__total_switch = not self.__total_switch
        for button in self.__total_container:
            button["state"] = "!disabled" if self.__total_switch else "disabled"

    def toggle_country_switch(self):
        self.__country_switch = not self.__country_switch
        if "Country" in self.__comboboxes:
            self.__comboboxes["Country"]["state"] = (
                "readonly" if self.__country_switch else "disabled"
            )

    def toggle_sort_switch(self):
        self.__sorting_switch = not self.__sorting_switch
        for sorting_opt in self.__sorting_container:
            sorting_opt["state"] = "!disabled" if self.__sorting_switch else "disabled"

        for sorting_ord_opt in self.__sorting_order_container:
            sorting_ord_opt["state"] = (
                "!disabled" if self.__sorting_switch else "disabled"
            )

    def toggle_continent_switch(self):
        self.__continent_switch = not self.__continent_switch
        if "Continent" in self.__comboboxes:
            self.__comboboxes["Continent"]["state"] = (
                "readonly" if self.__continent_switch else "disabled"
            )

    def toggle_single_day(self):
        if self.__single_day_var.get():
            self.__day_picker["state"] = "!disabled"
        else:
            self.__day_picker["state"] = "disabled"

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
        self.__ui_frame["borderwidth"] = 2
        self.__ui_frame["padding"] = 5
        self.__ui_frame["relief"] = "groove"
        self.__sorting_var = tk.StringVar()
        self.__total_var = tk.StringVar()
        self.__sorting_order_var = tk.StringVar()
        self.add_all_buttons(self.__buttons_frame)
        self.add_all_date_pickers(self.__ui_frame)
        self.add_all_comboboxes(self.__ui_frame)
        self.add_all_radio_buttons(self.__ui_frame)

    def add_all_date_pickers(self, parent):
        self.add_date_picker_widget(parent, "Date begin")
        self.add_date_picker_widget(parent, "Date end", column=0, row=1)

        self.__single_day_var = tk.IntVar()
        single_day_checkbox = tk.Checkbutton(
            parent,
            text="Single day",
            command=self.toggle_single_day,
            variable=self.__single_day_var,
        )
        single_day_checkbox.grid(column=0, row=5)
        self.__day_picker = self.add_date_picker_widget(parent, "", column=0, row=5)
        self.__day_picker["state"] = "disabled"

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

        button_show = tk.Button(
            parent, text="Show valid data", command=self.show_valid_data
        )
        button_show.grid(column=2, row=0)

    def add_all_radio_buttons(self, parent):
        self.add_radio_button(
            parent,
            "Value types",
            ["Deaths", "Cases"],
            self.__total_var,
            self.__total_container,
            self.toggle_total_switch,
            column=0,
            row=2,
        )

        self.add_radio_button(
            parent,
            "Sorting",
            ["Date", "Deaths", "Cases"],
            self.__sorting_var,
            self.__sorting_container,
            self.toggle_sort_switch,
            column=2,
            row=2,
            padding=0,
        )

        self.add_radio_without_checkbox(
            parent,
            ["Ascending", "Descending"],
            self.__sorting_order_var,
            self.__sorting_order_container,
            column=3,
            row=5,
            padding=20,
        )

    def add_radio_button(
        self,
        parent,
        label,
        options,
        var,
        storage,
        command,
        column=0,
        row=0,
        padding=0,
        sticky="w",
    ):
        checkbox = ttk.Checkbutton(parent, text=label, command=command)
        checkbox.grid(column=column, row=row, sticky=sticky)
        column += 1
        for i in range(0, len(options)):
            button = ttk.Radiobutton(
                parent, text=options[i], variable=var, value=options[i]
            )
            button.grid(column=column, row=row + i, sticky=sticky)
            button["state"] = "disabled"
            button["padding"] = padding
            storage.append(button)

    def add_radio_without_checkbox(
        self, parent, options, var, storage, column=0, row=0, padding=0
    ):
        for i in range(0, len(options)):
            button = ttk.Radiobutton(
                parent, text=options[i], variable=var, value=options[i]
            )
            button.grid(column=column, row=row + i, sticky="w")
            button["state"] = "disabled"
            if i == 0:
                button["padding"] = (0, padding, 0, 0)
            storage.append(button)

    def add_date_picker_widget(self, parent, title, column=0, row=0):
        labelText = tk.StringVar()
        labelText.set(title)
        label = tk.Label(parent, textvariable=labelText, height=1)
        label.grid(column=column, row=row, sticky="w")
        cal = DateEntry(parent, width=10, bg="darkblue", fg="white", year=2020)
        cal.grid(column=column + 1, row=row)

        return cal

    def add_dropdown_list_widget_with_checkbox(
        self, parent, title, command, values, column=0, row=0
    ):
        temp_var = tk.IntVar()
        checkbutton = tk.Checkbutton(
            parent, text=title, command=command, variable=temp_var
        )
        checkbutton.grid(column=column, row=row, sticky="w")

        current_var = tk.StringVar()
        combobox = ttk.Combobox(parent, textvariable=current_var)
        combobox["values"] = values
        combobox["state"] = "disabled"
        combobox.grid(column=column + 1, row=row)
        self.__comboboxes[title] = combobox
