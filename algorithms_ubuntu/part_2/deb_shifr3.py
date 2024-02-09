import sys
from string import digits
# ID - 104536545


def read_data() -> str:
    """Чтение входящей инструкции."""
    return sys.stdin.readline().rstrip()


def find_right_break(encrypted_command: str, left_break_idx: int) -> int:
    """Функция возвращает индекс правой кавычки в строке
    при указанном индексе соответствующей левой ковычки.
    """
    marker = 1
    for i in range(left_break_idx+1, len(encrypted_command)):
        if marker == 0:
            return i - 1

        if encrypted_command[i] == '[':
            marker += 1
        elif encrypted_command[i] == ']':
            marker -= 1

    return i


def decipher(encrypted_command: str) -> str:
    """Функция-расщифровщик инструкции."""
    if '[' not in encrypted_command:
        return encrypted_command

    for i, char in enumerate(encrypted_command):
        if char in digits:
            digit_idx = i
            break

    left_break_idx = encrypted_command.find('[')

    right_break_idx = find_right_break(encrypted_command, left_break_idx)

    return (
        encrypted_command[:digit_idx]
        + (
            int(encrypted_command[digit_idx:left_break_idx])
            * decipher(encrypted_command[left_break_idx+1:right_break_idx])
        ) + decipher(encrypted_command[right_break_idx+1:])
    )


def main():
    print(decipher(read_data()))


if __name__ == '__main__':
    main()
