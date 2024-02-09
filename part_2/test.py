# ДО
def find_right_break(encrypted_command: str, left_break_idx: int) -> int:
    """Функция возвращает индекс правой кавычки в строке
    при указанном индексе соответствующей левой ковычки.
    """
    marker = 1
    for i in range(left_break_idx+1, len(encrypted_command)):
        if encrypted_command[i] == '[':
            marker += 1
        elif encrypted_command[i] == ']':
            marker -= 1

        if marker == 0:
            return i

# ПОСЛЕ
def find_right_break(encrypted_command: str, left_break_idx: int) -> int:
    marker = 1
    for i in range(left_break_idx+1, len(encrypted_command)):
        if marker == 0:
            return i - 1

        if encrypted_command[i] == '[':
            marker += 1
        elif encrypted_command[i] == ']':
            marker -= 1

    return i
