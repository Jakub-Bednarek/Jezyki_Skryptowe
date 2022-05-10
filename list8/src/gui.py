from tabnanny import check
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext, simpledialog
from logger import msg_logger, log_info

commands_queue = []
new_command_callback = None
load_file_callback = None
check_actions_callback = None


def set_check_actions_callback(command):
    global check_actions_callback
    check_actions_callback = command


def set_load_file_callback(command):
    global load_file_callback
    load_file_callback = command


def set_new_command_callback(command):
    global new_command_callback
    new_command_callback = command


def set_log_file():
    file_name = create_popup_window("Ustawi plik do logow", "Nazwa")
    msg_logger.set_logger_file(file_name)


def load_file_command():
    file_name = create_popup_window("Zaladuj plik z danymi", "Nazwa")
    if load_file_callback and file_name and file_name != "":
        load_file_callback(file_name, 1)


def get_new_command():
    command = create_popup_window("Dodawanie nowej komendy", "Komenda")
    if new_command_callback and command != "":
        new_command_callback(command)
    else:
        log_info(f"Provided cmd is empty!")
        return
    check_actions_callback()


def create_popup_window(title, prompt):
    return simpledialog.askstring(title=title, prompt=prompt)


class GUI:
    def create_gui(self):
        self.__root = tk.Tk()
        frm = ttk.Frame(self.__root)
        self.__text_area = scrolledtext.ScrolledText(
            self.__root, wrap=tk.WORD, width=100, height=40, font=("Times New Roman", 8)
        )
        self.__text_area.grid(column=0, row=0)
        frm.grid(column=1, row=0)
        ttk.Button(frm, text="Load data file", command=load_file_command).grid(
            column=0, row=0
        )
        ttk.Button(frm, text="Set log file", command=set_log_file).grid(column=0, row=1)
        ttk.Button(frm, text="Add command", command=get_new_command).grid(
            column=0, row=2
        )

    def run(self):
        self.create_gui()
        self.__root.mainloop()

    def add_text_to_main_area(self, data):
        self.__text_area.delete("0.0", tk.END)
        for record in data:
            self.__text_area.insert(tk.END, f"{record}\n")
