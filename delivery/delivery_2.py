import sys
# Успешная попытка ID 103511133


def read_data():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def read_limit():
    return int(sys.stdin.readline().rstrip())


def pares_count(input_weights: list, limit: int):

    if len(input_weights) == 1:
        return 1

    weights = sorted(input_weights)
    counter = 0

    left_idx = 0
    right_idx = len(weights) - 1

    while left_idx <= right_idx:
        if weights[left_idx] + weights[right_idx] <= limit:
            left_idx += 1

        counter += 1
        right_idx -= 1

    return counter


def main():

    data = read_data()
    limit = read_limit()

    print(pares_count(data, limit))


if __name__ == '__main__':
    main()
