from re import sub
import sys

def calculate_moving_averages(values, move):
    subsum = sum(values[0:move])
    if len(values) <= move:
        return [subsum / len(values)]
    
    result = [subsum / move]
    for i in range(move - 1, len(values) - (move - 1)):
        subsum -= values[i - 1]
        subsum += values[i + move - 1]
        result.append(subsum / move)
    
    return result

def main():
    try:
        step = int(sys.argv[1])
        values = list(map(float, sys.argv[2:]))
    except (ValueError, IndexError):
        print("Nieprawidlowe dane wejsciowe")
        return

    print(calculate_moving_averages(values, step))

if __name__ == "__main__":
    main()