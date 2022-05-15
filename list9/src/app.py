import tkinter as tk
from tkcalendar import Calendar, DateEntry

DEFAULT_TITLE = "list9"


class App:
    def __init__(self):
        self.create_main_window()

    def run(self):
        self.__root.mainloop()

    def create_main_window(self, title=DEFAULT_TITLE):
        self.__root = tk.Tk()
        self.__root.title(title)
        self.add_date_picker_widget(self.__root, "Date begin")
        self.add_date_picker_widget(self.__root, "Date end", column=0, row=1)

    def add_date_picker_widget(self, parent, title, column=0, row=0):
        labelText = tk.StringVar()
        labelText.set(title)
        label = tk.Label(parent, textvariable=labelText, height=1)
        label.grid(column=column, row=row)
        cal = DateEntry(parent, width=10, bg="darkblue", fg="white", year=2020)
        cal.grid(column=column + 1, row=row)
