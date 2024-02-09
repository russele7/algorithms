import sys


def fibanachi(number):

    if number < 2:
        return 1

    fib1, fib2 = 1, 1

    for _ in range(number - 1):
        fib1, fib2 = fib2, fib1 + fib2

    return fib2


def main():
    num = int(sys.stdin.readline().rstrip())
    print(fibanachi(num))


if __name__ == '__main__':
    main()
