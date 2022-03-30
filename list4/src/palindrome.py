import sys


def main():
    for line in sys.stdin:
        line = line.replace(" ", "").strip()
        if line != line[::-1]:
            print("False")
        else:
            print("True")


if __name__ == "__main__":
    main()
