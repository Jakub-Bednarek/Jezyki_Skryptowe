from ast import arg
import sys

def main():
    arguments = sys.argv[1::]
    
    if arguments == [] or arguments != arguments[::-1]:
        print("False")
    else:
        print("True")
    
if __name__ == "__main__":
    main()