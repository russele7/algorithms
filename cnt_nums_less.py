import sys


def main():

    nums = list(map(int, sys.stdin.readline().rstrip().split()))

    def func(data):
        len_nums = len(data)
        result = [None] * len_nums

        for i, val in enumerate(data):
            counter = 0
            for comp in data[:i] + data[i+1:]:
                if comp < val:
                    counter += 1
            result[i] = counter

        return ' '.join(str(item) for item in result)

    print(func(nums))


if __name__ == '__main__':
    main()
