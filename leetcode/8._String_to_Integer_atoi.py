def myAtoi(s):

    if len(s) == 0:
        return 0

    if s[0] == ' ':
        for i, c in enumerate(s[1:]):
            if c != ' ':
                s = s[i+1:]
                break

    if len(s) == 0:
        return 0

    switch = 1
    if s[0] == '+':
        s = s[1:]
    elif s[0] == '-':
        s = s[1:]
        switch = -1
    elif not s[0].isdigit():
        return 0
    

    answer = ''
    for c in s:
        if c.isdigit():
            answer += c
        else:
            break

    if len(answer) == 0:
        return 0

    answer = int(answer) * switch

    if answer < -2**31:
        return -2**31

    if answer > 2**31 - 1:
        return 2**31 - 1

    return answer


cases = [
    '3.14159',
    'words and 987',
    '   -42',
    '-5-',
    '+1',
    '4193 with words',
    '+-12',
    '000-42a124',
    '0000012',
    "   +0 123",
    '    -88827   5655  U',
    
]

for i, case in enumerate(cases):
    print(i, myAtoi(case))