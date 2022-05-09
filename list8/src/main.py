from app import App
from console import print_choice_menu


def main():
    app = App()

    while not app.should_terminate():
        print_choice_menu()
        app.get_input()


if __name__ == "__main__":
    main()
