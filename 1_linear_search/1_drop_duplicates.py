import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    probs = sys.stdin.readline().rstrip().split()
    cur = 0
    for _ in range(n - 1):
        if probs[cur] == probs[cur + 1]:
            probs.pop(cur + 1)
            probs.append('_')
        else:
            cur += 1
    print(' '.join(probs))


if __name__ == '__main__':
    main()
