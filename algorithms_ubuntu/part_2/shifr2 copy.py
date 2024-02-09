import sys
from string import digits
# ID


def read_data():
    return sys.stdin.readline().rstrip()


def find_right_break(stroka: str, left_break_idx: int):
    marker = 1
    for i in range(left_break_idx+1, len(stroka)):
        if marker == 0:
            return i
        elif stroka[i] == '[':
            marker += 1
        elif stroka[i] == ']':
            marker -= 1


def decipher(stroka: str):
    if '[' not in stroka:
        return stroka

    for i, c in enumerate(stroka):
        if c in digits:
            digit_idx = i
            break

    left_break_idx = stroka.find('[')

    right_break_idx = find_right_break(stroka, left_break_idx)

    return (
        stroka[:digit_idx]
        + (
            int(stroka[digit_idx:left_break_idx])
            * decipher(stroka[left_break_idx+1:right_break_idx])
        ) + decipher(stroka[right_break_idx+1:])
    )


def main():
    print(decipher(read_data()))


if __name__ == '__main__':
    main()
