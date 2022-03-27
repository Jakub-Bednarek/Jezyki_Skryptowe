import math
import sys

def check_pi_precision(precision):
    pi_str = str(math.pi)
    current_pi_index = 0
    n = 1.0
    sum = 1.0
    while current_pi_index <= precision:
        val = (2 * n) * (2 * n) / ((2 * n - 1) * (2 * n + 1))
        n += 1
        sum *= val
        sum_str = str(sum * 2)
        if sum_str[current_pi_index] == pi_str[current_pi_index]:
            current_pi_index += 1
    
    return n

def main():
    if len(sys.argv) > 1: 
        precision = int(sys.argv[1])
        print(check_pi_precision(precision))
    

if __name__ == "__main__":
    main()