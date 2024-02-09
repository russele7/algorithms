import sys


def schitalka(n, k):
    # if k == 1:
    #     return n

    # candidates = [i + 1 for i in range(n)]

    # old_pos = 0

    # while len(candidates) != 1:
    #     new_pos = (old_pos + k - 1) % len(candidates)
    #     candidates.pop(new_pos)
    #     # print(f'candidates = {candidates} / new_pos = {new_pos}')
    #     old_pos = new_pos

    # return candidates.pop()


    last = 0
    for i in range(1, n + 1):
        last = (last + k) % i
        print(f'last = {last}')
    return last + 1


def main():
    # n = int(sys.stdin.readline().rstrip())
    # k = int(sys.stdin.readline().rstrip())
    n = 5
    k = 2
    print(schitalka(n, k))


if __name__ == '__main__':
    main()
