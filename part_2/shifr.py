import sys
from string import digits


def read_data():
    return sys.stdin.readline().rstrip()


def find_right_break(stroka: str, left_break_idx: int):
    marker = 1
    for i in range(left_break_idx+1, len(stroka)):
        if stroka[i] == '[':
            marker += 1
        elif stroka[i] == ']':
            marker -= 1

        if marker == 0:
            return i


def decipher(stroka: str):
    # если нет скобок, возвращаем строку
    if '[' not in stroka:
        return stroka

    # первая цифра
    for i, c in enumerate(stroka):
        if c in digits:
            digit_idx = i
            break
    # левая скобка
    left_break_idx = stroka.find('[')

    # правая скобка
    right_break_idx = find_right_break(stroka, left_break_idx)

    # берем левый центр и правый края

    # left = stroka[:digit_idx]
    # right = stroka[right_break_idx+1:]
    # multi = int(stroka[digit_idx:left_break_idx])
    # center = stroka[left_break_idx+1:right_break_idx]

    # return left + multi * decipher(center) + decipher(right)

    return (
        stroka[:digit_idx]
        + (
            int(stroka[digit_idx:left_break_idx])
            * decipher(stroka[left_break_idx+1:right_break_idx])
        ) + decipher(stroka[right_break_idx+1:])
    )


def main():
    # command = read_data()
    # command = '2[abc]3[cd]ef'
    print(decipher(read_data()))


if __name__ == '__main__':
    main()
