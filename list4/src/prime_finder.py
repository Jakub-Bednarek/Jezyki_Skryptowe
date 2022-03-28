import sys

def is_prime(number):
    if number <= 1: return False
    if number <= 3: return True
    if number % 2 == 0 or number % 3 == 0: return False
    
    i = 5
    while i * i < number:
        if number % i == 0 or number % (i + 2) == 0: return False
        i += 6
    
    return True

def get_next_prime(number):
    next_number = number + 1
    while not is_prime(next_number):
        next_number += 1
        
    return next_number

def main():
    for arg in sys.argv[1:]:
        try:
            next_prime = get_next_prime(int(arg))
            print(f"{arg} -> {next_prime}")
        except (ValueError, IndexError):
            pass
    
if __name__ == "__main__":
    main()