import sys


def main():

    def is_correct_bracket_seq(stroka):

        def pare_flg(opened, closed):
            if opened == '(':
                if closed == ')':
                    return True
            if opened == '[':
                if closed == ']':
                    return True
            if opened == '{':
                if closed == '}':
                    return True
            return False

        len_stroka = len(stroka)
        if len_stroka == 0:
            return True
        if len_stroka % 2 == 1:
            return False

        stack = []
        for char in stroka:
            if len(stack) == 0:
                stack.append(char)
            else:
                if pare_flg(stack[-1], char):
                    stack.pop()
                else:
                    stack.append(char)

        return len(stack) == 0

    data = "(){}[]"
    print(data)
    print(is_correct_bracket_seq(data))

    # print(is_correct_bracket_seq(sys.stdin.readline().rstrip()))

if __name__ == '__main__':
    main()
