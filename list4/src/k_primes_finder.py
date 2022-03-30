import sys
from prime_finder import get_next_prime


def calculate_k_next_primes(start_value, count):
    k_next_primes = []
    next_prime = start_value

    for i in range(count):
        next_prime = get_next_prime(next_prime)
        k_next_primes.append(next_prime)

    return k_next_primes


def main():
    try:
        start_value, count = map(int, input().split())
    except (ValueError, IndexError):
        print("Nieprawidlowe dane wejsciowe")
        return

    print(calculate_k_next_primes(start_value, count))


if __name__ == "__main__":
    main()
