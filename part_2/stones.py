import sys


def read_data():
    return (
        int(sys.stdin.readline().rstrip()),
        list(map(int, sys.stdin.readline().rstrip().split())),
        int(sys.stdin.readline().rstrip()),
        list(map(int, sys.stdin.readline().rstrip().split())),
    )


def happy_clients(
        n: int,
        orders: list,
        m: int,
        stones: list,
):
    # сортируем
    orders.sort()
    stones.sort()

    # идем по обоим массивам
    counter = 0
    curo = 0
    curs = 0
    # print(
    #     f'orders = {orders}\n'
    #     f'stones = {stones}\n'
    # )

    while True:
        # print(f'curo = {curo} / curs = {curs}')
        if stones[curs] >= orders[curo]:
            counter += 1
            curo += 1
            curs += 1
        else:
            curs += 1
        # print(f'counter = {counter}')

        if (curo == n) or (curs == m):
            break

    return counter


def main():

    n, orders, m, stones = read_data()
    # n = 5
    # orders = [3, 6, 10, 2, 5]
    # m = 4
    # stones = [5, 5, 5, 5]

    # n = 10
    # orders = [8, 5, 5, 8, 6, 9, 8, 2, 4, 7,]
    # m = 8
    # stones = [9, 8, 1, 1, 1, 5, 10, 8,]

    print(happy_clients(n, orders, m, stones))


if __name__ == '__main__':
    main()
