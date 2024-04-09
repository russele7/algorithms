def reverse(x):

    # учет знака
    switch = 1
    if x < 0:
        x = abs(x)
        switch = -1

    delitel = 10
    answer = 0
    while True:

        ostatok = (x % delitel) // (delitel / 10)

        if not -(2**31) <= answer * 10 * switch <= 2**31 - 1:
            return 0

        answer *= 10
        answer += ostatok

        if delitel > x:
            break
        delitel *= 10

    return int(answer * switch)

x = 0

print(reverse(x))
