import sys


def schitalka(n, k):
    if k == 1:
        return n

    candidates = [i + 1 for i in range(n)]

    def recursia(arr, s, old_pos):
        if len(arr) == 1:
            return arr.pop()

        new_pos = (old_pos + s - 1) % len(arr)
        arr.pop(new_pos)
        # print(f'candidates = {arr} / new_pos = {new_pos}')
        return recursia(arr, s, new_pos)

    return recursia(candidates, k, 0)


def main():
    n = int(sys.stdin.readline().rstrip())
    k = int(sys.stdin.readline().rstrip())
    print(schitalka(n, k))


if __name__ == '__main__':
    main()
