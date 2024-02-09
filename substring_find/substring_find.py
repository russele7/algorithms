import sys


def main():

    data = sys.stdin.readline().rstrip()

    def max_uniq_length(stroka):

        result = 0
        len_stroka = len(stroka)

        for i in range(len_stroka):
            charset = set()
            sub_result = 0
            for char in stroka[i:]:
                if char not in charset:
                    sub_result += 1
                    charset.add(char)
                else:
                    break
            
            result = max(result, sub_result)

            if result == len_stroka - i:
                break

        return result

    print(max_uniq_length(data))

if __name__ == '__main__':
    main()
