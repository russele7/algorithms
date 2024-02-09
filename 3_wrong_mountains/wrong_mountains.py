import sys


def main():

    def valid_mountain_array(data):

        len_data = len(data)
        if len_data <= 2:
            return False
        elif data[0] >= data[1]:
            return False

        up_flg = True
        cursor = -1
        while up_flg:
            cursor += 1

            if data[cursor] > data[cursor + 1]:
                up_flg = False

            elif (
                (data[cursor] == data[cursor + 1])
                or (cursor == len_data - 2)
            ):
                return False

        while cursor < len_data - 2:
            cursor += 1
            if (data[cursor] <= data[cursor + 1]):
                return False

        return True

    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    print(valid_mountain_array(arr))


if __name__ == '__main__':
    main()
