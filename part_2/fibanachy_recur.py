import sys


def fibanachi(n):
    if n < 2:
        return 1

    return fibanachi(n - 1) + fibanachi(n - 2)


def main():
    num = int(sys.stdin.readline().rstrip())
    print(fibanachi(num))


if __name__ == '__main__':
    main()
