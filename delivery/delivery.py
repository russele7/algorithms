import sys
# Успешная попытка / 20 дек 2023, 19:34:20 /  ID = 103462171


def main():

    data = list(map(int, sys.stdin.readline().rstrip().split()))
    limit = int(sys.stdin.readline().rstrip())
    data.sort()
    print(data)

    def pares_count(massiv: list, limit: int):
        counter = 0

        while len(massiv) > 0:

            if len(massiv) == 1:
                counter += 1
                break

            elif massiv[0] == limit:
                massiv.pop(0)
                counter += 1
                continue
            else:
                ostatok = limit - massiv[0]

                best_delta = limit
                best_idx_2 = None
                eshe_ne_nashli_flag = True

                for i, m2 in enumerate(massiv[1:]):
                    if ostatok == m2:
                        massiv.pop(i + 1)
                        massiv.pop(0)
                        counter += 1
                        eshe_ne_nashli_flag = False
                        break
                    elif ostatok > m2:
                        delta = ostatok - m2
                        if delta < best_delta:
                            best_idx_2 = i + 1
                            best_delta = delta
                if massiv and eshe_ne_nashli_flag:
                    if best_idx_2:
                        massiv.pop(best_idx_2)

                    massiv.pop(0)
                    counter += 1

        return counter

    print(pares_count(data, limit))


if __name__ == '__main__':
    main()
