import tkinter as tk
from datetime import datetime
from tkcalendar import DateEntry
from tkinter import ttk, simpledialog, messagebox
from helpers.file_parser import load_file
from helpers.data_record import Settings, get_all_valid_records
from helpers.logger import msg_logger
import configparser
import os

DEFAULT_TITLE = "list9"
DEFAULT_CONFIG_FILE = "conf.ini"


def create_popup_window(title, prompt):
    return simpledialog.askstring(title=title, prompt=prompt)


class App:
    def __init__(self):
        msg_logger.init_logger()

        self.__records = []
        self.__countries = []
        self.__continents = []
        self.__checkboxes = {}
        self.__total_switch = False
        self.__total_container = []
        self.__sorting_switch = False
        self.__sorting_container = []
        self.__sorting_order_container = []
        self.__valid_records = None
        self.__data_file_path = None
        self.__create_main_window()
        self.__load_config_file(DEFAULT_CONFIG_FILE)

    def __del__(self):
        msg_logger.cleanup_logger()

    def run(self):
        self.__root.mainloop()

    # Other
    def __load_config_file(self, path):
        config = configparser.ConfigParser()
        config_args = config.read(path)

        if not config_args:
            messagebox.showerror("Uwaga", "Nie znaleziono pliku konfiguracyjnego!")
            return

        try:
            self.__root.geometry(
                f"{config['Default']['window_x_size']}x{config['Default']['window_y_size']}+50+50"
            )
            self.__date_begin.set_date(
                datetime.strptime(config["Default"]["date_begin"], "%Y-%m-%d")
            )
            self.__date_end.set_date(
                datetime.strptime(config["Default"]["date_end"], "%Y-%m-%d")
            )

            self.__load_covid_file(config["Default"]["data_file"])
        except:
            messagebox.showerror(
                "Error", f"Blad podczas ladowania pliku konfiguracyjnego: {path}"
            )

    def __clear_text_area(self):
        self.__text_area.delete("1.0", tk.END)

    def __save_data_from_text_area(self):
        if not self.__valid_records:
            messagebox.showerror("Error", "Brak danych w polu!")
            return

        file_path = create_popup_window("Zapisz do pliku", "Nazwa")
        try:
            with open(file_path, "w") as file:
                for record in self.__valid_records:
                    file.write(str(record) + "\n")
        except:
            messagebox.showerror(
                "Error", f"Nie udalo sie zapisac danych do pliku {file_path}"
            )
            return
        messagebox.showinfo("Sukces", "Plik zostal pomyslnie zapisany")

    def __update_statusbar(self, text):
        self.statusbar.config(text=text)
        self.statusbar.after(5000, self.__clearStatusBar)

    def __clearStatusBar(self):
        self.statusbar["text"] = ""

    def __update_comboboxes_values(self):
        self.__comboboxes["Country"]["values"] = sorted(list(self.__countries))
        self.__comboboxes["Country"].set(next(iter(self.__countries)))
        self.__comboboxes["Continent"]["values"] = sorted(list(self.__continents))
        self.__comboboxes["Continent"].set(next(iter(self.__continents)))

        settings = self.__gather_settings()
        output_data = get_all_valid_records(self.__records, settings)
        self.__valid_records = output_data[0]

        str_out = ""
        for record in self.__valid_records:
            str_out += str(record) + "\n"

        self.__text_area.delete("1.0", tk.END)
        self.__text_area.insert(tk.END, str_out)

        if settings.total:
            self.__update_total_area(output_data[1])
        self.__update_statusbar("Sukces")

    def __gather_settings(self):
        settings = Settings()

        if self.__checkboxes["Country"].get():
            settings.country = self.__comboboxes["Country"].get().lower()
        if self.__checkboxes["Continent"].get():
            settings.continent = self.__comboboxes["Continent"].get().lower()
        if self.__single_day_var.get():
            settings.day = self.__day_picker.get_date().day
        if self.__checkboxes["Sorting"].get():
            settings.sort_type = self.__sorting_var.get().lower() if not "" else None
            settings.sort_order = self.__sorting_order_var.get().lower()
        if self.__checkboxes["Type"].get():
            settings.total = True
            settings.type = self.__total_var.get().lower()

        settings.date_begin = self.__convert_date_to_datetime(
            self.__date_begin.get_date()
        )
        settings.date_end = self.__convert_date_to_datetime(self.__date_end.get_date())

        return settings

    def __update_total_area(self, value):
        self.__total_label.config(text=f"Total: {value}")

    def __show_valid_data(self):
        self.__update_statusbar("Przetwarzanie")
        if not self.__records:
            messagebox.showerror("Error", "Nie zaladowano pliku!")
            return

    def __on_close(self):
        if messagebox.askokcancel("Zakoncz", "Czy jestes pewny ze chcesz zakonczyc?"):
            self.__root.destroy()

    def __convert_date_to_datetime(self, date):
        return datetime(date.year, date.month, date.day)

    def __save_config_to_file(self, path):
        config = configparser.ConfigParser()
        config["Default"] = {}
        config["Default"]["window_x_size"] = str(self.__root.winfo_width())
        config["Default"]["window_y_size"] = str(self.__root.winfo_height())
        config["Default"]["date_begin"] = str(self.__date_begin.get_date())
        config["Default"]["date_end"] = str(self.__date_end.get_date())
        config["Default"]["data_file"] = str(self.__data_file_path)
        self.__update_statusbar("Zapisywanie")
        with open(path, "w") as confile:
            config.write(confile)
        self.__update_statusbar("Sukces")

    # All UI commands
    def __add_status_bar(self, text):
        self.statusbar = tk.Label(self.__root, text=text, anchor=tk.W)
        self.statusbar.after(5000, self.__clearStatusBar)
        self.statusbar.grid(row=4, column=0, columnspan=2, sticky=tk.EW)
        pass

    def __set_log_file(self):
        file_path = create_popup_window("Ustaw plik loggera", "Nazwa")
        msg_logger.set_logger_file(file_path)

    def __load_covid_file(self, file_path=None):
        self.__update_statusbar("Ladowanie pliku")

        if not file_path:
            file_path = create_popup_window("Zaladuj plik z danymi", "Nazwa")

        return_tuple = load_file(file_path)
        self.__data_file_path = file_path

        if return_tuple:
            self.__records = return_tuple[0]
            self.__countries = return_tuple[1]
            self.__continents = return_tuple[2]
            self.__update_comboboxes_values()
            messagebox.showinfo("Sukces", f"Pomyslnie zaladowano plik {file_path}")
            self.__update_statusbar("Sukces")
        else:
            messagebox.showerror(
                "Blad",
                f"Niepowodzenie podczas ladowania pliku: {file_path}, plik nie istnieje.",
            )
            self.__update_statusbar("Niepowodzenie")

    def __load_config(self):
        file_path = create_popup_window("Wczytaj plik", "Nazwa")
        try:
            self.__load_config_file(file_path)
            messagebox.showinfo("Sukces", f"Plik zaladowany! {file_path}")
        except:
            messagebox.showerror(
                "Error", f"Nie udalo sie zaladowac pliku konfiguracyjnego: {file_path}"
            )

    def __save_config(self):
        try:
            file_path = create_popup_window("Zapisz plik", "Nazwa")
            self.__save_config_to_file(file_path)
            messagebox.showinfo("Sukces", f"Plik zapisany! {file_path}")
        except:
            messagebox.showerror(
                "Error", f"Nie udalo sie zapisac pliku konfiguracyjnego: {file_path}"
            )

    def __toggle_total_switch(self):
        self.__total_switch = not self.__total_switch
        for button in self.__total_container:
            button["state"] = "!disabled" if self.__total_switch else "disabled"

    def __toggle_country_switch(self):
        self.__country_switch = not self.__country_switch
        if "Country" in self.__comboboxes:
            self.__comboboxes["Country"]["state"] = (
                "readonly" if self.__country_switch else "disabled"
            )

    def __toggle_sort_switch(self):
        self.__sorting_switch = not self.__sorting_switch
        for sorting_opt in self.__sorting_container:
            sorting_opt["state"] = "!disabled" if self.__sorting_switch else "disabled"

        for sorting_ord_opt in self.__sorting_order_container:
            sorting_ord_opt["state"] = (
                "!disabled" if self.__sorting_switch else "disabled"
            )

    def __toggle_continent_switch(self):
        self.__continent_switch = not self.__continent_switch
        if "Continent" in self.__comboboxes:
            self.__comboboxes["Continent"]["state"] = (
                "readonly" if self.__continent_switch else "disabled"
            )

    def __toggle_single_day(self):
        if self.__single_day_var.get():
            self.__day_picker["state"] = "!disabled"
        else:
            self.__day_picker["state"] = "disabled"

    # All add UI functions
    def __create_main_window(self, title=DEFAULT_TITLE):
        self.__root = tk.Tk()
        self.__root.title(title)
        self.__comboboxes = {}
        self.__toolbar_frame = ttk.Frame(self.__root)
        self.__toolbar_frame.grid(column=0, row=0, sticky="w")
        self.__buttons_frame = ttk.Frame(self.__root)
        self.__buttons_frame.grid(column=0, row=1)
        self.__buttons_frame["borderwidth"] = 2
        self.__buttons_frame["padding"] = 5
        self.__buttons_frame["relief"] = "groove"
        self.__ui_frame = ttk.Frame(self.__root)
        self.__ui_frame.grid(column=0, row=2)
        self.__ui_frame["borderwidth"] = 2
        self.__ui_frame["padding"] = 5
        self.__ui_frame["relief"] = "groove"
        self.__sorting_var = tk.StringVar()
        self.__total_var = tk.StringVar()
        self.__sorting_order_var = tk.StringVar()
        self.__text_frame = ttk.Frame(self.__root)
        self.__text_frame["borderwidth"] = 2
        self.__text_frame["padding"] = 5
        self.__text_frame["relief"] = "groove"
        self.__text_frame.grid(column=0, row=3)
        self.__add_all_buttons(self.__buttons_frame)
        self.__add_all_date_pickers(self.__ui_frame)
        self.__add_all_comboboxes(self.__ui_frame)
        self.__add_all_radio_buttons(self.__ui_frame)
        self.__add_text_area(self.__text_frame)
        self.__add_total_area(self.__ui_frame)
        self.__add_menu()
        self.__add_status_bar("Linia statusu")
        self.__add_toolbar(self.__toolbar_frame)
        self.__root.protocol("WM_DELETE_WINDOW", self.__on_close)

    def __add_menu(self):
        self.__menubar = tk.Menu(self.__root)
        self.__root.config(menu=self.__menubar)
        self.__add_file_menu()

    def __add_file_menu(self):
        file_menu = tk.Menu(self.__menubar)
        self.__menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Load config", command=self.__load_config)
        file_menu.add_command(label="Save config", command=self.__save_config)

    def __add_total_area(self, parent):
        self.__total_label = tk.Label(parent, text="Total: 0")
        self.__total_label.grid(column=4, row=4)

    def __add_text_area(self, parent):
        self.__text_area = tk.Text(parent, width=110, height=20)
        self.__text_scrollbar = tk.Scrollbar(parent)
        self.__text_scrollbar.pack(side=tk.RIGHT)
        self.__text_area.pack(side=tk.LEFT)

    def __add_all_date_pickers(self, parent):
        self.__date_begin = self.__add_date_picker_widget(parent, "Date begin", 2019)
        self.__date_end = self.__add_date_picker_widget(
            parent, "Date end", 2021, column=0, row=1
        )

        self.__single_day_var = tk.IntVar()
        self.__single_day_checkbox = tk.Checkbutton(
            parent,
            text="Single day",
            command=self.__toggle_single_day,
            variable=self.__single_day_var,
        )
        self.__single_day_checkbox.grid(column=0, row=5)
        self.__day_picker = self.__add_date_picker_widget(
            parent, "", 2020, column=0, row=5
        )
        self.__day_picker["state"] = "disabled"

    def __add_all_comboboxes(self, parent):
        self.__country_switch = False
        self.__checkboxes["Country"] = self.__add_dropdown_list_widget_with_checkbox(
            parent,
            "Country",
            self.__toggle_country_switch,
            self.__countries,
            column=2,
            row=0,
        )

        self.__continent_switch = False
        self.__checkboxes["Continent"] = self.__add_dropdown_list_widget_with_checkbox(
            parent,
            "Continent",
            self.__toggle_continent_switch,
            self.__continents,
            column=2,
            row=1,
        )

    def __add_all_buttons(self, parent):
        button_load_file = tk.Button(
            parent, text="Load file", command=self.__load_covid_file
        )
        button_load_file.grid(column=0, row=0)

        button_set_log_file = tk.Button(
            parent, text="Set log file", command=self.__set_log_file
        )
        button_set_log_file.grid(column=1, row=0)

        button_show = tk.Button(
            parent, text="Show valid data", command=self.__show_valid_data
        )
        button_show.grid(column=2, row=0)

    def __add_all_radio_buttons(self, parent):
        self.__checkboxes["Type"] = self.__add_radio_button(
            parent,
            "Value types",
            ["Deaths", "Cases"],
            self.__total_var,
            self.__total_container,
            self.__toggle_total_switch,
            column=0,
            row=2,
        )
        self.__total_var.set("Deaths")

        self.__checkboxes["Sorting"] = self.__add_radio_button(
            parent,
            "Sorting",
            ["Date", "Deaths", "Cases"],
            self.__sorting_var,
            self.__sorting_container,
            self.__toggle_sort_switch,
            column=2,
            row=2,
            padding=0,
        )
        self.__sorting_var.set("Date")

        self.__add_radio_without_checkbox(
            parent,
            ["Ascending", "Descending"],
            self.__sorting_order_var,
            self.__sorting_order_container,
            column=3,
            row=5,
            padding=20,
        )
        self.__sorting_order_var.set("Ascending")

    def __add_radio_button(
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
        temp_var = tk.IntVar()
        checkbox = ttk.Checkbutton(
            parent, text=label, command=command, variable=temp_var
        )
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

        return temp_var

    def __add_radio_without_checkbox(
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

    def __add_date_picker_widget(self, parent, title, year, column=0, row=0):
        labelText = tk.StringVar()
        labelText.set(title)
        label = tk.Label(parent, textvariable=labelText, height=1)
        label.grid(column=column, row=row, sticky="w")
        cal = DateEntry(parent, width=10, bg="darkblue", fg="white", year=year)
        cal.grid(column=column + 1, row=row)

        return cal

    def __add_dropdown_list_widget_with_checkbox(
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
        return temp_var

    def __add_toolbar(self, parent):
        self.toolbar_images = []  # musz?? by?? pami??tane stale
        self.toolbar = tk.Frame(parent)
        for image, command in (
            ("images/editdelete.gif", self.__clear_text_area),
            ("images/filesave.gif", self.__save_data_from_text_area),
            ("images/editadd.gif", self.__load_covid_file),
            ("images/fileexport.gif", self.__set_log_file),
            ("images/editedit.gif", self.__show_valid_data),
        ):
            image = os.path.join(os.path.dirname(__file__), image)
            try:
                image = tk.PhotoImage(file=image)
                self.toolbar_images.append(image)
                button = tk.Button(self.toolbar, image=image, command=command)
                button.grid(row=0, column=len(self.toolbar_images) - 1, sticky=tk.W)
            except tk.TclError as err:
                messagebox.showerror(
                    "Error",
                    f"Blad przy ladowaniu tekstur, program moze nie dzialac poprawnie!",
                )
        self.toolbar.grid(row=0, column=0, columnspan=2, sticky=tk.W)
