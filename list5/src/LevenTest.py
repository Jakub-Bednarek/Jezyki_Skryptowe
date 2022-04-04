from ast import arg
import Leven
import sys

def main():
    print(Leven.LevSim(sys.argv[1], sys.argv[2]))
    
if __name__ == "__main__":
    main()