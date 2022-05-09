from app import App
import sys


def check_if_show_gui():
    args = sys.argv

    for arg in args:
        if arg == "-g":
            return True

    return False


def main():
    app = App(check_if_show_gui())
    app.run()


if __name__ == "__main__":
    main()
