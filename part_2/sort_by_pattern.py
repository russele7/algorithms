import sys


def read_arrsize():
    return int(sys.stdin.readline().rstrip())


def read_arr():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def sort_by_pattern(arr: list, pattern: list):
    # Создаем результат по паттерну
    counter = 0
    for p in pattern:
        for i, a in enumerate(arr):
            if a == p:
                cur = arr.pop(i)
                arr.insert(counter, cur)
                counter += 1

    # сортируем остаток
    arr = arr[:counter] + sorted(arr[counter:])

    return arr


def main():

    # n = read_arrsize()
    # arr = read_arr()

    # k = read_arrsize()
    # pattern = read_arr()

    n = 11
    arr = [2, 4, 3, 5, 6, 0, 9, 8, 7, 7]

    k = 6
    pattern = [2, 4, 3, 5, 6, 0]

    print(' '.join(list(map(str, sort_by_pattern(arr, pattern)))))


if __name__ == '__main__':
    main()
