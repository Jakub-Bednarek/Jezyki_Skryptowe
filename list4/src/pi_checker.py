import math
import sys


def check_pi_precision(precision):
    pi_str = str(math.pi)
    current_pi_index = 0
    n = 1.0
    current_sum = 1.0
    while current_pi_index <= precision:
        current_sum *= (2 * n) * (2 * n) / ((2 * n - 1) * (2 * n + 1))
        n += 1
        sum_str = str(current_sum * 2)
        if sum_str[current_pi_index] == pi_str[current_pi_index]:
            current_pi_index += 1
    
    return int(n)


def main():
    try:
        precision = int(input())
    except (ValueError, IndexError):
        print("Nieprawidlowe dane wejsciowe")
        return
    
    print(check_pi_precision(precision))
    

if __name__ == "__main__":
    main()
