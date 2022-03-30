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
    values = []
    for line in sys.stdin:
        for var in line.split():
            try:
                values.append(float(var))
            except ValueError:
                pass

    if len(values) > 0:
        step = values[0]
        values.pop(0)
        print(step)
        print(values)
        print(calculate_moving_averages(values, step))


if __name__ == "__main__":
    main()
